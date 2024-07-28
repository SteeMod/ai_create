import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv('out1.csv')

# Select specific columns
selected_columns = data[["Med1Check", "Med1Name", "Med1Dosage", "Med1Frequency", "Med1Form", "Med1Route", "Med1Instructions"]]

# Display the data in a table
st.table(selected_columns)
