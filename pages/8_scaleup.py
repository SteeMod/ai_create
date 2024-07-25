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
    with st.form("Review"):
        # Use columns to place fields side by side
        col1, col2 = st.columns(2)
        FirstName = col1.st.text_input("FirstName", value=str(row_data.get('FirstName', '')))
        LastName = col2.st.text_input("LastName", value=str(row_data.get('LastName', '')))
        Address = st.text_input("Address", value=str(row_data.get('Address', '')))
        City, State = st.columns(2)
        City = City.st.text_input("City", value=str(row_data.get('City', '')))
        State = State.st.text_input("State", value=str(row_data.get('State', '')))
        ZipCode, Phone = st.columns(2)
        ZipCode = ZipCode.st.text_input("ZipCode", value=str(row_data.get('ZipCode', '')))
        Phone = Phone.st.text_input("Phone", value=str(row_data.get('Phone', '')))
        Allergy1, Allergy2 = st.columns(2)
        Allergy1 = Allergy1.st.text_input("Allergy1", value=str(row_data.get('Allergy1', '')))
        Allergy2 = Allergy2.st.text_input("Allergy2", value=str(row_data.get('Allergy2', '')))

        # Medication details section
        MedIntakeName, MedIntakeMonth, MedIntakeYear = st.columns(3)
        MedIntakeName = MedIntakeName.st.text_input("MEDICATION NAME", value=str(row_data.get('MedIntakeName', '')))
        MedIntakeMonth = MedIntakeMonth.st.text_input("MONTH", value=str(row_data.get('MedIntakeMonth', '')))
        MedIntakeYear = MedIntakeYear.st.text_input("YEAR", value=str(row_data.get('MedIntakeYear', '')))

        # Treatment Plan table
        Med1Check, Med1Name, Med1Dosage, Med1Frequency, Med1Form, Med1Route, Med1Instructions = st.columns(7)
        Med1Check = Med1Check.st.text_input("Select [x]1", value=str(row_data.get('Med1Check', '')))
        Med1Name = Med1Name.st.text_input("Medication1", value=str(row_data.get('Med1Name', '')))
        Med1Dosage = Med1Dosage.st.text_input("Dosage1", value=str(row_data.get('Med1Dosage', '')))
        Med1Frequency = Med1Frequency.st.text_input("Frequency1", value=str(row_data.get('Med1Frequency', '')))
        Med1Form = Med1Form.st.text_input("Form1", value=str(row_data.get('Med1Form', '')))
        Med1Route = Med1Route.st.text_input("Route1", value=str(row_data.get('Med1Route', '')))
        Med1Instructions = Med1Instructions.st.text_input("Instructions1", value=str(row_data.get('Med1Instructions', '')))

        Med2Check, Med2Name, Med2Dosage, Med2Frequency, Med2Form, Med2Route, Med2Instructions = st.columns(7)
        Med2Check = Med2Check.st.text_input("Select [x]2", value=str(row_data.get('Med2Check', '')))
        Med2Name = Med2Name.st.text_input("Medication2", value=str(row_data.get('Med2Name', '')))
        Med2Dosage = Med2Dosage.st.text_input("Dosage2", value=str(row_data.get('Med2Dosage', '')))
        Med2Frequency = Med2Frequency.st.text_input("Frequency2", value=str(row_data.get('Med2Frequency', '')))
        Med2Form = Med2Form.st.text_input("Form2", value=str(row_data.get('Med2Form', '')))
        Med2Route = Med2Route.st.text_input("Route2", value=str(row_data.get('Med2Route', '')))
        Med2Instructions = Med2Instructions.st.text_input("Instructions2", value=str(row_data.get('Med2Instructions', '')))

        Med3Check, Med3Name, Med3Dosage, Med3Frequency, Med3Form, Med3Route, Med3Instructions = st.columns(7)
        Med3Check = Med3Check.st.text_input("Select [x]3", value=str(row_data.get('Med3Check', '')))
        Med3Name = Med3Name.st.text_input("Medication3", value=str(row_data.get('Med3Name', '')))
        Med3Dosage = Med3Dosage.st.text_input("Dosage3", value=str(row_data.get('Med3Dosage', '')))
        Med3Frequency = Med3Frequency.st.text_input("Frequency3", value=str(row_data.get('Med3Frequency', '')))
        Med3Form = Med3Form.st.text_input("Form3", value=str(row_data.get('Med3Form', '')))
        Med3Route = Med3Route.st.text_input("Route3", value=str(row_data.get('Med3Route', '')))
        Med3Instructions = Med3Instructions.st.text_input("Instructions3", value=str(row_data.get('Med3Instructions', '')))

        Med4Check, Med4Name, Med4Dosage, Med4Frequency, Med4Form, Med4Route, Med4Instructions = st.columns(7)
        Med4Check = Med4Check.st.text_input("Select [x]4", value=str(row_data.get('Med4Check', '')))
        Med4Name = Med4Name.st.text_input("Medication4", value=str(row_data.get('Med4Name', '')))
        Med4Dosage = Med4Dosage.st.text_input("Dosage4", value=str(row_data.get('Med4Dosage', '')))
        Med4Frequency = Med4Frequency.st.text_input("Frequency4", value=str(row_data.get('Med4Frequency', '')))
        Med4Form = Med4Form.st.text_input("Form4", value=str(row_data.get('Med4Form', '')))
        Med4Route = Med4Route.st.text_input("Route4", value=str(row_data.get('Med4Route', '')))
        Med4Instructions = Med4Instructions.st.text_input("Instructions4", value=str(row_data.get('Med4Instructions', '')))
 
        # Treatment Plan table
        Day1, Day1Yes, Day1No, Day1Dosage, Day1Freq, Day1Form, Day1Route = st.columns(7)
        Day1 = Day1.st.text_input("Day1", value=str(row_data.get('Day1', '')))
        Day1Yes = Day1Yes.st.text_input("Yes1", value=str(row_data.get('Day1Yes', '')))
        Day1No = Day1No.st.text_input("No1", value=str(row_data.get('Day1No', '')))
        Day1Dosage = Day1Dosage.st.text_input("Dosage1", value=str(row_data.get('Day1Dosage', '')))
        Day1Freq = Day1Freq.st.text_input("Frequency1", value=str(row_data.get('Day1Freq', '')))
        Day1Form = Day1Form.st.text_input("Form1", value=str(row_data.get('Day1Form', '')))
        Day1Route = Day1Route.st.text_input("Route1", value=str(row_data.get('Day1Route', '')))

        Day2, Day2Yes, Day2No, Day2Dosage, Day2Freq, Day2Form, Day2Route = st.columns(7)
        Day2 = Day2.st.text_input("Day2", value=str(row_data.get('Day2', '')))
        Day2Yes = Day2Yes.st.text_input("Yes2", value=str(row_data.get('Day2Yes', '')))
        Day2No = Day2No.st.text_input("No2", value=str(row_data.get('Day2No', '')))
        Day2Dosage = Day2Dosage.st.text_input("Dosage2", value=str(row_data.get('Day2Dosage', '')))
        Day2Freq = Day2Freq.st.text_input("Frequency2", value=str(row_data.get('Day2Freq', '')))
        Day2Form = Day2Form.st.text_input("Form2", value=str(row_data.get('Day2Form', '')))
        Day2Route = Day2Route.st.text_input("Route2", value=str(row_data.get('Day2Route', '')))

        Day3, Day3Yes, Day3No, Day3Dosage, Day3Freq, Day3Form, Day3Route = st.columns(7)
        Day3 = Day3.st.text_input("Day3", value=str(row_data.get('Day3', '')), key="Day3")
        Day3Yes = Day3Yes.st.text_input("Yes3", value=str(row_data.get('Day3Yes', '')), key="Day3Yes")
        Day3No = Day3No.st.text_input("No3", value=str(row_data.get('Day3No', '')), key="Day3No")
        Day3Dosage = Day3Dosage.st.text_input("Dosage3", value=str(row_data.get('Day3Dosage', '')), key="Day3Dosage")
        Day3Freq = Day3Freq.st.text_input("Frequency3", value=str(row_data.get('Day3Freq', '')), key="Day3Freq")
        Day3Form = Day3Form.st.text_input("Form3", value=str(row_data.get('Day3Form', '')), key="Day3Form")
        Day3Route = Day3Route.st.text_input("Route3", value=str(row_data.get('Day3Route', '')), key="Day3Route")

        

        Day4, Day4Yes, Day4No, Day4Dosage, Day4Freq, Day4Form, Day4Route = st.columns(7)
        Day4 = Day4.st.text_input("Day4", value=str(row_data.get('Day4', '')))
        Day4Yes = Day4Yes.st.text_input("Yes4", value=str(row_data.get('Day4Yes', '')))
        Day4No = Day4No.st.text_input("No4", value=str(row_data.get('Day4No', '')))
        Day4Dosage = Day4Dosage.st.text_input("Dosage4", value=str(row_data.get('Day4Dosage', '')))
        Day4Freq = Day4Freq.st.text_input("Frequency4", value=str(row_data.get('Day4Freq', '')))
        Day4Form = Day4Form.st.text_input("Form4", value=str(row_data.get('Day4Form', '')))
        Day4Route = Day4Route.st.text_input("Route4", value=str(row_data.get('Day4Route', '')))

        Day5, Day5Yes, Day5No, Day5Dosage, Day5Freq, Day5Form, Day5Route = st.columns(7)
        Day5 = Day5.st.text_input("Day5", value=str(row_data.get('Day5', '')))
        Day5Yes = Day5Yes.st.text_input("Yes5", value=str(row_data.get('Day5Yes', '')))
        Day5No = Day5No.st.text_input("No5", value=str(row_data.get('Day5No', '')))
        Day5Dosage = Day5Dosage.st.text_input("Dosage5", value=str(row_data.get('Day5Dosage', '')))
        Day5Freq = Day5Freq.st.text_input("Frequency5", value=str(row_data.get('Day5Freq', '')))
        Day5Form = Day5Form.st.text_input("Form5", value=str(row_data.get('Day5Form', '')))
        Day5Route = Day5Route.st.text_input("Route5", value=str(row_data.get('Day5Route', '')))

        Day6, Day6Yes, Day6No, Day6Dosage, Day6Freq, Day6Form, Day6Route = st.columns(7)
        Day6 = Day6.st.text_input("Day6", value=str(row_data.get('Day6', '')))
        Day6Yes = Day6Yes.st.text_input("Yes6", value=str(row_data.get('Day6Yes', '')))
        Day6No = Day6No.st.text_input("No6", value=str(row_data.get('Day6No', '')))
        Day6Dosage = Day6Dosage.st.text_input("Dosage6", value=str(row_data.get('Day6Dosage', '')))
        Day6Freq = Day6Freq.st.text_input("Frequency6", value=str(row_data.get('Day6Freq', '')))
        Day6Form = Day6Form.st.text_input("Form6", value=str(row_data.get('Day6Form', '')))
        Day6Route = Day6Route.st.text_input("Route6", value=str(row_data.get('Day6Route', '')))

        Day7, Day7Yes, Day7No, Day7Dosage, Day7Freq, Day7Form, Day7Route = st.columns(7)
        Day7 = Day7.st.text_input("Day7", value=str(row_data.get('Day7', '')))
        Day7Yes = Day7Yes.st.text_input("Yes7", value=str(row_data.get('Day7Yes', '')))
        Day7No = Day7No.st.text_input("No7", value=str(row_data.get('Day7No', '')))
        Day7Dosage = Day7Dosage.st.text_input("Dosage7", value=str(row_data.get('Day7Dosage', '')))
        Day7Freq = Day7Freq.st.text_input("Frequency7", value=str(row_data.get('Day7Freq', '')))
        Day7Form = Day7Form.st.text_input("Form7", value=str(row_data.get('Day7Form', '')))
        Day7Route = Day7Route.st.text_input("Route7", value=str(row_data.get('Day7Route', '')))

        Day8, Day8Yes, Day8No, Day8Dosage, Day8Freq, Day8Form, Day8Route = st.columns(7)
        Day8 = Day8.st.text_input("Day8", value=str(row_data.get('Day8', '')))
        Day8Yes = Day8Yes.st.text_input("Yes8", value=str(row_data.get('Day8Yes', '')))
        Day8No = Day8No.st.text_input("No8", value=str(row_data.get('Day8No', '')))
        Day8Dosage = Day8Dosage.st.text_input("Dosage8", value=str(row_data.get('Day8Dosage', '')))
        Day8Freq = Day8Freq.st.text_input("Frequency8", value=str(row_data.get('Day8Freq', '')))
        Day8Form = Day8Form.st.text_input("Form8", value=str(row_data.get('Day8Form', '')))
        Day8Route = Day8Route.st.text_input("Route8", value=str(row_data.get('Day8Route', '')))

        Day9, Day9Yes, Day9No, Day9Dosage, Day9Freq, Day9Form, Day9Route = st.columns(7)
        Day9 = Day9.st.text_input("Day9", value=str(row_data.get('Day9', '')))
        Day9Yes = Day9Yes.st.text_input("Yes9", value=str(row_data.get('Day9Yes', '')))
        Day9No = Day9No.st.text_input("No9", value=str(row_data.get('Day9No', '')))
        Day9Dosage = Day9Dosage.st.text_input("Dosage9", value=str(row_data.get('Day9Dosage', '')))
        Day9Freq = Day9Freq.st.text_input("Frequency9", value=str(row_data.get('Day9Freq', '')))
        Day9Form = Day9Form.st.text_input("Form9", value=str(row_data.get('Day9Form', '')))
        Day9Route = Day9Route.st.text_input("Route9", value=str(row_data.get('Day9Route', '')))

        Day10, Day10Yes, Day10No, Day10Dosage, Day10Freq, Day10Form, Day10Route = st.columns(7)
        Day10 = Day10.st.text_input("Day10", value=str(row_data.get('Day10', '')))
        Day10Yes = Day10Yes.st.text_input("Yes10", value=str(row_data.get('Day10Yes', '')))
        Day10No = Day10No.st.text_input("No10", value=str(row_data.get('Day10No', '')))
        Day10Dosage = Day10Dosage.st.text_input("Dosage10", value=str(row_data.get('Day10Dosage', '')))
        Day10Freq = Day10Freq.st.text_input("Frequency10", value=str(row_data.get('Day10Freq', '')))
        Day10Form = Day10Form.st.text_input("Form10", value=str(row_data.get('Day10Form', '')))
        Day10Route = Day10Route.st.text_input("Route10", value=str(row_data.get('Day10Route', '')))

        Day11, Day11Yes, Day11No, Day11Dosage, Day11Freq, Day11Form, Day11Route = st.columns(7)
        Day11 = Day11.st.text_input("Day11", value=str(row_data.get('Day11', '')))
        Day11Yes = Day11Yes.st.text_input("Yes11", value=str(row_data.get('Day11Yes', '')))
        Day11No = Day11No.st.text_input("No11", value=str(row_data.get('Day11No', '')))
        Day11Dosage = Day11Dosage.st.text_input("Dosage11", value=str(row_data.get('Day11Dosage', '')))
        Day11Freq = Day11Freq.st.text_input("Frequency11", value=str(row_data.get('Day11Freq', '')))
        Day11Form = Day11Form.st.text_input("Form11", value=str(row_data.get('Day11Form', '')))
        Day11Route = Day11Route.st.text_input("Route11", value=str(row_data.get('Day11Route', '')))

        Day12, Day12Yes, Day12No, Day12Dosage, Day12Freq, Day12Form, Day12Route = st.columns(7)
        Day12 = Day12.st.text_input("Day12", value=str(row_data.get('Day12', '')))
        Day12Yes = Day12Yes.st.text_input("Yes12", value=str(row_data.get('Day12Yes', '')))
        Day12No = Day12No.st.text_input("No12", value=str(row_data.get('Day12No', '')))
        Day12Dosage = Day12Dosage.st.text_input("Dosage12", value=str(row_data.get('Day12Dosage', '')))
        Day12Freq = Day12Freq.st.text_input("Frequency12", value=str(row_data.get('Day12Freq', '')))
        Day12Form = Day12Form.st.text_input("Form12", value=str(row_data.get('Day12Form', '')))
        Day12Route = Day12Route.st.text_input("Route12", value=str(row_data.get('Day12Route', '')))

        Day13, Day13Yes, Day13No, Day13Dosage, Day13Freq, Day13Form, Day13Route = st.columns(7)
        Day13 = Day13.st.text_input("Day13", value=str(row_data.get('Day13', '')))
        Day13Yes = Day13Yes.st.text_input("Yes13", value=str(row_data.get('Day13Yes', '')))
        Day13No = Day13No.st.text_input("No13", value=str(row_data.get('Day13No', '')))
        Day13Dosage = Day13Dosage.st.text_input("Dosage13", value=str(row_data.get('Day13Dosage', '')))
        Day13Freq = Day13Freq.st.text_input("Frequency13", value=str(row_data.get('Day13Freq', '')))
        Day13Form = Day13Form.st.text_input("Form13", value=str(row_data.get('Day13Form', '')))
        Day13Route = Day13Route.st.text_input("Route13", value=str(row_data.get('Day13Route', '')))

        Day14, Day14Yes, Day14No, Day14Dosage, Day14Freq, Day14Form, Day14Route = st.columns(7)
        Day14 = Day14.st.text_input("Day14", value=str(row_data.get('Day14', '')))
        Day14Yes = Day14Yes.st.text_input("Yes14", value=str(row_data.get('Day14Yes', '')))
        Day14No = Day14No.st.text_input("No14", value=str(row_data.get('Day14No', '')))
        Day14Dosage = Day14Dosage.st.text_input("Dosage14", value=str(row_data.get('Day14Dosage', '')))
        Day14Freq = Day14Freq.st.text_input("Frequency14", value=str(row_data.get('Day14Freq', '')))
        Day14Form = Day14Form.st.text_input("Form14", value=str(row_data.get('Day14Form', '')))
        Day14Route = Day14Route.st.text_input("Route14", value=str(row_data.get('Day14Route', '')))

        Day15, Day15Yes, Day15No, Day15Dosage, Day15Freq, Day15Form, Day15Route = st.columns(7)
        Day15 = Day15.st.text_input("Day15", value=str(row_data.get('Day15', '')))
        Day15Yes = Day15Yes.st.text_input("Yes15", value=str(row_data.get('Day15Yes', '')))
        Day15No = Day15No.st.text_input("No15", value=str(row_data.get('Day15No', '')))
        Day15Dosage = Day15Dosage.st.text_input("Dosage15", value=str(row_data.get('Day15Dosage', '')))
        Day15Freq = Day15Freq.st.text_input("Frequency15", value=str(row_data.get('Day15Freq', '')))
        Day15Form = Day15Form.st.text_input("Form15", value=str(row_data.get('Day15Form', '')))
        Day15Route = Day15Route.st.text_input("Route15", value=str(row_data.get('Day15Route', '')))

        Day16, Day16Yes, Day16No, Day16Dosage, Day16Freq, Day16Form, Day16Route = st.columns(7)
        Day16 = Day16.st.text_input("Day16", value=str(row_data.get('Day16', '')))
        Day16Yes = Day16Yes.st.text_input("Yes16", value=str(row_data.get('Day16Yes', '')))
        Day16No = Day16No.st.text_input("No16", value=str(row_data.get('Day16No', '')))
        Day16Dosage = Day16Dosage.st.text_input("Dosage16", value=str(row_data.get('Day16Dosage', '')))
        Day16Freq = Day16Freq.st.text_input("Frequency16", value=str(row_data.get('Day16Freq', '')))
        Day16Form = Day16Form.st.text_input("Form16", value=str(row_data.get('Day16Form', '')))
        Day16Route = Day16Route.st.text_input("Route16", value=str(row_data.get('Day16Route', '')))

        Day17, Day17Yes, Day17No, Day17Dosage, Day17Freq, Day17Form, Day17Route = st.columns(7)
        Day17 = Day17.st.text_input("Day17", value=str(row_data.get('Day17', '')))
        Day17Yes = Day17Yes.st.text_input("Yes17", value=str(row_data.get('Day17Yes', '')))
        Day17No = Day17No.st.text_input("No17", value=str(row_data.get('Day17No', '')))
        Day17Dosage = Day17Dosage.st.text_input("Dosage17", value=str(row_data.get('Day17Dosage', '')))
        Day17Freq = Day17Freq.st.text_input("Frequency17", value=str(row_data.get('Day17Freq', '')))
        Day17Form = Day17Form.st.text_input("Form17", value=str(row_data.get('Day17Form', '')))
        Day17Route = Day17Route.st.text_input("Route17", value=str(row_data.get('Day17Route', '')))

        Day18, Day18Yes, Day18No, Day18Dosage, Day18Freq, Day18Form, Day18Route = st.columns(7)
        Day18 = Day18.st.text_input("Day18", value=str(row_data.get('Day18', '')))
        Day18Yes = Day18Yes.st.text_input("Yes18", value=str(row_data.get('Day18Yes', '')))
        Day18No = Day18No.st.text_input("No18", value=str(row_data.get('Day18No', '')))
        Day18Dosage = Day18Dosage.st.text_input("Dosage18", value=str(row_data.get('Day18Dosage', '')))
        Day18Freq = Day18Freq.st.text_input("Frequency18", value=str(row_data.get('Day18Freq', '')))
        Day18Form = Day18Form.st.text_input("Form18", value=str(row_data.get('Day18Form', '')))
        Day18Route = Day18Route.st.text_input("Route18", value=str(row_data.get('Day18Route', '')))
        
        Day19, Day19Yes, Day19No, Day19Dosage, Day19Freq, Day19Form, Day19Route = st.columns(7)
        Day19 = Day19.st.text_input("Day19", value=str(row_data.get('Day19', '')))
        Day19Yes = Day19Yes.st.text_input("Yes19", value=str(row_data.get('Day19Yes', '')))
        Day19No = Day19No.st.text_input("No19", value=str(row_data.get('Day19No', '')))
        Day19Dosage = Day19Dosage.st.text_input("Dosage19", value=str(row_data.get('Day19Dosage', '')))
        Day19Freq = Day19Freq.st.text_input("Frequency19", value=str(row_data.get('Day19Freq', '')))
        Day19Form = Day19Form.st.text_input("Form19", value=str(row_data.get('Day19Form', '')))
        Day19Route = Day19Route.st.text_input("Route19", value=str(row_data.get('Day19Route', '')))

       

        Day20, Day20Yes, Day20No, Day20Dosage, Day20Freq, Day20Form, Day20Route = st.columns(7)
        Day20 = Day20.st.text_input("Day20", value=str(row_data.get('Day20', '')))
        Day20Yes = Day20Yes.st.text_input("Yes20", value=str(row_data.get('Day20Yes', '')))
        Day20No = Day20No.st.text_input("No20", value=str(row_data.get('Day20No', '')))
        Day20Dosage = Day20Dosage.st.text_input("Dosage20", value=str(row_data.get('Day20Dosage', '')))
        Day20Freq = Day20Freq.st.text_input("Frequency20", value=str(row_data.get('Day20Freq', '')))
        Day20Form = Day20Form.st.text_input("Form20", value=str(row_data.get('Day20Form', '')))
        Day20Route = Day20Route.st.text_input("Route20", value=str(row_data.get('Day20Route', '')))

        Day21, Day21Yes, Day21No, Day21Dosage, Day21Freq, Day21Form, Day21Route = st.columns(7)
        Day21 = Day21.st.text_input("Day21", value=str(row_data.get('Day21', '')))
        Day21Yes = Day21Yes.st.text_input("Yes21", value=str(row_data.get('Day21Yes', '')))
        Day21No = Day21No.st.text_input("No21", value=str(row_data.get('Day21No', '')))
        Day21Dosage = Day21Dosage.st.text_input("Dosage21", value=str(row_data.get('Day21Dosage', '')))
        Day21Freq = Day21Freq.st.text_input("Frequency21", value=str(row_data.get('Day21Freq', '')))
        Day21Form = Day21Form.st.text_input("Form21", value=str(row_data.get('Day21Form', '')))
        Day21Route = Day21Route.st.text_input("Route21", value=str(row_data.get('Day21Route', '')))

        Day22, Day22Yes, Day22No, Day22Dosage, Day22Freq, Day22Form, Day22Route = st.columns(7)
        Day22 = Day22.st.text_input("Day22", value=str(row_data.get('Day22', '')))
        Day22Yes = Day22Yes.st.text_input("Yes22", value=str(row_data.get('Day22Yes', '')))
        Day22No = Day22No.st.text_input("No22", value=str(row_data.get('Day22No', '')))
        Day22Dosage = Day22Dosage.st.text_input("Dosage22", value=str(row_data.get('Day22Dosage', '')))
        Day22Freq = Day22Freq.st.text_input("Frequency22", value=str(row_data.get('Day22Freq', '')))
        Day22Form = Day22Form.st.text_input("Form22", value=str(row_data.get('Day22Form', '')))
        Day22Route = Day22Route.st.text_input("Route22", value=str(row_data.get('Day22Route', '')))

        Day23, Day23Yes, Day23No, Day23Dosage, Day23Freq, Day23Form, Day23Route = st.columns(7)
        Day23 = Day23.st.text_input("Day23", value=str(row_data.get('Day23', '')))
        Day23Yes = Day23Yes.st.text_input("Yes23", value=str(row_data.get('Day23Yes', '')))
        Day23No = Day23No.st.text_input("No23", value=str(row_data.get('Day23No', '')))
        Day23Dosage = Day23Dosage.st.text_input("Dosage23", value=str(row_data.get('Day23Dosage', '')))
        Day23Freq = Day23Freq.st.text_input("Frequency23", value=str(row_data.get('Day23Freq', '')))
        Day23Form = Day23Form.st.text_input("Form23", value=str(row_data.get('Day23Form', '')))
        Day23Route = Day23Route.st.text_input("Route23", value=str(row_data.get('Day23Route', '')))

        Day24, Day24Yes, Day24No, Day24Dosage, Day24Freq, Day24Form, Day24Route = st.columns(7)
        Day24 = Day24.st.text_input("Day24", value=str(row_data.get('Day24', '')))
        Day24Yes = Day24Yes.st.text_input("Yes24", value=str(row_data.get('Day24Yes', '')))
        Day24No = Day24No.st.text_input("No24", value=str(row_data.get('Day24No', '')))
        Day24Dosage = Day24Dosage.st.text_input("Dosage24", value=str(row_data.get('Day24Dosage', '')))
        Day24Freq = Day24Freq.st.text_input("Frequency24", value=str(row_data.get('Day24Freq', '')))
        Day24Form = Day24Form.st.text_input("Form24", value=str(row_data.get('Day24Form', '')))
        Day24Route = Day24Route.st.text_input("Route24", value=str(row_data.get('Day24Route', '')))

        Day25, Day25Yes, Day25No, Day25Dosage, Day25Freq, Day25Form, Day25Route = st.columns(7)
        Day25 = Day25.st.text_input("Day25", value=str(row_data.get('Day25', '')))
        Day25Yes = Day25Yes.st.text_input("Yes25", value=str(row_data.get('Day25Yes', '')))
        Day25No = Day25No.st.text_input("No25", value=str(row_data.get('Day25No', '')))
        Day25Dosage = Day25Dosage.st.text_input("Dosage25", value=str(row_data.get('Day25Dosage', '')))
        Day25Freq = Day25Freq.st.text_input("Frequency25", value=str(row_data.get('Day25Freq', '')))
        Day25Form = Day25Form.st.text_input("Form25", value=str(row_data.get('Day25Form', '')))
        Day25Route = Day25Route.st.text_input("Route25", value=str(row_data.get('Day25Route', '')))

        Day26, Day26Yes, Day26No, Day26Dosage, Day26Freq, Day26Form, Day26Route = st.columns(7)
        Day26 = Day26.st.text_input("Day26", value=str(row_data.get('Day26', '')))
        Day26Yes = Day26Yes.st.text_input("Yes26", value=str(row_data.get('Day26Yes', '')))
        Day26No = Day26No.st.text_input("No26", value=str(row_data.get('Day26No', '')))
        Day26Dosage = Day26Dosage.st.text_input("Dosage26", value=str(row_data.get('Day26Dosage', '')))
        Day26Freq = Day26Freq.st.text_input("Frequency26", value=str(row_data.get('Day26Freq', '')))
        Day26Form = Day26Form.st.text_input("Form26", value=str(row_data.get('Day26Form', '')))
        Day26Route = Day26Route.st.text_input("Route26", value=str(row_data.get('Day26Route', '')))

        Day27, Day27Yes, Day27No, Day27Dosage, Day27Freq, Day27Form, Day27Route = st.columns(7)
        Day27 = Day27.st.text_input("Day27", value=str(row_data.get('Day27', '')))
        Day27Yes = Day27Yes.st.text_input("Yes27", value=str(row_data.get('Day27Yes', '')))
        Day27No = Day27No.st.text_input("No27", value=str(row_data.get('Day27No', '')))
        Day27Dosage = Day27Dosage.st.text_input("Dosage27", value=str(row_data.get('Day27Dosage', '')))
        Day27Freq = Day27Freq.st.text_input("Frequency27", value=str(row_data.get('Day27Freq', '')))
        Day27Form = Day27Form.st.text_input("Form27", value=str(row_data.get('Day27Form', '')))
        Day27Route = Day27Route.st.text_input("Route27", value=str(row_data.get('Day27Route', '')))

        Day28, Day28Yes, Day28No, Day28Dosage, Day28Freq, Day28Form, Day28Route = st.columns(7)
        Day28 = Day28.st.text_input("Day28", value=str(row_data.get('Day28', '')))
        Day28Yes = Day28Yes.st.text_input("Yes28", value=str(row_data.get('Day28Yes', '')))
        Day28No = Day28No.st.text_input("No28", value=str(row_data.get('Day28No', '')))
        Day28Dosage = Day28Dosage.st.text_input("Dosage28", value=str(row_data.get('Day28Dosage', '')))
        Day28Freq = Day28Freq.st.text_input("Frequency28", value=str(row_data.get('Day28Freq', '')))
        Day28Form = Day28Form.st.text_input("Form28", value=str(row_data.get('Day28Form', '')))
        Day28Route = Day28Route.st.text_input("Route28", value=str(row_data.get('Day28Route', '')))

        Day29, Day29Yes, Day29No, Day29Dosage, Day29Freq, Day29Form, Day29Route = st.columns(7)
        Day29 = Day29.st.text_input("Day29", value=str(row_data.get('Day29', '')))
        Day29Yes = Day29Yes.st.text_input("Yes29", value=str(row_data.get('Day29Yes', '')))
        Day29No = Day29No.st.text_input("No29", value=str(row_data.get('Day29No', '')))
        Day29Dosage = Day29Dosage.st.text_input("Dosage29", value=str(row_data.get('Day29Dosage', '')))
        Day29Freq = Day29Freq.st.text_input("Frequency29", value=str(row_data.get('Day29Freq', '')))
        Day29Form = Day29Form.st.text_input("Form29", value=str(row_data.get('Day29Form', '')))
        Day29Route = Day29Route.st.text_input("Route29", value=str(row_data.get('Day29Route', '')))

        Day30, Day30Yes, Day30No, Day30Dosage, Day30Freq, Day30Form, Day30Route = st.columns(7)
        Day30 = Day30.st.text_input("Day30", value=str(row_data.get('Day30', '')))
        Day30Yes = Day30Yes.st.text_input("Yes30", value=str(row_data.get('Day30Yes', '')))
        Day30No = Day30No.st.text_input("No30", value=str(row_data.get('Day30No', '')))
        Day30Dosage = Day30Dosage.st.text_input("Dosage30", value=str(row_data.get('Day30Dosage', '')))
        Day30Freq = Day30Freq.st.text_input("Frequency30", value=str(row_data.get('Day30Freq', '')))
        Day30Form = Day30Form.st.text_input("Form30", value=str(row_data.get('Day30Form', '')))
        Day30Route = Day30Route.st.text_input("Route30", value=str(row_data.get('Day30Route', '')))

        Day31, Day31Yes, Day31No, Day31Dosage, Day31Freq, Day31Form, Day31Route = st.columns(7)
        Day31 = Day31.st.text_input("Day31", value=str(row_data.get('Day31', '')))
        Day31Yes = Day31Yes.st.text_input("Yes31", value=str(row_data.get('Day31Yes', '')))
        Day31No = Day31No.st.text_input("No31", value=str(row_data.get('Day31No', '')))
        Day31Dosage = Day31Dosage.st.text_input("Dosage31", value=str(row_data.get('Day31Dosage', '')))
        Day31Freq = Day31Freq.st.text_input("Frequency31", value=str(row_data.get('Day31Freq', '')))
        Day31Form = Day31Form.st.text_input("Form31", value=str(row_data.get('Day31Form', '')))
        Day31Route = Day31Route.st.text_input("Route31", value=str(row_data.get('Day31Route', '')))


        # Medication details section
        OTPName, OTPClinician, OTPphone= st.columns(3)
        OTPName = OTPName.st.text_input("OTPName", value=str(row_data.get('OTPName', '')))
        OTPClinician=OTPClinician.st.text_input("OTPClinician", value=str(row_data.get('OTPClinician', '')))
        OTPphone = OTPphone.st.text_input("OTPphone", value=str(row_data.get('OTPphone', '')))
        OTPAddress= st.text_input("OTPAddress", value=str(row_data.get('OTPAddress', '')))

        PharmacyName, PharmacyPhone = st.columns(2)
        PharmacyName=PharmacyName.st.text_input("PharmacyName", value=str(row_data.get('PharmacyName', '')))
        PharmacyPhone=PharmacyPhone.st.text_input("PharmacyPhone", value=str(row_data.get('PharmacyPhone', '')))

    

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

       #Function to submit form
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")
if __name__ == "__main__":
    main()
