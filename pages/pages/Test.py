import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt

# Open the CSV file
df = pd.read_csv('out1.csv')

# Select only columns with names containing 'Day' 'Yes' or 'Day' 'yes'
df = df[[col for col in df.columns if 'Day' in col and ('Yes' in col or 'yes' in col)]]

# Transpose the DataFrame
df = df.transpose()

# Sort the DataFrame by column names
df = df.sort_index(axis=1)

# Rename the first column to 'Yes'
df.rename(columns={df.columns[0]: 'Yes'}, inplace=True)

# Display the DataFrame
st.dataframe(df)

# Count the rows where 'Yes' is ':selected:'
numerator = df[df['Yes'] == ':selected:'].shape[0]

# Get the total row count
denominator = df.shape[0]

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie([numerator, denominator - numerator], labels=['Selected', 'Not Selected'], autopct='%1.1f%%')
plt.title('Pie Chart of Selected vs Not Selected')
st.pyplot(plt.gcf())
