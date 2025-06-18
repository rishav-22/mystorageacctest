from flask import Flask
import requests
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

app = Flask(__name__)

@app.route("/")
def home():
    return "App Service is running!"

@app.route("/sas")
def sas_access():
    sas_url = "https://mystorageaccountlabvwits.blob.core.windows.net/?sv=2024-11-04&ss=b&srt=co&sp=rtfx&se=2025-06-21T03:24:53Z&st=2025-06-18T19:24:53Z&spr=https&sig=raG%2ByH2lX%2F1TPvunL6zdHkNTUMkyd7j87w%2BB7SP%2BaPw%3D"
    response = requests.get(sas_url)
    return response.text if response.status_code == 200 else "SAS Access Failed"

# @app.route("/entra")
# def entra_access():
#     credential = DefaultAzureCredential()
#     blob = BlobClient(
#         account_url="https://mystorageaccountlabvwits.blob.core.windows.net",
#         container_name="testcontainer",
#         blob_name="sample.txt",
#         credential=credential
#     )
#     data = blob.download_blob().readall()
#     return data.decode()

if __name__ == "__main__":
    app.run()
