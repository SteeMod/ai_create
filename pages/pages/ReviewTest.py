import streamlit as st
import pandas as pd

# Define row_data as an empty dictionary
row_data = {}

# Create columns in Streamlit
Day4, Day4Yes, Day4No, Day4Dosage, Day4Freq, Day4Form, Day4Route = st.columns(7)

# Get user input and store it in the dictionary
row_data['Day4'] = Day4.text_input("Day4")
row_data['Day4Yes'] = Day4Yes.text_input("Yes_4")
row_data['Day4No'] = Day4No.text_input("No_4")
row_data['Day4Dosage'] = Day4Dosage.text_input("Dosage_4")
row_data['Day4Freq'] = Day4Freq.text_input("Frequency_4")
row_data['Day4Form'] = Day4Form.text_input("Form_4")
row_data['Day4Route'] = Day4Route.text_input("Route_4")

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(row_data, index=[0])

# Display the DataFrame as a table in Streamlit
st.table(df)
