import streamlit as st
import base64
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

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
    download_stream = blob_client.download_blob()
    return download_stream.readall()

# Function to make the file downloadable
def get_download_link(file_name, file_content):
    b64 = base64.b64encode(file_content).decode()  # some strings <-> bytes conversions necessary here
    button_uuid = st.button("Download File")
    if button_uuid:
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

# Get the content of the selected file
file_content = get_file_content(selected_file)

# Show the download link
get_download_link(selected_file, file_content)
