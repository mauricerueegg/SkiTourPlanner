# model.py
import argparse
import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

class AvalancheRiskModel:
    def __init__(self, model):
        self.model = model

    def predict(self, input_data):
        input_df = pd.DataFrame([input_data])
        prediction = self.model.predict(input_df)
        return prediction[0]

def connect_to_mongo(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    return db[collection_name]

def load_data_from_mongo(collection):
    data = list(collection.find())
    if not data:
        raise ValueError("Keine Daten in der MongoDB-Collection gefunden.")
    return pd.DataFrame(data)

def preprocess_data(df):
    df = df.dropna()
    df["Gipfelhöhe"] = df["Gipfel"].str.extract(r"(\d+)").astype(int)
    df["Höhendifferenz"] = df["Höhendifferenz"].str.replace("\u2006", "", regex=False).str.replace("hm", "", regex=False).astype(int)
    df["Routenlänge"] = df["Routenlänge"].str.replace("\u2006", "", regex=False).str.replace("m", "", regex=False).astype(int)
    df["Schnee"] = df["Schnee"].str.extract(r"\u00d8\s?(\d+)").astype(int)
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
    param_grid = {
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.05, 0.1, 0.2],
        "max_depth": [2, 3, 4]
    }
    grid = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid, cv=5, scoring="r2", n_jobs=-1)
    grid.fit(X, y)
    print(f"Beste Parameter: {grid.best_params_}")
    return grid.best_estimator_

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--uri", required=True, help="MongoDB URI")
    args = parser.parse_args()

    collection = connect_to_mongo(args.uri, "skitouren", "skitour")
    df = load_data_from_mongo(collection)
    print("✅ Daten geladen")
    df = preprocess_data(df)
    print("✅ Daten vorverarbeitet")

    X = df[["Höhendifferenz", "Routenlänge", "Schnee", "Gipfelhöhe"]]
    y = df["Lawinenrisiko"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    print("✅ Modell trainiert")

    y_pred = model.predict(X_test)
    print("R²-Score:", r2_score(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))

    joblib.dump(AvalancheRiskModel(model), "gradient_boosting_model.pkl")
    print("✅ Modell gespeichert")

if __name__ == "__main__":
    main()