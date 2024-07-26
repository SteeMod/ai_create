from azure.storage.blob import BlobServiceClient
import csv
import os
import streamlit as st
import pandas as pd

# Function to upload CSV data to Azure Blob Storage
def upload_csv_data_to_blob(df, container_name, blob_name, connection_string):
    try:
        # Create a BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        # Save DataFrame to CSV
        df.to_csv('temp.csv', index=False)
        
        # Upload the created file
        with open('temp.csv', 'rb') as data:
            blob_client.upload_blob(data, overwrite=True)
        
        # Delete the temporary file
        os.remove('temp.csv')
    except Exception as e:
        st.error(f"Error uploading CSV to blob: {e}")

# Function to download the latest CSV data from Azure Blob Storage
def download_latest_csv_from_blob(container_name, connection_string):
    try:
        # Create a BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        
        # Get the list of all blobs in the container
        blob_list = container_client.list_blobs()
        
        # Find the latest blob based on the name (assuming the name includes a timestamp or some identifier that increases with each new file)
        latest_blob_name = max(blob.name for blob in blob_list)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=latest_blob_name)
        
        # Download the blob to a CSV
        with open('latest.csv', 'wb') as csv_file:
            csv_file.write(blob_client.download_blob().readall())
        
        # Load the CSV data into a DataFrame
        df = pd.read_csv('latest.csv', error_bad_lines=False)
        
        return df
    except Exception as e:
        st.error(f"Error downloading CSV from blob: {e}")
        return pd.DataFrame()

# Generate and pre-populate the form based on the CSV data
def generate_form(df, row_index=0):
    if df.empty or row_index >= len(df):
        st.write("No data found in CSV or index out of range")
        return
    row_data = df.iloc[row_index]
    with st.form("Review"):
        
        col1, col2 = st.columns(2)
        FirstName = col1.text_input("FirstName", value=str(row_data.get('FirstName', '')))
        LastName = col2.text_input("LastName", value=str(row_data.get('LastName', '')))
        Address = st.text_input("Address", value=str(row_data.get('Address', '')))
        City, State = st.columns(2)
        City = City.text_input("City", value=str(row_data.get('City', '')))
        State = State.text_input("State", value=str(row_data.get('State', '')))
        ZipCode, Phone = st.columns(2)
        ZipCode = ZipCode.text_input("ZipCode", value=str(row_data.get('ZipCode', '')))
        Phone = Phone.text_input("Phone", value=str(row_data.get('Phone', '')))
        Allergy1, Allergy2 = st.columns(2)
        Allergy1 = Allergy1.text_input("Allergy1", value=str(row_data.get('Allergy1', '')))
        Allergy2 = Allergy2.text_input("Allergy2", value=str(row_data.get('Allergy2', '')))

        # When the form is submitted, save the data to a new DataFrame and upload it to Blob Storage
        submitted = st.form_submit_button("Submit")
        if submitted:
            new_data = {
                'FirstName': FirstName,
                'LastName': LastName,
                'Address': Address,
                'City': City,
                'State': State,
                'ZipCode': ZipCode,
                'Phone': Phone,
                'Allergy1': Allergy1,
                'Allergy2': Allergy2
            }
            new_df = pd.DataFrame([new_data])
            upload_csv_data_to_blob(new_df, 'data1/ReviewedFiles', 'ANODABOSS.csv', 'DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net')

# Example usage
def main():
    st.title("Submit Form Data to Azure Blob Storage")
    # Load your CSV data into a DataFrame
    df = download_latest_csv_from_blob('data1', 'DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net')
    generate_form(df)

if __name__ == "__main__":
    main()