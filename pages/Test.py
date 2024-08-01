1_Download.py



import streamlit as st
from azure.storage.blob import BlobServiceClient
import io
import base64
import os

st.title("Download Medication Intake Tracker Form")

# Retrieve Azure blob storage connection string from environment variable
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
if not connection_string:
    st.error("Azure Storage connection string is not set in environment variables.")
    st.stop()

container_name = "data1"

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

try:
    # Get a list of blobs in the container
    blob_list = blob_service_client.get_container_client(container_name).list_blobs()

    # Get the names of the blobs (files) in the container
    # Only select files with prefix 'form_'
    file_list = [blob.name for blob in blob_list if blob.name.startswith('form_')]

    if not file_list:
        st.warning("No files found with the prefix 'form_'.")
        st.stop()

    # Create a dropdown list for the user to select a file
    selected_file = st.selectbox('Select a file to download', file_list)

    # Function to get file content given file name
    def get_file_content(file_name):
        blob_client = blob_service_client.get_blob_client(container_name, file_name)
        download_stream = blob_client.download_blob().readall()

        # Create a BytesIO object
        pdf_data = io.BytesIO(download_stream)

        return pdf_data

    # Get the content of the selected file
    file_content = get_file_content(selected_file)

    # Convert the BytesIO object to base64 encoded string
    b64 = base64.b64encode(file_content.getvalue()).decode()

    # Display the selected file content
    st.text("Displaying the selected file:")
    st.markdown(f'<embed src="data:application/pdf;base64,{b64}" width="700" height="800" type="application/pdf">', unsafe_allow_html=True)

except Exception as e:
    st.error(f"An error occurred: {e}")