import os
import streamlit as st
import smtplib
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def send_email(user_message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.getenv("stephenmodimakwane@gmail.com"), os.getenv("Gmail_2023"))
    message = 'Subject: {}\n\n{}'.format("Webpage Message", user_message)
    server.sendmail(os.getenv("EMAIL"), os.getenv("EMAIL"), message)
    server.quit()

def append_blob(blob_service_client, container_name, blob_name, content):
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)
    
    # Download the blob to a stream
    data = blob_client.download_blob().readall()
    
    # Decode the blob data
    decoded_data = data.decode('utf-8')
    
    # Append new content
    updated_data = decoded_data + content + '\n'
    
    # Upload the updated blob
    blob_client.upload_blob(updated_data, overwrite=True)

def main():
    connection_string = os.getenv("DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net")
    container_name = os.getenv("data1")
    blob_name = "comment.csv"
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    st.title('Contact Form')
    user_input = st.text_area("Please enter your comment: ")
    
    if st.button("Send Message"):
        append_blob(blob_service_client, container_name, blob_name, user_input)
        send_email(user_input)
        st.success("Message sent successfully!")

if __name__ == "__main__":
    main()
