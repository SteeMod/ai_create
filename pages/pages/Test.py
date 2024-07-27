import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt
from azure.storage.blob import ContainerClient

# Provide your Azure Blob Storage connection string and container name
your_connection_string = 'DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net'
your_container_name = 'data1'

# Connect to the container
container = ContainerClient.from_connection_string(conn_str=your_connection_string, container_name=your_container_name)

# Get the name of the latest blob
latest_blob_name = sorted([(blob.name, blob.last_modified) for blob in container.list_blobs()], key=lambda x: x[1])[-1][0]

# Read the latest CSV file from Azure Blob Storage
df = pd.read_csv(f'azure://{your_container_name}/{latest_blob_name}')

# Select only columns with names containing 'Day' 'Yes' or 'Day' 'yes'
df = df[[col for col in df.columns if 'Day' in col and ('Yes' in col or 'yes' in col)]]

# Transpose the DataFrame
df = df.transpose()

# Sort the DataFrame by column names
df = df.sort_index(axis=1)

# Rename the first column to 'Yes'
df.rename(columns={df.columns[0]: 'Yes'}, inplace=True)

# Display the DataFrame
st.dataframe(df)

# Count the rows where 'Yes' is ':selected:'
numerator = df[df['Yes'] == ':selected:'].shape[0]

# Get the total row count
denominator = df.shape[0]

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie([numerator, denominator - numerator], labels=['Selected', 'Not Selected'], autopct='%1.1f%%')
plt.title('Pie Chart of Selected vs Not Selected')
st.pyplot(plt.gcf())







































#Praise the lord