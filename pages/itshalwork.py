import pandas as pd
import matplotlib.pyplot as plt
import io
from azure.storage.blob import BlobServiceClient

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

# Load the stream into a DataFrame and transpose it
df = pd.read_csv(stream).T

# Rename the columns
df.columns = ['Day', 'Yes']

# Filter rows from 'Day1' to 'Day31'
df = df.loc['Day1':'Day31']

# Count 'Yes' entries
yes_count = (df['Yes'] == 'Yes').sum()

# Create a pie chart
plt.figure(figsize=(10, 6))
plt.pie([yes_count, len(df) - yes_count], labels=['Yes', 'No'], autopct='%1.1f%%')
plt.title('Percentage of "Yes" Entries from Day1 to Day31')
plt.show()
