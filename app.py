from flask import Flask
import requests
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ App Service is running!"

@app.route("/sas")
def sas_access():
    # Replace <SAS_TOKEN> with your actual SAS token (URL-encoded)
    sas_url = "https://mystorageaccountlabvwits.blob.core.windows.net/testcontainer?sp=r&st=2025-06-18T20:30:35Z&se=2025-06-27T04:30:35Z&spr=https&sv=2024-11-04&sr=c&sig=5NeaByaI9TEbnLEet%2BBjoDGLuDahAgVdzeh1%2BZNHdI8%3D"
    response = requests.get(sas_url)
    if response.status_code == 200:
        return f"✅ SAS Access Successful:\n\n{response.text}"
    else:
        return f"❌ SAS Access Failed: {response.status_code}"

@app.route("/entra")
def entra_access():
    try:
        credential = DefaultAzureCredential()
        blob = BlobClient(
            account_url="https://mystorageaccountlab.blob.core.windows.net",
            container_name="testcontainer",
            blob_name="sample.txt",
            credential=credential
        )
        data = blob.download_blob().readall()
        return f"✅ Entra ID Access Successful:\n\n{data.decode()}"
    except Exception as e:
        return f"❌ Entra ID Access Failed:\n\n{str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
