import json
import os
import argparse
from pymongo import MongoClient

def import_to_mongodb(mongo_uri, db_name, collection_name, input_file):
    # Verbindung zu MongoDB herstellen
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Daten aus der .jl-Datei lesen und in MongoDB einfügen
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            collection.insert_one(doc)

    print(f"✅ Daten erfolgreich in {db_name}.{collection_name} importiert")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Importiere Daten in MongoDB.")
    parser.add_argument("-u", "--uri", required=True, help="MongoDB-Verbindungs-URI")
    parser.add_argument("-c", "--collection", required=True, help="Name der MongoDB-Collection")
    parser.add_argument("-i", "--input", required=True, help="Pfad zur Eingabedatei (.jl)")

    args = parser.parse_args()

    # Standard-Datenbankname
    DB_NAME = "skitouren"

    import_to_mongodb(args.uri, DB_NAME, args.collection, args.input)





