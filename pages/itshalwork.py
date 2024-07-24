import pandas as pd
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

# Load the stream into a DataFrame
df = pd.read_csv(stream)

# Select columns from 'Day1Yes' to 'Day31Yes'
selected_columns = df.loc[:, 'Day1Yes':'Day31Yes']

# Count 'Yes' entries for each day
yes_counts = selected_columns.apply(lambda x: (x == 'Yes').sum())

# Create a pie chart
plt.figure(figsize=(10, 6))
plt.pie(yes_counts, labels=yes_counts.index, autopct='%1.1f%%')
plt.title('Distribution of "Yes" Entries from Day1 to Day31')
plt.show()
