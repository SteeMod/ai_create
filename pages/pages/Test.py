import pandas as pd
import streamlit as st
import os

# Open the CSV file
df = pd.read_csv('out1.csv')

# Select only columns with names containing 'Day' 'Yes' or 'Day' 'yes'
df = df[[col for col in df.columns if 'Day' in col and ('Yes' in col or 'yes' in col)]]

# Display the DataFrame
st.dataframe(df)
