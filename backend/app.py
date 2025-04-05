# app.py
import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from azure.storage.blob import BlobServiceClient
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Verbindungszeichenkette prüfen
if 'AZURE_STORAGE_CONNECTION_STRING' not in os.environ:
    raise EnvironmentError("Setze AZURE_STORAGE_CONNECTION_STRING")

# Azure Blob Storage initialisieren
conn_str = os.environ['AZURE_STORAGE_CONNECTION_STRING']
client = BlobServiceClient.from_connection_string(conn_str)

# Neueste Modell-Container ermitteln
containers = [c.name for c in client.list_containers() if c.name.startswith("skitourplanner-model")]
suffix = max(int(name.split("-")[-1]) for name in containers)
container_name = f"skitourplanner-model-{suffix}"

# Modell aus Blob Storage herunterladen
blob_client = client.get_blob_client(container_name, "gradient_boosting_model.pkl")
Path("model").mkdir(exist_ok=True)
local_path = "model/gradient_boosting_model.pkl"
with open(local_path, "wb") as file:
    file.write(blob_client.download_blob().readall())
print("✅ Modell heruntergeladen")

# Modell laden
model = joblib.load(local_path)

# API-Endpunkte
@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()

        if isinstance(input_data, dict):
            df = pd.DataFrame([input_data])
        elif isinstance(input_data, pd.DataFrame):
            df = input_data
        else:
            raise ValueError("Ungültiges Eingabeformat")

        result = model.predict(df)
        return jsonify({"lawinenrisiko": float(result[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def hello():
    return "✅ Backend läuft!"

if __name__ == "__main__":
    app.run(debug=True)