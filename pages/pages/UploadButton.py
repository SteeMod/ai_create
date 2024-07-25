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

def main(uploaded_file):
    try:
        endpoint = os.getenv('FORM_RECOGNIZER_ENDPOINT')
        credential = AzureKeyCredential(os.getenv('FORM_RECOGNIZER_API_KEY'))
        client = DocumentAnalysisClient(endpoint, credential)

        model_id = os.getenv('FORM_RECOGNIZER_CUSTOM_MODEL_ID')

        # Create BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(os.getenv('AZURE_STORAGE_CONNECTION_STRING'))
        container_client = blob_service_client.get_container_client(os.getenv('BLOB_CONTAINER_NAME'))

        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        original_blob_name = uploaded_file.name
        file_extension = os.path.splitext(original_blob_name)[1]
        timestamped_blob_name = f"{timestamp}{file_extension}"

        # Create a new blob client for the PDF file
        pdf_blob_client = container_client.get_blob_client(timestamped_blob_name)

        # Upload the PDF to Azure Blob Storage
        pdf_blob_client.upload_blob(uploaded_file, overwrite=True)

        logging.info(f"PDF file '{timestamped_blob_name}' uploaded successfully.")

        poller = client.begin_analyze_document(model_id=model_id, document=uploaded_file)
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
        main(uploaded_file)
