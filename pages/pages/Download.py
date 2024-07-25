import streamlit as st
import base64
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import io
import PyPDF2

# Azure blob storage details
connection_string = "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"
container_name = "data1"

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get a list of blobs in the container
blob_list = blob_service_client.get_container_client(container_name).list_blobs()

# Get the names of the blobs (files) in the container
# Only select files with prefix 'form_'
file_list = [blob.name for blob in blob_list if blob.name.startswith('form_')]

# Create a dropdown list for the user to select a file
selected_file = st.selectbox('Select a file to download', file_list)

# Function to get file content given file name
def get_file_content(file_name):
    blob_client = blob_service_client.get_blob_client(container_name, file_name)
    download_stream = blob_client.download_blob().readall()

    # Create a BytesIO object
    pdf_data = io.BytesIO(download_stream)

    # Create a PDF file reader
    pdf_reader = PyPDF2.PdfReader(pdf_data)

    # Initialize an empty string to hold the PDF text
    pdf_text = ""

    # Loop through each page in the PDF and extract the text
    for page_num in range(pdf_reader.numPages):
        pdf_text += pdf_reader.getPage(page_num).extractText()

    return pdf_text

# Get the content of the selected file
file_content = get_file_content(selected_file)

# Display the selected file content
st.text("Displaying the content of the selected file:")
st.write(file_content)
