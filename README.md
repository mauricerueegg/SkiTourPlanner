# HikePlanner

inspired by https://blog.mimacom.com/data-collection-scrapy-hiketime-prediction/
similar dataset https://www.kaggle.com/datasets/roccoli/gpx-hike-tracks

## Spider

* Scrape regularly for new / additional data
* Output file.jl (json list)
* Load data into MongoDB
* Update model
    * Produce correlation heatmap
    * Check R2 (bigger and close to 1 is better)
    * Check MSE (lower better, square seconds)
* Save model to model/GradientBoostingRegressor.pkl

## Azure Blob Storage

* Save model to Azure Blob Storage
* Always save new version of model
* Zugriff: Speicherkonto > Zugriffsschlüssel
    * Als Umgebungsvariable für Docker
    * Als Secret für GitHub

## GitHub Action

* Scrape
* Load data to MongoDB (Azure Cosmos DB)
* Update model and save to Azure Blob Storage

## App
* Backend: Python Flask (backend/app.py)
* Frontend: SvelteKit (build still manually)

## Deployment with Docker

* Dockerfile
* Install dependencies with pip
* Copy Frontend (prebuilt, TODO Build)
* Azure Blob Storage: Zugriffsschlüssel als Umgebungsvariable

## Update Requirements

* Delete requirements.txt
* Create .venv
* pip install -r dev-requirements.in
* pip-compile requirements.in
* pip install -r requirements.txt

## Ideas

* Personalized Model
    * For a specific Hikr user
    * z.B. 100 weitere "neue" Daten eines bestimmten Benutzers 



## maurice
cd skitouren_scraper       

python scraper.py 


python mongo_import.py -c skitour -i downloads/skitouren_daten.jl -u 'mongodb+srv://mongodb:gAqtam-segves-rojri4@mdmcluster.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000'

cd ..             

cd model 

python model.py -u 'mongodb+srv://mongodb:gAqtam-segves-rojri4@mdmcluster.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000' 


cd model

python save.py -c "DefaultEndpointsProtocol=https;AccountName=rueegmauzhaw;AccountKey=6Mv3hMP3FdZMsE4u9Q0pRpi3/z8CSYyBpSUuFMo/PZpzn7npWSg3Tufkh7yuUY2IOLAzE2CUWPFa+AStBS0fNA==;EndpointSuffix=core.windows.net" 

export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=rueegmauzhaw;AccountKey=6Mv3hMP3FdZMsE4u9Q0pRpi3/z8CSYyBpSUuFMo/PZpzn7npWSg3Tufkh7yuUY2IOLAzE2CUWPFa+AStBS0fNA==;EndpointSuffix=core.windows.net"          

echo $AZURE_STORAGE_CONNECTION_STRING 


curl -X POST http://127.0.0.1:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Höhendifferenz": 1000,
    "Routenlänge": 2000,
    "Schnee": 200,
    "Gipfelhöhe": 3000
}'

{
  "lawinenrisiko": 2.049204631595841
}