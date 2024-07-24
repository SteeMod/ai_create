import streamlit as st
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from io import StringIO
import streamlit as st
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
import os
from csv import DictWriter
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    try:
        endpoint = os.getenv('FORM_RECOGNIZER_ENDPOINT', "https://new2two.cognitiveservices.azure.com/")
        credential = AzureKeyCredential(os.getenv('FORM_RECOGNIZER_API_KEY', "027ad9245a594c5886cf5d90abecb9d1"))
        client = DocumentAnalysisClient(endpoint, credential)

        model_id = os.getenv('FORM_RECOGNIZER_CUSTOM_MODEL_ID', "Thessa5vs6")

        # Create BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(os.getenv('AZURE_STORAGE_CONNECTION_STRING', "DefaultEndpointsProtocol=https;AccountName=devcareall;AccountKey=GEW0V0frElMx6YmZyObMDqJWDj3pG0FzJCTkCaknW/JMH9UqHqNzeFhF/WWCUKeIj3LNN5pb/hl9+AStHMGKFA==;EndpointSuffix=core.windows.net"))
        container_client = blob_service_client.get_container_client(os.getenv('BLOB_CONTAINER_NAME', "data1"))

        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        original_blob_name = os.getenv('BLOB_NAME', "test4.pdf")
        file_extension = os.path.splitext(original_blob_name)[1]
        timestamped_blob_name = f"{timestamp}{file_extension}"

        block_blob_client = container_client.get_blob_client(original_blob_name)

        # Check if the blob exists
        if not block_blob_client.exists():
            logging.error(f"Blob '{original_blob_name}' does not exist.")
            return

        # Download blob content to a stream
        downloader = block_blob_client.download_blob()
        blob_stream = downloader.readall()

        # Save the PDF to local storage
        with open(timestamped_blob_name, 'wb') as pdf_file:
            pdf_file.write(blob_stream)

        # Create a new blob client for the PDF file
        pdf_blob_client = container_client.get_blob_client(timestamped_blob_name)

        # Upload the PDF to Azure Blob Storage
        with open(timestamped_blob_name, 'rb') as data:
            pdf_blob_client.upload_blob(data, overwrite=True)

        logging.info(f"PDF file '{timestamped_blob_name}' downloaded and uploaded successfully.")

        poller = client.begin_analyze_document(model_id=model_id, document=blob_stream)
        result = poller.result()

        if not result.documents:
            raise Exception("Expected at least one document in the result.")

        document = result.documents[0]

        # Create a CSV writer
        csv_filename = f'result_{timestamp}.csv'
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [name for name in document.fields.keys()]
            writer = DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Transform document.fields into a format suitable for csv-writer
            record = {}
            for key, field in document.fields.items():
                if field.value_type == 'dictionary' and field.value and 'rows' in field.value:
                    # Check if the object is a table
                    if isinstance(field.value['rows'], list):
                        # Handle table data
                        for rowIndex, row in enumerate(field.value['rows']):
                            if row and isinstance(row, list):
                                for cellIndex, cell in enumerate(row):
                                    record[f"{key}_row{rowIndex}_cell{cellIndex}"] = cell.content
                else:
                    # Handle regular fields
                    record[key] = field.content if field.content else field.value

            writer.writerow(record)

        # Create a new blob client for the CSV file
        csv_blob_client = container_client.get_blob_client(csv_filename)

        # Upload the CSV file to Azure Blob Storage
        with open(csv_filename, 'rb') as data:
            csv_blob_client.upload_blob(data, overwrite=True)

        logging.info(f"CSV file '{csv_filename}' uploaded successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        main()

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
        Day3 = Day3.text_input("Day3", value=str(row_data.get('Day3', '')), key="Day3")
        Day3Yes = Day3Yes.text_input("Yes3", value=str(row_data.get('Day3Yes', '')), key="Day3Yes")
        Day3No = Day3No.text_input("No3", value=str(row_data.get('Day3No', '')), key="Day3No")
        Day3Dosage = Day3Dosage.text_input("Dosage3", value=str(row_data.get('Day3Dosage', '')), key="Day3Dosage")
        Day3Freq = Day3Freq.text_input("Frequency3", value=str(row_data.get('Day3Freq', '')), key="Day3Freq")
        Day3Form = Day3Form.text_input("Form3", value=str(row_data.get('Day3Form', '')), key="Day3Form")
        Day3Route = Day3Route.text_input("Route3", value=str(row_data.get('Day3Route', '')), key="Day3Route")

        

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

        Day8, Day8Yes, Day8No, Day8Dosage, Day8Freq, Day8Form, Day8Route = st.columns(7)
        Day8 = Day8.text_input("Day8", value=str(row_data.get('Day8', '')))
        Day8Yes = Day8Yes.text_input("Yes8", value=str(row_data.get('Day8Yes', '')))
        Day8No = Day8No.text_input("No8", value=str(row_data.get('Day8No', '')))
        Day8Dosage = Day8Dosage.text_input("Dosage8", value=str(row_data.get('Day8Dosage', '')))
        Day8Freq = Day8Freq.text_input("Frequency8", value=str(row_data.get('Day8Freq', '')))
        Day8Form = Day8Form.text_input("Form8", value=str(row_data.get('Day8Form', '')))
        Day8Route = Day8Route.text_input("Route8", value=str(row_data.get('Day8Route', '')))

        Day9, Day9Yes, Day9No, Day9Dosage, Day9Freq, Day9Form, Day9Route = st.columns(7)
        Day9 = Day9.text_input("Day9", value=str(row_data.get('Day9', '')))
        Day9Yes = Day9Yes.text_input("Yes9", value=str(row_data.get('Day9Yes', '')))
        Day9No = Day9No.text_input("No9", value=str(row_data.get('Day9No', '')))
        Day9Dosage = Day9Dosage.text_input("Dosage9", value=str(row_data.get('Day9Dosage', '')))
        Day9Freq = Day9Freq.text_input("Frequency9", value=str(row_data.get('Day9Freq', '')))
        Day9Form = Day9Form.text_input("Form9", value=str(row_data.get('Day9Form', '')))
        Day9Route = Day9Route.text_input("Route9", value=str(row_data.get('Day9Route', '')))

        Day10, Day10Yes, Day10No, Day10Dosage, Day10Freq, Day10Form, Day10Route = st.columns(7)
        Day10 = Day10.text_input("Day10", value=str(row_data.get('Day10', '')))
        Day10Yes = Day10Yes.text_input("Yes10", value=str(row_data.get('Day10Yes', '')))
        Day10No = Day10No.text_input("No10", value=str(row_data.get('Day10No', '')))
        Day10Dosage = Day10Dosage.text_input("Dosage10", value=str(row_data.get('Day10Dosage', '')))
        Day10Freq = Day10Freq.text_input("Frequency10", value=str(row_data.get('Day10Freq', '')))
        Day10Form = Day10Form.text_input("Form10", value=str(row_data.get('Day10Form', '')))
        Day10Route = Day10Route.text_input("Route10", value=str(row_data.get('Day10Route', '')))

        Day11, Day11Yes, Day11No, Day11Dosage, Day11Freq, Day11Form, Day11Route = st.columns(7)
        Day11 = Day11.text_input("Day11", value=str(row_data.get('Day11', '')))
        Day11Yes = Day11Yes.text_input("Yes11", value=str(row_data.get('Day11Yes', '')))
        Day11No = Day11No.text_input("No11", value=str(row_data.get('Day11No', '')))
        Day11Dosage = Day11Dosage.text_input("Dosage11", value=str(row_data.get('Day11Dosage', '')))
        Day11Freq = Day11Freq.text_input("Frequency11", value=str(row_data.get('Day11Freq', '')))
        Day11Form = Day11Form.text_input("Form11", value=str(row_data.get('Day11Form', '')))
        Day11Route = Day11Route.text_input("Route11", value=str(row_data.get('Day11Route', '')))

        Day12, Day12Yes, Day12No, Day12Dosage, Day12Freq, Day12Form, Day12Route = st.columns(7)
        Day12 = Day12.text_input("Day12", value=str(row_data.get('Day12', '')))
        Day12Yes = Day12Yes.text_input("Yes12", value=str(row_data.get('Day12Yes', '')))
        Day12No = Day12No.text_input("No12", value=str(row_data.get('Day12No', '')))
        Day12Dosage = Day12Dosage.text_input("Dosage12", value=str(row_data.get('Day12Dosage', '')))
        Day12Freq = Day12Freq.text_input("Frequency12", value=str(row_data.get('Day12Freq', '')))
        Day12Form = Day12Form.text_input("Form12", value=str(row_data.get('Day12Form', '')))
        Day12Route = Day12Route.text_input("Route12", value=str(row_data.get('Day12Route', '')))

        Day13, Day13Yes, Day13No, Day13Dosage, Day13Freq, Day13Form, Day13Route = st.columns(7)
        Day13 = Day13.text_input("Day13", value=str(row_data.get('Day13', '')))
        Day13Yes = Day13Yes.text_input("Yes13", value=str(row_data.get('Day13Yes', '')))
        Day13No = Day13No.text_input("No13", value=str(row_data.get('Day13No', '')))
        Day13Dosage = Day13Dosage.text_input("Dosage13", value=str(row_data.get('Day13Dosage', '')))
        Day13Freq = Day13Freq.text_input("Frequency13", value=str(row_data.get('Day13Freq', '')))
        Day13Form = Day13Form.text_input("Form13", value=str(row_data.get('Day13Form', '')))
        Day13Route = Day13Route.text_input("Route13", value=str(row_data.get('Day13Route', '')))

        Day14, Day14Yes, Day14No, Day14Dosage, Day14Freq, Day14Form, Day14Route = st.columns(7)
        Day14 = Day14.text_input("Day14", value=str(row_data.get('Day14', '')))
        Day14Yes = Day14Yes.text_input("Yes14", value=str(row_data.get('Day14Yes', '')))
        Day14No = Day14No.text_input("No14", value=str(row_data.get('Day14No', '')))
        Day14Dosage = Day14Dosage.text_input("Dosage14", value=str(row_data.get('Day14Dosage', '')))
        Day14Freq = Day14Freq.text_input("Frequency14", value=str(row_data.get('Day14Freq', '')))
        Day14Form = Day14Form.text_input("Form14", value=str(row_data.get('Day14Form', '')))
        Day14Route = Day14Route.text_input("Route14", value=str(row_data.get('Day14Route', '')))

        Day15, Day15Yes, Day15No, Day15Dosage, Day15Freq, Day15Form, Day15Route = st.columns(7)
        Day15 = Day15.text_input("Day15", value=str(row_data.get('Day15', '')))
        Day15Yes = Day15Yes.text_input("Yes15", value=str(row_data.get('Day15Yes', '')))
        Day15No = Day15No.text_input("No15", value=str(row_data.get('Day15No', '')))
        Day15Dosage = Day15Dosage.text_input("Dosage15", value=str(row_data.get('Day15Dosage', '')))
        Day15Freq = Day15Freq.text_input("Frequency15", value=str(row_data.get('Day15Freq', '')))
        Day15Form = Day15Form.text_input("Form15", value=str(row_data.get('Day15Form', '')))
        Day15Route = Day15Route.text_input("Route15", value=str(row_data.get('Day15Route', '')))

        Day16, Day16Yes, Day16No, Day16Dosage, Day16Freq, Day16Form, Day16Route = st.columns(7)
        Day16 = Day16.text_input("Day16", value=str(row_data.get('Day16', '')))
        Day16Yes = Day16Yes.text_input("Yes16", value=str(row_data.get('Day16Yes', '')))
        Day16No = Day16No.text_input("No16", value=str(row_data.get('Day16No', '')))
        Day16Dosage = Day16Dosage.text_input("Dosage16", value=str(row_data.get('Day16Dosage', '')))
        Day16Freq = Day16Freq.text_input("Frequency16", value=str(row_data.get('Day16Freq', '')))
        Day16Form = Day16Form.text_input("Form16", value=str(row_data.get('Day16Form', '')))
        Day16Route = Day16Route.text_input("Route16", value=str(row_data.get('Day16Route', '')))

        Day17, Day17Yes, Day17No, Day17Dosage, Day17Freq, Day17Form, Day17Route = st.columns(7)
        Day17 = Day17.text_input("Day17", value=str(row_data.get('Day17', '')))
        Day17Yes = Day17Yes.text_input("Yes17", value=str(row_data.get('Day17Yes', '')))
        Day17No = Day17No.text_input("No17", value=str(row_data.get('Day17No', '')))
        Day17Dosage = Day17Dosage.text_input("Dosage17", value=str(row_data.get('Day17Dosage', '')))
        Day17Freq = Day17Freq.text_input("Frequency17", value=str(row_data.get('Day17Freq', '')))
        Day17Form = Day17Form.text_input("Form17", value=str(row_data.get('Day17Form', '')))
        Day17Route = Day17Route.text_input("Route17", value=str(row_data.get('Day17Route', '')))

        Day18, Day18Yes, Day18No, Day18Dosage, Day18Freq, Day18Form, Day18Route = st.columns(7)
        Day18 = Day18.text_input("Day18", value=str(row_data.get('Day18', '')))
        Day18Yes = Day18Yes.text_input("Yes18", value=str(row_data.get('Day18Yes', '')))
        Day18No = Day18No.text_input("No18", value=str(row_data.get('Day18No', '')))
        Day18Dosage = Day18Dosage.text_input("Dosage18", value=str(row_data.get('Day18Dosage', '')))
        Day18Freq = Day18Freq.text_input("Frequency18", value=str(row_data.get('Day18Freq', '')))
        Day18Form = Day18Form.text_input("Form18", value=str(row_data.get('Day18Form', '')))
        Day18Route = Day18Route.text_input("Route18", value=str(row_data.get('Day18Route', '')))
        
        Day19, Day19Yes, Day19No, Day19Dosage, Day19Freq, Day19Form, Day19Route = st.columns(7)
        Day19 = Day19.text_input("Day19", value=str(row_data.get('Day19', '')))
        Day19Yes = Day19Yes.text_input("Yes19", value=str(row_data.get('Day19Yes', '')))
        Day19No = Day19No.text_input("No19", value=str(row_data.get('Day19No', '')))
        Day19Dosage = Day19Dosage.text_input("Dosage19", value=str(row_data.get('Day19Dosage', '')))
        Day19Freq = Day19Freq.text_input("Frequency19", value=str(row_data.get('Day19Freq', '')))
        Day19Form = Day19Form.text_input("Form19", value=str(row_data.get('Day19Form', '')))
        Day19Route = Day19Route.text_input("Route19", value=str(row_data.get('Day19Route', '')))

       

        Day20, Day20Yes, Day20No, Day20Dosage, Day20Freq, Day20Form, Day20Route = st.columns(7)
        Day20 = Day20.text_input("Day20", value=str(row_data.get('Day20', '')))
        Day20Yes = Day20Yes.text_input("Yes20", value=str(row_data.get('Day20Yes', '')))
        Day20No = Day20No.text_input("No20", value=str(row_data.get('Day20No', '')))
        Day20Dosage = Day20Dosage.text_input("Dosage20", value=str(row_data.get('Day20Dosage', '')))
        Day20Freq = Day20Freq.text_input("Frequency20", value=str(row_data.get('Day20Freq', '')))
        Day20Form = Day20Form.text_input("Form20", value=str(row_data.get('Day20Form', '')))
        Day20Route = Day20Route.text_input("Route20", value=str(row_data.get('Day20Route', '')))

        Day21, Day21Yes, Day21No, Day21Dosage, Day21Freq, Day21Form, Day21Route = st.columns(7)
        Day21 = Day21.text_input("Day21", value=str(row_data.get('Day21', '')))
        Day21Yes = Day21Yes.text_input("Yes21", value=str(row_data.get('Day21Yes', '')))
        Day21No = Day21No.text_input("No21", value=str(row_data.get('Day21No', '')))
        Day21Dosage = Day21Dosage.text_input("Dosage21", value=str(row_data.get('Day21Dosage', '')))
        Day21Freq = Day21Freq.text_input("Frequency21", value=str(row_data.get('Day21Freq', '')))
        Day21Form = Day21Form.text_input("Form21", value=str(row_data.get('Day21Form', '')))
        Day21Route = Day21Route.text_input("Route21", value=str(row_data.get('Day21Route', '')))

        Day22, Day22Yes, Day22No, Day22Dosage, Day22Freq, Day22Form, Day22Route = st.columns(7)
        Day22 = Day22.text_input("Day22", value=str(row_data.get('Day22', '')))
        Day22Yes = Day22Yes.text_input("Yes22", value=str(row_data.get('Day22Yes', '')))
        Day22No = Day22No.text_input("No22", value=str(row_data.get('Day22No', '')))
        Day22Dosage = Day22Dosage.text_input("Dosage22", value=str(row_data.get('Day22Dosage', '')))