import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def append_blob(blob_service_client, container_name, blob_name, content):
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)
    
    # Download the blob to a stream
    data = blob_client.download_blob().readall()
    
    # Decode the blob data
    decoded_data = data.decode('utf-8')
    
    # Append new content
    updated_data = decoded_data + content + '\n'
    
    # Upload the updated blob
    blob_client.upload_blob(updated_data, overwrite=True)

def main():
    # Access secrets from st.secrets
    connection_string = st.secrets["DEFAULT"]["connection_string"]
    container_name = st.secrets["DEFAULT"]["azure_container_name"]

    blob_name = "comment.csv"
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    st.title('Contact Form')
    user_input = st.text_area("Please enter your comment: ")
    
    if st.button("Send Message"):
        append_blob(blob_service_client, container_name, blob_name, user_input)
        st.success("Message sent successfully!")

if __name__ == "__main__":
    main()
