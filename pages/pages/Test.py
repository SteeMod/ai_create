import pandas as pd
import streamlit as st

# Assuming df is your DataFrame
df = pd.read_csv('latest.csv')

# Split the dataframe into two dataframes at the 5th column index
df1 = df.iloc[:, :5]
df2 = df.iloc[:, 5:]

# Now you can display these dataframes
print(df1)
print(df2)
st.table(df1)
st.table(df2)
