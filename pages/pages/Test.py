import streamlit as st
import pandas as pd

# Create an empty DataFrame with 7 columns
column_names = ["Day", "DayYes", "DayNo", "DayDosage", "DayFreq", "Day1Form", "Day1Route"]
df = pd.DataFrame(columns = column_names)

# Load the CSV data into the DataFrame
data = pd.read_csv('out1.csv')
for column in column_names:
    if column in data.columns:
        df[column] = data[column]

# Display the data in a table
st.table(df)
