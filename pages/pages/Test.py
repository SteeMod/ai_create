import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv('out1.csv')

# Select specific columns
selected_columns = data[["Med3Check", "Med3Name", "Med3Dosage", "Med3Frequency", "Med3Form", "Med3Route", "Med3Instructions"]]

# Display the data in a table
st.table(selected_columns)
