import streamlit as st
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from io import StringIO

# Function to download CSV data from Azure Blob Storage
def download_csv_data_from_blob(container_name, blob_name, connection_string):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_data = blob_client.download_blob()
    return pd.read_csv(StringIO(blob_data.content_as_text()))

# Display the DataFrame in a table format
def display_data_table(df):
    if df.empty:
        st.write("No data found in CSV")
    else:
        st.table(df)  # You can use st.dataframe(df) for a slightly different style

# Main function to control the app
def main():
    st.title("CSV to Web Form")
    # Button to load the CSV file from Azure Blob Storage
    if st.button('Review'):
        # Azure Blob Storage details
        container_name = 'data1'
        blob_name = 'out1.csv'
        # Replace 'your_connection_string' with your actual Azure Blob Storage connection string
        connection_string = 'DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net'
        df = download_csv_data_from_blob(container_name, blob_name, connection_string)
        display_data_table(df)

if __name__ == "__main__":
    main()