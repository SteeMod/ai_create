import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
from azure.storage.blob import BlobServiceClient

st.title("Medication Intake Dashboard")

try:
    blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net')
    container_client = blob_service_client.get_container_client('data1')

    # List all blobs in the virtual folder 'ReviewedFiles'
    blob_list = container_client.list_blobs(name_starts_with='ReviewedFiles/')

    # Find the latest blob
    latest_blob = max(blob_list, key=lambda blob: blob.last_modified)

    # Download the latest blob as a pandas DataFrame
    blob_client = blob_service_client.get_blob_client('data1', latest_blob.name)
    df = pd.read_csv(BytesIO(blob_client.download_blob().readall()))

    # Select only columns with names containing 'Day' 'Yes' or 'Day' 'yes'
    df = df[[col for col in df.columns if 'Day' in col and ('Yes' in col or 'yes' in col)]]

    # Transpose the DataFrame
    df = df.transpose()

    # Sort the DataFrame by column names
    df = df.sort_index(axis=1)

    # Rename the first column to 'Yes'
    df.rename(columns={df.columns[0]: 'Yes'}, inplace=True)

    # Count the rows where 'Yes' is ':selected:'
    numerator = df[df['Yes'] == ':selected:'].shape[0]

    # Get the total row count
    denominator = df.shape[0]

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie([numerator, denominator - numerator], labels=['Selected', 'Not Selected'], autopct='%1.1f%%')
    ax.set_title('Your Statistics')

    # Create two columns
    col1, col2 = st.columns(2)

    # Display the DataFrame in the first column and the pie chart in the second column
    with col1:
        st.dataframe(df)
    with col2:
        st.pyplot(fig)

except Exception as ex:
    print(f'Exception: {ex}')
