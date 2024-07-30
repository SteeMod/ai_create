import streamlit as st
import streamlit as st
from PIL import Image
import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
import io
st.title("About[Me]")
st.write(
    "Stephen Modimakwane is a  Management Information Systems Specialist with over 18 years of experience in the field. I focus on Data Analytics, Data Visualization, and AI Infusion. I have a passion for creating data-driven solutions that help organizations."
)



def show_image():
    try:
        blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net")
        blob_client = blob_service_client.get_blob_client("data1", "photo.png")

        blob_data = blob_client.download_blob().readall()
        image_data = Image.open(io.BytesIO(blob_data))

        st.image(image_data, caption='Your Image Caption', use_column_width=True)

    except Exception as ex:
        print('Exception:')
        print(ex)

show_image()

