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
        FirstName = col1.text_input("FirstName", value=str(row_data.get('FirstName', '')))
        LastName = col2.text_input("LastName", value=str(row_data.get('LastName', '')))
        Address = st.text_input("Address", value=str(row_data.get('Address', '')))
        City, State = st.columns(2)
        City = City.text_input("City", value=str(row_data.get('City', '')))
        State = State.text_input("State", value=str(row_data.get('State', '')))
        ZipCode, Phone = st.columns(2)
        ZipCode = ZipCode.text_input("ZipCode", value=str(row_data.get('ZipCode', '')))
        Phone = Phone.text_input("Phone", value=str(row_data.get('Phone', '')))
        Allergy1, Allergy2 = st.columns(2)
        Allergy1 = Allergy1.text_input("Allergy1", value=str(row_data.get('Allergy1', '')))
        Allergy2 = Allergy2.text_input("Allergy2", value=str(row_data.get('Allergy2', '')))

        # Medication details section
        MedIntakeName, MedIntakeMonth, MedIntakeYear = st.columns(3)
        MedIntakeName = MedIntakeName.text_input("MEDICATION NAME", value=str(row_data.get('MedIntakeName', '')))
        MedIntakeMonth = MedIntakeMonth.text_input("MONTH", value=str(row_data.get('MedIntakeMonth', '')))
        MedIntakeYear = MedIntakeYear.text_input("YEAR", value=str(row_data.get('MedIntakeYear', '')))

        # Treatment Plan table
        Med1Check, Med1Name, Med1Dosage, Med1Frequency, Med1Form, Med1Route, Med1Instructions = st.columns(7)
        Med1Check = Med1Check.text_input("Select [x]1", value=str(row_data.get('Med1Check', '')))
        Med1Name = Med1Name.text_input("Medication1", value=str(row_data.get('Med1Name', '')))
        Med1Dosage = Med1Dosage.text_input("Dosage1", value=str(row_data.get('Med1Dosage', '')))
        Med1Frequency = Med1Frequency.text_input("Frequency1", value=str(row_data.get('Med1Frequency', '')))
        Med1Form = Med1Form.text_input("Form1", value=str(row_data.get('Med1Form', '')))
        Med1Route = Med1Route.text_input("Route1", value=str(row_data.get('Med1Route', '')))
        Med1Instructions = Med1Instructions.text_input("Instructions1", value=str(row_data.get('Med1Instructions', '')))

        Med2Check, Med2Name, Med2Dosage, Med2Frequency, Med2Form, Med2Route, Med2Instructions = st.columns(7)
        Med2Check = Med2Check.text_input("Select [x]2", value=str(row_data.get('Med2Check', '')))
        Med2Name = Med2Name.text_input("Medication2", value=str(row_data.get('Med2Name', '')))
        Med2Dosage = Med2Dosage.text_input("Dosage2", value=str(row_data.get('Med2Dosage', '')))
        Med2Frequency = Med2Frequency.text_input("Frequency2", value=str(row_data.get('Med2Frequency', '')))
        Med2Form = Med2Form.text_input("Form2", value=str(row_data.get('Med2Form', '')))
        Med2Route = Med2Route.text_input("Route2", value=str(row_data.get('Med2Route', '')))
        Med2Instructions = Med2Instructions.text_input("Instructions2", value=str(row_data.get('Med2Instructions', '')))

        Med3Check, Med3Name, Med3Dosage, Med3Frequency, Med3Form, Med3Route, Med3Instructions = st.columns(7)
        Med3Check = Med3Check.text_input("Select [x]3", value=str(row_data.get('Med3Check', '')))
        Med3Name = Med3Name.text_input("Medication3", value=str(row_data.get('Med3Name', '')))
        Med3Dosage = Med3Dosage.text_input("Dosage3", value=str(row_data.get('Med3Dosage', '')))
        Med3Frequency = Med3Frequency.text_input("Frequency3", value=str(row_data.get('Med3Frequency', '')))
        Med3Form = Med3Form.text_input("Form3", value=str(row_data.get('Med3Form', '')))
        Med3Route = Med3Route.text_input("Route3", value=str(row_data.get('Med3Route', '')))
        Med3Instructions = Med3Instructions.text_input("Instructions3", value=str(row_data.get('Med3Instructions', '')))

        Med4Check, Med4Name, Med4Dosage, Med4Frequency, Med4Form, Med4Route, Med4Instructions = st.columns(7)
        Med4Check = Med4Check.text_input("Select [x]4", value=str(row_data.get('Med4Check', '')))
        Med4Name = Med4Name.text_input("Medication4", value=str(row_data.get('Med4Name', '')))
        Med4Dosage = Med4Dosage.text_input("Dosage4", value=str(row_data.get('Med4Dosage', '')))
        Med4Frequency = Med4Frequency.text_input("Frequency4", value=str(row_data.get('Med4Frequency', '')))
        Med4Form = Med4Form.text_input("Form4", value=str(row_data.get('Med4Form', '')))
        Med4Route = Med4Route.text_input("Route4", value=str(row_data.get('Med4Route', '')))
        Med4Instructions = Med4Instructions.text_input("Instructions4", value=str(row_data.get('Med4Instructions', '')))
 
        # Treatment Plan table
        Day1, Day1Yes, Day1No, Day1Dosage, Day1Freq, Day1Form, Day1Route = st.columns(7)
        Day1 = Day1.text_input("Day1", value=str(row_data.get('Day1', '')))
        Day1Yes = Day1Yes.text_input("Yes1", value=str(row_data.get('Day1Yes', '')))
        Day1No = Day1No.text_input("No1", value=str(row_data.get('Day1No', '')))
        Day1Dosage = Day1Dosage.text_input("Dosage1", value=str(row_data.get('Day1Dosage', '')))
        Day1Freq = Day1Freq.text_input("Frequency1", value=str(row_data.get('Day1Freq', '')))
        Day1Form = Day1Form.text_input("Form1", value=str(row_data.get('Day1Form', '')))
        Day1Route = Day1Route.text_input("Route1", value=str(row_data.get('Day1Route', '')))

        Day2, Day2Yes, Day2No, Day2Dosage, Day2Freq, Day2Form, Day2Route = st.columns(7)
        Day2 = Day2.text_input("Day2", value=str(row_data.get('Day2', '')))
        Day2Yes = Day2Yes.text_input("Yes2", value=str(row_data.get('Day2Yes', '')))
        Day2No = Day2No.text_input("No2", value=str(row_data.get('Day2No', '')))
        Day2Dosage = Day2Dosage.text_input("Dosage2", value=str(row_data.get('Day2Dosage', '')))
        Day2Freq = Day2Freq.text_input("Frequency2", value=str(row_data.get('Day2Freq', '')))
        Day2Form = Day2Form.text_input("Form2", value=str(row_data.get('Day2Form', '')))
        Day2Route = Day2Route.text_input("Route2", value=str(row_data.get('Day2Route', '')))

        Day3, Day3Yes, Day3No, Day3Dosage, Day3Freq, Day3Form, Day3Route = st.columns(7)
        Day3 = Day3.text_input("Day3", value=str(row_data.get('Day3', '')))
        Day3Yes = Day3Yes.text_input("Yes3", value=str(row_data.get('Day3Yes', '')))
        Day3No = Day3No.text_input("No3", value=str(row_data.get('Day3No', '')))
        Day3Dosage = Day3Dosage.text_input("Dosage3", value=str(row_data.get('Day3Dosage', '')))
        Day3Freq = Day3Freq.text_input("Frequency3", value=str(row_data.get('Day3Freq', '')))
        Day3Form = Day3Form.text_input("Form3", value=str(row_data.get('Day3Form', '')))
        Day3Route = Day3Route.text_input("Route3", value=str(row_data.get('Day3Route', '')))

        Day4, Day4Yes, Day4No, Day4Dosage, Day4Freq, Day4Form, Day4Route = st.columns(7)
        Day4 = Day4.text_input("Day4", value=str(row_data.get('Day4', '')))
        Day4Yes = Day4Yes.text_input("Yes4", value=str(row_data.get('Day4Yes', '')))
        Day4No = Day4No.text_input("No4", value=str(row_data.get('Day4No', '')))
        Day4Dosage = Day4Dosage.text_input("Dosage4", value=str(row_data.get('Day4Dosage', '')))
        Day4Freq = Day4Freq.text_input("Frequency4", value=str(row_data.get('Day4Freq', '')))
        Day4Form = Day4Form.text_input("Form4", value=str(row_data.get('Day4Form', '')))
        Day4Route = Day4Route.text_input("Route4", value=str(row_data.get('Day4Route', '')))

        Day5, Day5Yes, Day5No, Day5Dosage, Day5Freq, Day5Form, Day5Route = st.columns(7)
        Day5 = Day5.text_input("Day5", value=str(row_data.get('Day5', '')))
        Day5Yes = Day5Yes.text_input("Yes5", value=str(row_data.get('Day5Yes', '')))
        Day5No = Day5No.text_input("No5", value=str(row_data.get('Day5No', '')))
        Day5Dosage = Day5Dosage.text_input("Dosage5", value=str(row_data.get('Day5Dosage', '')))
        Day5Freq = Day5Freq.text_input("Frequency5", value=str(row_data.get('Day5Freq', '')))
        Day5Form = Day5Form.text_input("Form5", value=str(row_data.get('Day5Form', '')))
        Day5Route = Day5Route.text_input("Route5", value=str(row_data.get('Day5Route', '')))

        Day6, Day6Yes, Day6No, Day6Dosage, Day6Freq, Day6Form, Day6Route = st.columns(7)
        Day6 = Day6.text_input("Day6", value=str(row_data.get('Day6', '')))
        Day6Yes = Day6Yes.text_input("Yes6", value=str(row_data.get('Day6Yes', '')))
        Day6No = Day6No.text_input("No6", value=str(row_data.get('Day6No', '')))
        Day6Dosage = Day6Dosage.text_input("Dosage6", value=str(row_data.get('Day6Dosage', '')))
        Day6Freq = Day6Freq.text_input("Frequency6", value=str(row_data.get('Day6Freq', '')))
        Day6Form = Day6Form.text_input("Form6", value=str(row_data.get('Day6Form', '')))
        Day6Route = Day6Route.text_input("Route6", value=str(row_data.get('Day6Route', '')))

        Day7, Day7Yes, Day7No, Day7Dosage, Day7Freq, Day7Form, Day7Route = st.columns(7)
        Day7 = Day7.text_input("Day7", value=str(row_data.get('Day7', '')))
        Day7Yes = Day7Yes.text_input("Yes7", value=str(row_data.get('Day7Yes', '')))
        Day7No = Day7No.text_input("No7", value=str(row_data.get('Day7No', '')))
        Day7Dosage = Day7Dosage.text_input("Dosage7", value=str(row_data.get('Day7Dosage', '')))
        Day7Freq = Day7Freq.text_input("Frequency7", value=str(row_data.get('Day7Freq', '')))
        Day7Form = Day7Form.text_input("Form7", value=str(row_data.get('Day7Form', '')))
        Day7Route = Day7Route.text_input("Route7", value=str(row_data.get('Day7Route', '')))

        Day8, Day8Yes, Day8No, Day8Dosage, Day8Freq, Day8Form, Day8Route = st.columns(8)
        Day8 = Day8.text_input("Day8", value=str(row_data.get('Day8', '')))
        Day8Yes = Day8Yes.text_input("Yes8", value=str(row_data.get('Day8Yes', '')))
        Day8No = Day8No.text_input("No8", value=str(row_data.get('Day8No', '')))
        Day8Dosage = Day8Dosage.text_input("Dosage8", value=str(row_data.get('Day8Dosage', '')))
        Day8Freq = Day8Freq.text_input("Frequency8", value=str(row_data.get('Day8Freq', '')))
        Day8Form = Day8Form.text_input("Form8", value=str(row_data.get('Day8Form', '')))
        Day8Route = Day8Route.text_input("Route8", value=str(row_data.get('Day8Route', '')))

        Day9, Day9Yes, Day9No, Day9Dosage, Day9Freq, Day9Form, Day9Route = st.columns(9)
        Day9 = Day9.text_input("Day9", value=str(row_data.get('Day9', '')))
        Day9Yes = Day9Yes.text_input("Yes9", value=str(row_data.get('Day9Yes', '')))
        Day9No = Day9No.text_input("No9", value=str(row_data.get('Day9No', '')))
        Day9Dosage = Day9Dosage.text_input("Dosage9", value=str(row_data.get('Day9Dosage', '')))
        Day9Freq = Day9Freq.text_input("Frequency9", value=str(row_data.get('Day9Freq', '')))
        Day9Form = Day9Form.text_input("Form9", value=str(row_data.get('Day9Form', '')))
        Day9Route = Day9Route.text_input("Route9", value=str(row_data.get('Day9Route', '')))

        Day10, Day10Yes, Day10No, Day10Dosage, Day10Freq, Day10Form, Day10Route = st.columns(10)
        Day10 = Day10.text_input("Day10", value=str(row_data.get('Day10', '')))
        Day10Yes = Day10Yes.text_input("Yes10", value=str(row_data.get('Day10Yes', '')))
        Day10No = Day10No.text_input("No10", value=str(row_data.get('Day10No', '')))
        Day10Dosage = Day10Dosage.text_input("Dosage10", value=str(row_data.get('Day10Dosage', '')))
        Day10Freq = Day10Freq.text_input("Frequency10", value=str(row_data.get('Day10Freq', '')))
        Day10Form = Day10Form.text_input("Form10", value=str(row_data.get('Day10Form', '')))
        Day10Route = Day10Route.text_input("Route10", value=str(row_data.get('Day10Route', '')))

        # Medication details section
        OTPName, OTPClinician, OTPphone= st.columns(3)
        OTPName = OTPName.text_input("OTPName", value=str(row_data.get('OTPName', '')))
        OTPClinician=OTPClinician.text_input("OTPClinician", value=str(row_data.get('OTPClinician', '')))
        OTPphone = OTPphone.text_input("OTPphone", value=str(row_data.get('OTPphone', '')))
        OTPAddress= st.text_input("OTPAddress", value=str(row_data.get('OTPAddress', '')))

        PharmacyName, PharmacyPhone = st.columns(2)
        PharmacyName=PharmacyName.text_input("PharmacyName", value=str(row_data.get('PharmacyName', '')))
        PharmacyPhone=PharmacyPhone.text_input("PharmacyPhone", value=str(row_data.get('PharmacyPhone', '')))


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
