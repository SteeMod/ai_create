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

# Select only columns that contain the word 'Day'
day_columns = [col for col in df.columns if 'Day' in col]

# Sort these columns and update the DataFrame
df[day_columns] = df[day_columns].sort_index(axis=1)

# Display the data in a table
st.table(df)
