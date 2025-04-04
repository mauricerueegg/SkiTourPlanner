import os
import pickle
from pathlib import Path

import pandas as pd
from azure.storage.blob import BlobServiceClient
from flask import Flask, jsonify, request
from flask_cors import CORS

# Flask-App initialisieren
app = Flask(__name__)
CORS(app)  # CORS für alle Routen aktivieren

print("*** Init and load model ***")

# Überprüfen, ob die Umgebungsvariable gesetzt ist
if 'AZURE_STORAGE_CONNECTION_STRING' in os.environ:
    azureStorageConnectionString = os.environ['AZURE_STORAGE_CONNECTION_STRING']
    blob_service_client = BlobServiceClient.from_connection_string(azureStorageConnectionString)

    print("Fetching blob containers...")
    containers = blob_service_client.list_containers(include_metadata=True)

    # Debugging: Liste der Container ausgeben
    print("Gefundene Container:")
    container_names = [container.name for container in containers]
    for name in container_names:
        print(name)

    # Filtere Container, die mit "skitourplanner-model" beginnen
    filtered_containers = [
        name for name in container_names if name.startswith("skitourplanner-model")
    ]

    if not filtered_containers:
        raise ValueError("Keine Container gefunden, die mit 'skitourplanner-model' beginnen.")

    # Bestimme den höchsten Suffix-Wert
    suffix = max(
        int(name.split("-")[-1]) for name in filtered_containers
    )
    model_folder = f"skitourplanner-model-{suffix}"
    print(f"Using model folder: {model_folder}")

    # Lade das Modell aus dem Blob-Container
    container_client = blob_service_client.get_container_client(model_folder)
    blob_list = container_client.list_blobs()
    blob_name = next(blob.name for blob in blob_list)

    # Lade das Modell in den lokalen Speicher
    Path("../model").mkdir(parents=True, exist_ok=True)
    download_file_path = os.path.join("../model", "gradient_boosting_model.pkl")
    print(f"Downloading blob to {download_file_path}")

    with open(file=download_file_path, mode="wb") as download_file:
        download_file.write(container_client.download_blob(blob_name).readall())

else:
    raise EnvironmentError("CANNOT ACCESS AZURE BLOB STORAGE - Please set AZURE_STORAGE_CONNECTION_STRING.")

# Lade das Modell aus der lokalen Datei
file_path = Path("../model/gradient_boosting_model.pkl")
if not file_path.exists():
    raise FileNotFoundError(f"Modell-Datei nicht gefunden: {file_path}")

with open(file_path, 'rb') as fid:
    model = pickle.load(fid)

# Überprüfen, ob das Modell eine `predict`-Methode hat
if not hasattr(model, "predict"):
    raise ValueError("Das geladene Modell unterstützt keine 'predict'-Methode. Bitte überprüfen Sie die Modell-Datei.")

print("*** Sample calculation with model ***")

@app.route("/api/predict", methods=["POST"])
def predict_lawinenrisiko():
    """
    API-Endpunkt, um das Lawinenrisiko vorherzusagen.
    """
    try:
        # JSON-Daten aus der Anfrage abrufen
        data = request.get_json()

        # Eingabedaten in ein DataFrame umwandeln
        input_df = pd.DataFrame([data])

        # Vorhersage mit dem Modell durchführen
        prediction = model.predict(input_df)
        lawinenrisiko = prediction[0]

        # Ergebnis als JSON zurückgeben
        return jsonify({
            'lawinenrisiko': lawinenrisiko,
            'input': data
        })
    except Exception as e:
        return jsonify({'error': f"Fehler bei der Vorhersage: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)