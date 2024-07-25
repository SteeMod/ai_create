import streamlit as st
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
import os
from csv import DictWriter
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    try:
        endpoint = os.getenv('FORM_RECOGNIZER_ENDPOINT', "https://new2two.cognitiveservices.azure.com/")
        credential = AzureKeyCredential(os.getenv('FORM_RECOGNIZER_API_KEY', "027ad9245a594c5886cf5d90abecb9d1"))
        client = DocumentAnalysisClient(endpoint, credential)

        model_id = os.getenv('FORM_RECOGNIZER_CUSTOM_MODEL_ID', "Thessa5vs6")

        # Create BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(os.getenv('AZURE_STORAGE_CONNECTION_STRING', "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"))
        container_client = blob_service_client.get_container_client(os.getenv('BLOB_CONTAINER_NAME', "data1"))

        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_extension = os.path.splitext(original_blob_name)[1]
        timestamped_blob_name = f"{timestamp}{file_extension}"

        block_blob_client = container_client.get_blob_client(original_blob_name)

        # Check if the blob exists
        if not block_blob_client.exists():
            logging.error(f"Blob '{original_blob_name}' does not exist.")
            return

        # Download blob content to a stream
        downloader = block_blob_client.download_blob()
        blob_stream = downloader.readall()

        # Save the PDF to local storage
        with open(timestamped_blob_name, 'wb') as pdf_file:
            pdf_file.write(blob_stream)

        # Create a new blob client for the PDF file
        pdf_blob_client = container_client.get_blob_client(timestamped_blob_name)

        # Upload the PDF to Azure Blob Storage
        with open(timestamped_blob_name, 'rb') as data:
            pdf_blob_client.upload_blob(data, overwrite=True)

        logging.info(f"PDF file '{timestamped_blob_name}' downloaded and uploaded successfully.")

        poller = client.begin_analyze_document(model_id=model_id, document=blob_stream)
        result = poller.result()

        if not result.documents:
            raise Exception("Expected at least one document in the result.")

        document = result.documents[0]

        # Create a CSV writer
        csv_filename = f'result_{timestamp}.csv'
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [name for name in document.fields.keys()]
            writer = DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Transform document.fields into a format suitable for csv-writer
            record = {}
            for key, field in document.fields.items():
                if field.value_type == 'dictionary' and field.value and 'rows' in field.value:
                    # Check if the object is a table
                    if isinstance(field.value['rows'], list):
                        # Handle table data
                        for rowIndex, row in enumerate(field.value['rows']):
                            if row and isinstance(row, list):
                                for cellIndex, cell in enumerate(row):
                                    record[f"{key}_row{rowIndex}_cell{cellIndex}"] = cell.content
                else:
                    # Handle regular fields
                    record[key] = field.content if field.content else field.value

            writer.writerow(record)

        # Create a new blob client for the CSV file
        csv_blob_client = container_client.get_blob_client(csv_filename)

        # Upload the CSV file to Azure Blob Storage
        with open(csv_filename, 'rb') as data:
            csv_blob_client.upload_blob(data, overwrite=True)

        logging.info(f"CSV file '{csv_filename}' uploaded successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        main()
