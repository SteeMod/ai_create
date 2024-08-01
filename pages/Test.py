import streamlit as st
from azure.storage.blob import BlobServiceClient
import io
import base64

st.title("Download Medication Intake Tracker Form")

# Azure blob storage details
connection_string = "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"
container_name = "data1"

try:
    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

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
        try:
            blob_client = blob_service_client.get_blob_client(container_name, file_name)
            download_stream = blob_client.download_blob().readall()

            # Create a BytesIO object
            pdf_data = io.BytesIO(download_stream)

            return pdf_data
        except Exception as e:
            st.error(f"Error retrieving file content: {e}")
            return None

    # Get the content of the selected file
    if selected_file:
        file_content = get_file_content(selected_file)

        if file_content:
            # Debugging: Check the size of the file content
            st.write(f"File size: {len(file_content.getvalue())} bytes")

            # Convert the BytesIO object to base64 encoded string
            b64 = base64.b64encode(file_content.getvalue()).decode()

            # Debugging: Check the first 100 characters of the base64 string
            st.write(f"Base64 string (first 100 chars): {b64[:100]}")

            # Display the selected file content
            st.text("Displaying the selected file:")
            st.markdown(f'<iframe src="data:application/pdf;base64,{b64}" width="700" height="800" type="application/pdf"></iframe>', unsafe_allow_html=True)
        else:
            st.error("Failed to retrieve the file content.")
except Exception as e:
    st.error(f"An error occurred: {e}")