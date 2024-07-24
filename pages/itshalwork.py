import streamlit as st
import pandas as pd
from azure.storage.blob import BlobServiceClient
import io

# Azure Blob Storage credentials
connection_string = 'DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net'
container_name = 'data1'
blob_name = 'out1.csv'

# Create a blob client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container_name, blob_name)

# Download the blob data into a stream
stream = io.BytesIO()
stream.write(blob_client.download_blob().readall())
stream.seek(0)

# Load the stream into a DataFrame
df = pd.read_csv(stream)

# Transpose the DataFrame
df_transposed = df.transpose()

# Display the transposed DataFrame using Streamlit
st.title('Transposed CSV Data')
st.dataframe(df_transposed)