import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Create a form with a text input in Streamlit
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your comment')
    submit_button = st.form_submit_button(label='Submit')

    # If the form is submitted, write the comment to a file
    if submit_button:
        with open('comments.txt', 'a') as f:
            f.write(text_input + '\n')

        # Create a blob client using the local file name as the name for the blob
        blob_service_client = BlobServiceClient.from_connection_string('your_connection_string')
        blob_client = blob_service_client.get_blob_client('your_container_name', 'your_blob_name')

        # Upload the created file
        with open('comments.txt', 'rb') as data:
            blob_client.upload_blob(data)
