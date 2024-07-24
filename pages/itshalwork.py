import streamlit as st
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Replace with your Azure Blob Storage details
connection_string = "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"
container_name = "data1"
blob_name = "out1.csv"

# Create a blob client using the local file name as the name for the blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container_name, blob_name)

# Download the blob to a local file
with open("temp.csv", "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())

# Load the data into a pandas DataFrame
df = pd.read_csv("temp.csv")

# Get the column names
columns = df.columns.tolist()

# Let the user select a column to pivot on
pivot_column = st.selectbox("Select a column to pivot on", columns)

# Pivot the DataFrame
pivot_df = df.pivot(columns=pivot_column)

# Let the user select a range of rows to display
row_range = st.slider("Select a range of rows", 0, len(pivot_df), (0, len(pivot_df)))

# Filter the DataFrame by the selected range of rows
filtered_df = pivot_df.iloc[row_range[0]:row_range[1]]

# Display the filtered DataFrame
st.dataframe(filtered_df)
