import streamlit as st
from azure.storage.blob import BlobServiceClient
import os

# Retrieve Azure blob storage connection string from environment variable
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
if not connection_string:
    st.error("Azure Storage connection string is not set in environment variables.")
    st.stop()

container_name = "data1"
blob_name = "comments.txt"

# Create a form with a text area in Streamlit
st.subheader("Instructions")
st.write("Include who the message is from and give detailed comments.")
with st.form(key='Comment'):
    text_input = st.text_area(label='Enter your comment', value='', placeholder='Type here...', max_chars=500)
    submit_button = st.form_submit_button(label='Submit')

    # If the form is submitted, write the comment to a file
    if submit_button:
        with open('comments.txt', 'a') as f:
            f.write(text_input + '\n')

        # Create a blob client using the local file name as the name for the blob
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Upload the created file, overwriting if it already exists
        try:
            with open('comments.txt', 'rb') as data:
                blob_client.upload_blob(data, overwrite=True)
            st.success("Comment uploaded successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Steps to Set Environment Variables
# Windows:
# Open Command Prompt and run:
# setx AZURE_STORAGE_CONNECTION_STRING "your_connection_string_here"
# macOS/Linux:
# Open Terminal and run:
# export AZURE_STORAGE_CONNECTION_STRING="your_connection_string_here"