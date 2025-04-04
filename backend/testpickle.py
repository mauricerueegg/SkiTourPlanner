import joblib
import pandas as pd
import joblib
import pandas as pd

# Öffne die .pkl-Datei mit joblib
model = joblib.load('../model/gradient_boosting_model.pkl')

print(f"Methoden des Modells: {dir(model)}")


"""
# Öffne die .pkl-Datei mit joblib
model = joblib.load('../model/gradient_boosting_model.pkl')

print(f"Methoden des Modells: {dir(model)}")


# Beispiel-Eingabedaten für die Vorhersage
example_input = {
    "Höhendifferenz": 1000,  # Beispielwert in Metern
    "Routenlänge": 2000,    # Beispielwert in Metern
    "Schnee": 2000.0,       # Beispielwert in cm
    "Gipfelhöhe": 3000,     # Beispielwert in Metern
}
# Eingabedaten in ein DataFrame umwandeln
input_df = pd.DataFrame([example_input])

# Vorhersage durchführen
try:
    prediction = model.predict(input_df)
    print(f"Beispiel-Eingabe: {example_input}")
    print(f"Vorhergesagtes Lawinenrisiko: {prediction[0]}")
except Exception as e:
    print(f"Fehler bei der Vorhersage: {e}")
"""