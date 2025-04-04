import datetime
import os
import pickle
from pathlib import Path
from joblib import load  # Importiere joblib.load


import pandas as pd
from azure.storage.blob import BlobServiceClient
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

# Init app and load model from storage
print("*** Init and load model ***")
if 'AZURE_STORAGE_CONNECTION_STRING' in os.environ:
    azureStorageConnectionString = os.environ['AZURE_STORAGE_CONNECTION_STRING']
    blob_service_client = BlobServiceClient.from_connection_string(azureStorageConnectionString)

    print("Fetching blob containers...")
    containers = blob_service_client.list_containers(include_metadata=True)
    suffix = max(
        int(container.name.split("-")[-1])
        for container in containers
        if container.name.startswith("skitourplanner-model")
    )
    model_folder = f"skitourplanner-model-{suffix}"
    print(f"Using model {model_folder}")

    container_client = blob_service_client.get_container_client(model_folder)
    blob_list = container_client.list_blobs()
    blob_name = next(blob.name for blob in blob_list)

    # Download the blob to a local file
    Path("../model").mkdir(parents=True, exist_ok=True)
    download_file_path = os.path.join("../model", "gradient_boosting_model.pkl")
    print(f"Downloading blob to {download_file_path}")

    with open(file=download_file_path, mode="wb") as download_file:
        download_file.write(container_client.download_blob(blob_name).readall())

else:
    print("CANNOT ACCESS AZURE BLOB STORAGE - Please set AZURE_STORAGE_CONNECTION_STRING. Current env: ")
    print(os.environ)

# Lade das Modell
file_path = Path(".", "../model/", "gradient_boosting_model.pkl")
model = load(file_path)  # Verwende joblib.load statt pickle.load
print(f"Geladenes Modell: {type(model)}")  # Sollte <class 'sklearn.ensemble._gb.GradientBoostingRegressor'> sein

# Überprüfen, ob das Modell korrekt geladen wurde
if not hasattr(model, "predict"):
    raise ValueError("Das geladene Modell unterstützt keine 'predict'-Methode. Bitte überprüfen Sie die Modell-Datei.")

print("*** Sample calculation with model ***")

def lawinenrisiko_predictor(Höhendifferenz, Routenlänge, Schnee, Gipfelhöhe):
    """
    Sagt das Lawinenrisiko basierend auf den Eingabeparametern vorher.
    """
    # Eingabedaten für das Modell vorbereiten
    demoinput = [[Höhendifferenz, Routenlänge, Schnee, Gipfelhöhe]]
    demodf = pd.DataFrame(columns=['Höhendifferenz', 'Routenlänge', 'Schnee', 'Gipfelhöhe'], data=demoinput)

    # Modellvorhersage durchführen
    try:
        demooutput = model.predict(demodf)
        lawinenrisiko = demooutput[0]
    except Exception as e:
        print(f"Fehler bei der Modellvorhersage: {e}")
        lawinenrisiko = None

    print(f"Our Model predicted Lawinenrisiko: {lawinenrisiko}")
    return lawinenrisiko


@app.route("/api/predict", methods=["GET"])
def predict_lawinenrisiko():
    """
    API-Endpunkt, um das Lawinenrisiko vorherzusagen.
    """
    # Eingabeparameter aus der Anfrage abrufen
    Höhendifferenz = request.args.get('Höhendifferenz', default=0, type=int)
    Routenlänge = request.args.get('Routenlänge', default=0, type=int)
    Schnee = request.args.get('Schnee', default=0, type=float)
    Gipfelhöhe = request.args.get('Gipfelhöhe', default=0, type=int)

    # Eingabedaten für das Modell vorbereiten
    demoinput = [[Höhendifferenz, Routenlänge, Schnee, Gipfelhöhe]]
    demodf = pd.DataFrame(columns=['Höhendifferenz', 'Routenlänge', 'Schnee', 'Gipfelhöhe'], data=demoinput)

    # Vorhersage mit dem Modell durchführen
    try:
        demooutput = model.predict(demodf)
        lawinenrisiko = demooutput[0]  # Annahme: Das Modell gibt das Lawinenrisiko zurück
    except Exception as e:
        return jsonify({'error': f"Fehler bei der Vorhersage: {str(e)}"}), 500

    # Ergebnis als JSON zurückgeben
    return jsonify({
        'lawinenrisiko': lawinenrisiko,
        'Höhendifferenz': Höhendifferenz,
        'Routenlänge': Routenlänge,
        'Schnee': Schnee,
        'Gipfelhöhe': Gipfelhöhe
    })