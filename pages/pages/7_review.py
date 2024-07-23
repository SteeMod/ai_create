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

# Generate and pre-populate the form based on the CSV data
def generate_form(df, row_index=0):
    if df.empty or row_index >= len(df):
        st.write("No data found in CSV or index out of range")
        return
    row_data = df.iloc[row_index]
    form = st.form(key='csv_form')
    fields = {}
    for column in df.columns:
        fields[column] = form.text_input(column, value=str(row_data[column]))
    submit_button = form.form_submit_button(label='Submit')
    if submit_button:
        st.write("Form submitted")
        # Here you can handle the form submission (e.g., save the edited data)
        # For demonstration, we'll just display the submitted values
        for column, value in fields.items():
            st.write(f"{column}: {value}")

# Main function to control the app
def main():
    st.title("CSV to Web Form")
    # Button to load the CSV file from Azure Blob Storage
    if st.button('Review'):
        # Azure Blob Storage details
        container_name = 'data1'
        blob_name = 'out1.csv'
        # Ensure you replace 'your_connection_string' with your actual Azure Blob Storage connection string
        connection_string = 'DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=7RH6SmoiZzhCTgoxeqBj3GkStL1CCZssv1bjUjSLuU+xhVJy4P2QRCHgwrFGshxyFBeqkULxEGGc+AStNDYvOA==;EndpointSuffix=core.windows.net'
        df = download_csv_data_from_blob(container_name, blob_name, connection_string)
        generate_form(df)

if __name__ == "__main__":
    main()