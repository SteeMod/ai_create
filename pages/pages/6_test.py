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

try:
    # Create blob service client
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get blob client
    container_client = blob_service_client.get_container_client(container_name)

    # Get the latest blob based on the timestamp in the filename
    blobs_list = container_client.list_blobs(name_starts_with="ReviewedFiles/review_")
    blobs_list = sorted(blobs_list, key=lambda x: datetime.strptime(re.search(r'review_(.*).csv', x.name).group(1), '%Y%m%d%H%M%S'), reverse=True)
    blob_name = blobs_list[0].name

    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    # Download the blob to a stream
    stream = io.BytesIO()
    downloader = blob_client.download_blob()
    downloader.readinto(stream)


    # Convert the stream to a pandas dataframe
    stream.seek(0)
    df = pd.read_csv(stream)

    # Display the range of columns from Day1Yes to Day31Yes in Streamlit
    st.write(df.loc[:, 'Day1Yes':'Day31Yes'])
    

    # Convert range of columns from Day1Yes to Day31Yes to single column 'Yes'
    df['Yes'] = df.loc[:, 'Day1Yes':'Day31Yes'].sum(axis=1)

    # Create pie chart
    yes_count = df['Yes'].sum()
    total_count = df.shape[0]
    labels = ['Yes', 'No']
    sizes = [yes_count, total_count - yes_count]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    # Display the dataframe in Streamlit
    st.write(df)

except Exception as e:
    st.write("An error occurred:", str(e))
