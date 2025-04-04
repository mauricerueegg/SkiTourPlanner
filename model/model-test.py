import pickle
import pandas as pd

# Modellpfad
model_path = "gradient_boosting_model.pkl"

# Testdaten
test_data = pd.DataFrame([{
    "Gipfel": "Schollenhorn",
    "Start": "Splügen",
    "Höhendifferenz": 1270,
    "Routenlänge": 4734,
    "Aufstiegszeit": 4,  # in Stunden
    "Schwierigkeitsgrad": "WS+"
}])

# Vorverarbeitung der Testdaten (falls nötig)
def preprocess_test_data(data):
    # Beispiel: Schwierigkeitsgrad in numerischen Wert umwandeln
    schwierigkeit_mapping = {"L": 1, "WS": 2, "WS+": 3, "ZS": 4, "ZS+": 5, "S": 6, "S+": 7}
    data["Schwierigkeitsgrad_num"] = data["Schwierigkeitsgrad"].map(schwierigkeit_mapping)
    return data[["Höhendifferenz", "Routenlänge", "Aufstiegszeit", "Schwierigkeitsgrad_num"]]

# Testdaten vorverarbeiten
processed_data = preprocess_test_data(test_data)

# Modell laden
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
        print(f"Geladenes Modell: {type(model)}")
except Exception as e:
    print(f"Fehler beim Laden des Modells: {e}")
    exit()

# Vorhersage durchführen
try:
    predictions = model.predict(processed_data)
    print(f"Vorhersage für das Lawinenrisiko: {predictions[0]}")
except Exception as e:
    print(f"Fehler bei der Vorhersage: {e}")