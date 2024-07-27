import pandas as pd
import streamlit as st
import os

# Open the CSV file
df = pd.read_csv('out1.csv')
    
    # Select the range 'Day1Yes' to 'Day31Yes' and transpose the DataFrame
df = df.loc[:, 'Day5Yes':'Day31Yes'].transpose()
    
    # Display the transposed DataFrame
st.dataframe(df)
