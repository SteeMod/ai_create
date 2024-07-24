import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Replace with your Azure Blob Storage details
connection_string = "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"
container_name = "data1"
blob_name = "out2.csv"

# Create a blob client using the local file name as the name for the blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container_name, blob_name)

# Download the blob to a local file
with open("temp.csv", "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())

# Load the data into a pandas DataFrame
df = pd.read_csv("temp.csv")

# Convert the data type to float and replace selected columns with number 1
df = df.astype(float).replace(selected_columns, 1)

# Get the column names
columns = df.columns.tolist()

# Filter the column names based on the pattern 'Day#Yes'
day_columns = [col for col in columns if 'Day' in col and 'Yes' in col]

# Let the user select columns
selected_columns = st.multiselect("Select the columns you're interested in", day_columns)

# Filter the DataFrame based on the selected columns
filtered_df = df[selected_columns]

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(filtered_df.sum(), labels=selected_columns, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
st.pyplot(fig)
