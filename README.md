# 🏔️ SkiTourPlanner

*Sichere Skitourenplanung mit Machine Learning – Vorhersage von Lawinenrisiken auf Basis öffentlicher Tourdaten.*

---

## 📦 Projektübersicht

SkiTourPlanner ist eine Webanwendung zur Vorhersage von Lawinenrisiken basierend auf automatisch gesammelten Skitourendaten. Die Anwendung kombiniert Daten-Scraping, ein Machine-Learning-Modell, Azure-Cloud-Deployment und eine moderne Weboberfläche mit SvelteKit.

---

## 🔁 Datenpipeline

### 🧹 Scraper

- Scraped täglich neue Touren von [skitourenguru.ch](https://www.skitourenguru.ch)
- Ausgabeformat: `.jl` (JSON Lines)
- Daten werden in eine MongoDB-Datenbank geladen (lokal oder Azure Cosmos DB)

### 📊 Modelltraining

- Modell: Gradient Boosting Regressor
- Bewertungskriterien:
  - **R²-Score** (je näher an 1, desto besser)
  - **MSE** (Mean Squared Error – je kleiner, desto besser)
- Das trainierte Modell wird als `.pkl` Datei gespeichert (`model/gradient_boosting_model.pkl`)

---

## ☁️ Azure Blob Storage

- Modellversionierung im Azure Blob Storage
- Zugriff per Zugriffsschlüssel:
  - Als **Umgebungsvariable** in Docker (`AZURE_STORAGE_KEY`)
  - Als **Secret** in GitHub Actions (`AZURE_STORAGE_KEY`)

---

## ⚙️ Automatisierung mit GitHub Actions

Jeder Push kann automatisch folgende Schritte auslösen:

1. Ausführen des Scrapers
2. Laden neuer Daten in MongoDB
3. Trainieren & Speichern eines aktualisierten Modells
4. Upload des Modells in Azure Blob Storage
5. Docker-Build & Deployment auf Azure

---

## 🚀 App-Architektur

### 🖥️ Backend

- Python Flask REST-API (`backend/app.py`)
- Lädt das aktuellste Modell aus Azure Blob Storage
- Berechnet Lawinenrisiko anhand übermittelter Tour-Merkmale

### 🌐 Frontend

- Modernes UI mit **SvelteKit**
- Benutzer wählt Tour aus → Risikoanzeige in **Farben (grün, orange, rot)** + evtl. Diagramm
- Statische Dateien werden ins Backend eingebunden (Docker-Build)

---

## 🐳 Deployment mit Docker

- Basis: Python-Image
- Schritte:
  - Installieren der Dependencies via `pip`
  - Kopieren des Frontends (prebuilt, später automatisch builden)
  - Einbinden des Azure Zugriffsschlüssels als Umgebungsvariable
- Bereitstellung über Azure Container App / App Service

---

## 📌 Requirements aktualisieren

```bash
# Altes requirements.txt löschen
rm requirements.txt

# Neues venv erstellen
python -m venv .venv
source .venv/bin/activate

# Installieren & einfrieren
pip install -r dev-requirements.in
pip-compile requirements.in
pip install -r requirements.txt