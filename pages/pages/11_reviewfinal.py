import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient
import pandas as pd
import io

def download_blob_data(container_name, blob_name, connection_string):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    stream = io.BytesIO()
    blob_data = blob_client.download_blob()
    blob_data.readinto(stream)
    return pd.read_csv(stream)

def main():
    st.title("Verify Accuracy")

    # Azure Blob Storage details
    CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"
    CONTAINER_NAME = "data1"
    BLOB_NAME = "out1.csv"

    # Download and parse CSV data
    try:
        df = download_blob_data(CONTAINER_NAME, BLOB_NAME, CONNECTION_STRING)
        data_dict = df.to_dict(orient='records')[0]  # Assuming there's only one record
    except Exception as e:
        st.error(f"Failed to download or parse CSV: {e}")
        return

    with st.form("my_form"):
        # Use columns to place fields side by side and pre-fill with CSV data
        col1, col2 = st.columns(2)
        FirstName = col1.text_input("FirstName", value=data_dict.get("FirstName", ""))
        LastName = col2.text_input("LastName", value=data_dict.get("LastName", ""))
        Address = st.text_input("Address", value=data_dict.get("Address", ""))
        City, State = st.columns(2)
        City = City.text_input("City", value=data_dict.get("City", ""))
        State = State.text_input("State", value=data_dict.get("State", ""))
        Zipcode, Phone = st.columns(2)
        Zipcode = Zipcode.text_input("Zipcode", value=data_dict.get("Zipcode", ""))
        Phone = Phone.text_input("Phone", value=data_dict.get("Phone", ""))
        Allergy1, Allergy2 = st.columns(2)
        Allergy1 = Allergy1.text_input("Allergy1", value=data_dict.get("Allergy1", ""))
        Allergy2 = Allergy2.text_input("Allergy2", value=data_dict.get("Allergy2", ""))

        # Additional fields (example for MedicationName, Month, Year)
        MedicationName, Month, Year = st.columns(3)
        MedicationName = MedicationName.text_input("MEDICATION NAME", value=data_dict.get("MEDICATION NAME", ""))
        Month = Month.text_input("MONTH", value=data_dict.get("MONTH", ""))
        Year = Year.text_input("YEAR", value=data_dict.get("YEAR", ""))

        # Assuming similar approach for other fields...

        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()