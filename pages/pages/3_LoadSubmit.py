import streamlit as st
from werkzeug.utils import secure_filename
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
import os
from csv import DictWriter
import asyncio
import tempfile

async def process_file(file_path, filename):
    # Hardcoded variables
    endpoint = "https://new2two.cognitiveservices.azure.com/"
    api_key = "027ad9245a594c5886cf5d90abecb9d1A"
    model_id = "Thessa5vs6"
    connection_string = "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"
    container_name = "data1"

    credential = AzureKeyCredential(api_key)
    client = DocumentAnalysisClient(endpoint, credential)

    # Create BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(filename)

    # Upload the PDF file to Azure Blob Storage
    with open(file_path, 'rb') as data:
        blob_client.upload_blob(data, overwrite=True)

    # Send PDF to Azure AI Document Intelligence
    with open(file_path, 'rb') as data:
        poller = await client.begin_analyze_document(model_id=model_id, document=data)
    result = await poller.result()

    if not result.documents:
        raise Exception("Expected at least one document in the result.")

    document = result.documents[0]

    # Save analysis result as CSV
    csv_filename = 'result_' + filename.split('.')[0] + '.csv'
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [name for name in document.fields.keys()]
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        record = {key: field.content if field.content else field.value for key, field in document.fields.items()}
        writer.writerow(record)

    # Upload the CSV file to Azure Blob Storage
    csv_blob_client = container_client.get_blob_client(csv_filename)
    with open(csv_filename, 'rb') as data:
        csv_blob_client.upload_blob(data, overwrite=True)

    # Clean up local files
    os.remove(file_path)
    os.remove(csv_filename)

def main():
    st.title('Azure AI Document Intelligence with Streamlit')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            tmp_file_path = tmp_file.name
        
        if os.path.exists(tmp_file_path):
            asyncio.run(process_file(tmp_file_path, uploaded_file.name))
            st.write('File has been processed and saved to Blob Storage.')
        else:
            st.write('Error: File was not saved correctly.')
    else:
        st.write('No file provided or file is empty.')

if __name__ == '__main__':
    main()