import pandas as pd
import streamlit as st
import os

# Open the CSV file
df = pd.read_csv('out1.csv')

# Select only columns with names containing 'Day' 'Yes' or 'Day' 'yes'
df = df[[col for col in df.columns if 'Day' in col and ('Yes' in col or 'yes' in col)]]

# Transpose the DataFrame
df = df.transpose()

# Sort the DataFrame by column names
df = df.sort_index(axis=1)

# Display the DataFrame
st.dataframe(df)
