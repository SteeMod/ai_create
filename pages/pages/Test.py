import streamlit as st
from azure.storage.blob import BlobServiceClient

# Retrieve secrets from the secrets.toml file
connection_string = st.secrets["DEFAULT"]["connection_string"]
container_name = st.secrets["DEFAULT"]["azure_container_name"]
blob_name = "comments.txt"

# Create a form with a text input in Streamlit
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your comment')
    submit_button = st.form_submit_button(label='Submit')import streamlit as st
from azure.storage.blob import BlobServiceClient

# Hardcoded connection string and container name
connection_string = "your_connection_string_here"
container_name = "your_container_name_here"
blob_name = "comments.txt"

# Create a form with a text input in Streamlit
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your comment')
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