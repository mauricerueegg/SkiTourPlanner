
# save.py
import os
import argparse
from azure.storage.blob import BlobServiceClient

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--connection", required=True, help="Azure connection string")
args = parser.parse_args()

client = BlobServiceClient.from_connection_string(args.connection)
containers = client.list_containers()

suffix = 0
for container in containers:
    if container.name.startswith("skitourplanner-model"):
        try:
            suffix = max(suffix, int(container.name.split("-")[-1]))
        except:
            continue

suffix += 1
container_name = f"skitourplanner-model-{suffix}"
print(f"Erstelle Container: {container_name}")
client.create_container(container_name)

blob_client = client.get_blob_client(container_name, "gradient_boosting_model.pkl")
with open("gradient_boosting_model.pkl", "rb") as data:
    blob_client.upload_blob(data)
print("✅ Modell hochgeladen")
