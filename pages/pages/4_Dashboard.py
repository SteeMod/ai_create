import streamlit as st
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import matplotlib.pyplot as plt
import re
from datetime import datetime

# Azure blob storage details
connection_string = "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"
container_name = "data1"

# Create blob service client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get blob client
container_client = blob_service_client.get_container_client(container_name)

# Get the latest blob based on the timestamp in the filename
blobs_list = container_client.list_blobs(name_starts_with="data1/ReviewedFiles/reviewed_")
blobs_list = sorted(blobs_list, key=lambda x: datetime.strptime(re.search(r'reviewed_(.*).csv', x.name).group(1), '%Y%m%d%H%M%S'), reverse=True)
blob_name = blobs_list[0].name

blob_client = blob_service_client.get_blob_client(container_name, blob_name)

# Download the blob to a stream
stream = io.BytesIO()
downloader = blob_client.download_blob()
downloader.readinto(stream)

# Convert the stream to a pandas dataframe
stream.seek(0)
df = pd.read_csv(stream)

# Convert the range of columns from Day1Yes to Day31Yes to a single column with 31 rows
df = df.melt(id_vars=[col for col in df.columns if not col.startswith('Day')], 
             value_vars=[f'Day{i}Yes' for i in range(1, 32)], 
             var_name='Day', 
             value_name='Yes')

# Calculate percentage where selected over total
df['Percentage'] = df['Yes'].apply(lambda x: x / df['Yes'].sum() * 100)

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(df['Percentage'], labels=df['Day'], autopct='%1.1f%%')
plt.title('Percentage of Yes by Day')

# Display the pie chart in Streamlit
st.pyplot(fig)
