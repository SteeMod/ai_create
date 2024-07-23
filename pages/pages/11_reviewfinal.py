import streamlit as st
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

def download_blob_data(container_name, blob_name, connection_string):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        stream = io.BytesIO()
        blob_data = blob_client.download_blob()
        blob_data.readinto(stream)
        stream.seek(0)  # Reset stream position to the beginning
        return pd.read_csv(stream)
    except Exception as e:
        st.error(f"Failed to download or parse CSV: {e}")
        return None

def main():
    st.title("Verify Accuracy")

    # Azure Blob Storage details
    CONNECTION_STRING = "Your_Azure_Storage_Connection_String"
    CONTAINER_NAME = "Your_Container_Name"
    BLOB_NAME = "out1.csv"
    
    # Download and parse CSV data
    data_dict = download_blob_data(CONTAINER_NAME, BLOB_NAME, CONNECTION_STRING)
    if data_dict is None:
        st.stop()

    data_dict = data_dict.to_dict(orient='records')[0]  # Assuming there's only one record

    with st.form("my_form"):
        # Use columns to place fields side by side and pre-fill with CSV data
        col1, col2 = st.columns(2)
        FirstName = col1.text_input("FirstName", value=data_dict.get("FirstName", ""))
        LastName = col2.text_input("LastName", value=data_dict.get("LastName", ""))
        # Repeat for other fields as before

        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()