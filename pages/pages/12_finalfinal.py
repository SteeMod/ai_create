import streamlit as st
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from io import StringIO

# Function to download CSV data from Azure Blob Storage
def download_csv_data_from_blob(container_name, blob_name, connection_string):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_data = blob_client.download_blob()
    return pd.read_csv(StringIO(blob_data.content_as_text()))

# Generate and pre-populate the form based on the CSV data
def generate_form(df, row_index=0):
    if df.empty or row_index >= len(df):
        st.write("No data found in CSV or index out of range")
        return
    row_data = df.iloc[row_index]
    with st.form("my_form"):
        # Use columns to place fields side by side
        col1, col2 = st.columns(2)
        FirstName = col1.text_input("FirstName", value=str(row_data['FirstName']))
        LastName = col2.text_input("LastName", value=str(row_data['LastName']))
        Address = st.text_input("Address", value=str(row_data['Address']))
        City, State = st.columns(2)
        City = City.text_input("City", value=str(row_data['City']))
        State = State.text_input("State", value=str(row_data['State']))
        ZipCode, Phone = st.columns(2)
        ZipCode = ZipCode.text_input("ZipCode", value=str(row_data['ZipCode']))
        Phone = Phone.text_input("Phone", value=str(row_data['Phone']))
        Allergy1, Allergy2 = st.columns(2)
        Allergy1 = Allergy1.text_input("Allergy1", value=str(row_data['Allergy1']))
        Allergy2 = Allergy2.text_input("Allergy2", value=str(row_data['Allergy2']))

        # Medication details section
        MedIntakeName, MedIntakeMonth, MedIntakeYear = st.columns(3)
        MedIntakeName = MedIntakeName.text_input("MEDICATION NAME", value=str(row_data['MedIntakeName']))
        MedIntakeMonth = MedIntakeMonth.text_input("MONTH", value=str(row_data['MedIntakeMonth']))
        MedIntakeYear = MedIntakeYear.text_input("YEAR", value=str(row_data['MedIntakeYear']))

        # Medication table
        Med1Check, Med1Name, Med1Dosage, Med1Frequency, Med1Form, Med1Route, Med1Instructions = st.columns(7)
        Med1Check = Med1Check.text_input("Select [mark x]", value=str(row_data['Med1Check']))
        Med1Name = Med1Name.text_input("Medication", value=str(row_data['Med1Name']))
        Med1Dosage = Med1Dosage.text_input("Dosage", value=str(row_data['Med1Dosage']))
        Med1Frequency = Med1Frequency.text_input("Frequency", value=str(row_data['Med1Frequency']))
        Med1Form = Med1Form.text_input("Form", value=str(row_data['Med1Form']))
        Med1Route = Med1Route.text_input("Route", value=str(row_data['Med1Route']))
        Med1Instructions = Med1Instructions.text_input("Instructions", value=str(row_data['Med1Instructions']))


        num_rows_medication = 4
        num_columns_medication = 7
        column_names_medication = ["Mark X", "Medication", "Dosage", "Frequency", "Form", "Route", "Instructions"]
        header_cols_medication = st.columns(num_columns_medication)
        for col, col_name in zip(header_cols_medication, column_names_medication):
            col.write(col_name)
        for row in range(num_rows_medication):
            cols = st.columns(num_columns_medication)
            for i, col in enumerate(cols):
                col.text_input(column_names_medication[i], key=f"{column_names_medication[i]}_{row}")

        # Medication intake progress section
        num_rows_progress = 31
        num_columns_progress = 7
        column_names_progress = ["Date", "Yes", "No", "Dosage", "Frequency", "Form", "Route"]
        header_cols_progress = st.columns(num_columns_progress)
        for col, col_name in zip(header_cols_progress, column_names_progress):
            col.write(col_name)
        for row in range(num_rows_progress):
            cols = st.columns(num_columns_progress)
            for i, col in enumerate(cols):
                col.text_input(column_names_progress[i], key=f"{column_names_progress[i]}_{row}_progress")

        # Medication details section
        OTPName, OTPClinician, OTPphone= st.columns(3)
        OTPName = OTPName.text_input("OTPName", value=str(row_data['OTPName']))
        OTPClinician=OTPClinician.text_input("OTPClinician", value=str(row_data['OTPClinician']))
        OTPphone = OTPphone.text_input("OTPphone", value=str(row_data['OTPphone']))
        OTPAddress= st.text_input("OTPAdress", value=str(row_data['OTPAddress']))

        PharmacyName, PharmacyPhone = st.columns(2)
        PharmacyName=PharmacyName.text_input("PharmacyName", value=str(row_data['PharmacyName']))
        PharmacyPhone=PharmacyPhone.text_input("PharmacyPhone", value=str(row_data['PharmacyPhone']))

# Main function to control the app
def main():
    st.title("Verify Accuracy")
    # Button to load the CSV file from Azure Blob Storage
    if st.button('Review'):
        # Azure Blob Storage details
        container_name = 'data1'
        blob_name = 'out1.csv'
        # Ensure you replace 'your_connection_string' with your actual Azure Blob Storage connection string
        connection_string = 'DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net'
        df = download_csv_data_from_blob(container_name, blob_name, connection_string)
        generate_form(df)

if __name__ == "__main__":
    main()
