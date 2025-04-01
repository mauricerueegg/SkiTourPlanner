import argparse
import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib  # Zum Speichern & Laden von Modellen

def connect_to_mongo(uri, db_name, collection_name):
    """Stellt eine Verbindung zu MongoDB her und gibt die Collection zurück."""
    client = MongoClient(uri)
    db = client[db_name]
    return db[collection_name]

def load_data_from_mongo(collection):
    """Lädt Daten aus MongoDB und gibt sie als DataFrame zurück."""
    data = list(collection.find())
    if not data:
        raise ValueError("Keine Daten in der MongoDB-Collection gefunden.")
    return pd.DataFrame(data)

def preprocess_data(df):
    """Verarbeitet die Daten und bereitet sie für das Modell vor."""
    df = df.dropna()  # Entferne fehlende Werte
    df["Gipfelhöhe"] = df["Gipfel"].str.extract(r"(\d+)").astype(int)
    df["Höhendifferenz"] = df["Höhendifferenz"].str.replace("\u2006", "", regex=False).str.replace("hm", "", regex=False).astype(int)
    df["Routenlänge"] = df["Routenlänge"].str.replace("\u2006", "", regex=False).str.replace("m", "", regex=False).astype(int)
    df["Schnee"] = df["Schnee"].str.extract(r"Ø (\d+)").astype(int)
    df["Lawinenrisiko"] = df["Lawinenrisiko"].astype(float)

    def transform_difficulty(value):
        base_mapping = {"L": 2.0, "WS": 3.0, "ZS": 4.0, "S": 5.0, "SS": 6.0}
        modifier = 0.3 if "+" in value else -0.3 if "-" in value else 0.0
        for key in base_mapping:
            if key in value:
                return base_mapping[key] + modifier
        return None

    df["Schwierigkeitsgrad_num"] = df["Schwierigkeitsgrad"].apply(transform_difficulty)
    return df

def train_model(X, y):
    """Trainiert ein Gradient Boosting Modell und gibt das beste Modell zurück."""
    param_grid = {"n_estimators": [50, 100, 200], "learning_rate": [0.05, 0.1, 0.2], "max_depth": [2, 3, 4]}
    grid = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid, cv=5, scoring="r2", n_jobs=-1)
    grid.fit(X, y)
    return grid.best_estimator_

def main():
    # Argumente für MongoDB-Verbindung
    parser = argparse.ArgumentParser(description="Trainiere ein Modell basierend auf MongoDB-Daten.")
    parser.add_argument("-u", "--uri", required=True, help="MongoDB-Verbindungs-URI mit Benutzername/Passwort")
    args = parser.parse_args()

    # MongoDB-Verbindung
    mongo_uri = args.uri
    mongo_db = "skitouren"
    mongo_collection = "skitour"

    try:
        collection = connect_to_mongo(mongo_uri, mongo_db, mongo_collection)
        df = load_data_from_mongo(collection)
        print("✅ Daten erfolgreich aus MongoDB geladen.")

        # Datenvorverarbeitung
        df = preprocess_data(df)
        print("✅ Daten erfolgreich vorverarbeitet.")

        # Features und Zielvariable
        numerical_features = ["Höhendifferenz", "Routenlänge", "Schnee", "Gipfelhöhe", "Schwierigkeitsgrad_num"]
        X = df[numerical_features]
        y = df["Lawinenrisiko"]

        # Train-Test-Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Modelltraining
        best_model = train_model(X_train, y_train)
        print("✅ Modell erfolgreich trainiert.")

        # Evaluation
        y_pred = best_model.predict(X_test)
        print("R²-Score:", r2_score(y_test, y_pred))
        print("MSE:", mean_squared_error(y_test, y_pred))

        # Modell speichern
        joblib.dump(best_model, "gradient_boosting_model.pkl")
        print("✅ Modell gespeichert als 'gradient_boosting_model.pkl'.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

if __name__ == "__main__":
    main()