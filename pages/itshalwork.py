import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

# Rename columns for easier access
df_transposed.columns = df_transposed.iloc[0]
df_transposed = df_transposed[1:]

# Calculate the total number of 'Yes' entries
yes_counts = df_transposed.apply(lambda x: (x == 'Yes').sum())

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(yes_counts, labels=yes_counts.index, autopct='%1.1f%%')
ax.set_title('Distribution of "Yes" Entries from Day1 to Day31')

# Display the pie chart using Streamlit
st.title('Transposed CSV Data and Pie Chart')
st.dataframe(df_transposed)
st.pyplot(fig)