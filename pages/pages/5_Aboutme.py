import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
import io
import os

def show_image():
    try:
        # Retrieve Azure blob storage connection string from environment variable
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        if not connection_string:
            st.error("Azure Storage connection string is not set in environment variables.")
            st.stop()

        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client("data1", "photo.png")

        blob_data = blob_client.download_blob().readall()
        image_data = Image.open(io.BytesIO(blob_data))

        return image_data

    except Exception as ex:
        st.error(f'Exception: {ex}')
        return None

# Create two columns
col1, col2 = st.columns(2)

# Use the first column for text
col1.title("About[Me]")
col1.write(
    "Stephen Modimakwane is a Management Information Systems Specialist with over 18 years of experience in the field. I focus on Data Analytics, Data Visualization, and AI Infusion. I have a passion for creating data-driven solutions that help organizations."
)

# Use the second column for the image
image = show_image()
if image:
    col2.image(image, caption='Stephen Modimakwane', width=200)  # Adjust width as needed

st.subheader("Skills & Education")

# Steps to Set Environment Variables
# Windows:
# Open Command Prompt and run:
# setx AZURE_STORAGE_CONNECTION_STRING "your_connection_string_here"
# macOS/Linux:
# Open Terminal and run:
# export AZURE_STORAGE_CONNECTION_STRING="your_connection_string_here"
#PRAISEEEEEEE THE LORD