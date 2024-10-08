


import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
import io

def show_image():
    try:
        blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net")
        blob_client = blob_service_client.get_blob_client("data1", "photo.png")

        blob_data = blob_client.download_blob().readall()
        image_data = Image.open(io.BytesIO(blob_data))

        return image_data

    except Exception as ex:
        print('Exception:')
        print(ex)

# Create two columns
col1, col2 = st.columns(2)

# Use the first column for text
col1.title("About[Me]")
col1.write(
    "Stephen Modimakwane is a  Management Information Systems Specialist with over 18 years of experience in the field. His expertise include Data Analytics, Data Visualization, AI Infusion and Strategy Execution. He has a passion for creating technology solutions that help organizations and communities.Email:stephenmodimakwane@gmail.com"
)

# Use the second column for the image
image = show_image()
col2.image(image, caption='Stephen Modimakwane', width=200)  # Adjust width as needed





