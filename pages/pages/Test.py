import pandas as pd
import streamlit as st

# Assuming df is your DataFrame
df = pd.read_csv('latest.csv')

# Split the dataframe into two dataframes at the 31st to 100th and 101st to 150th column index
df1 = df.iloc[:, 30:100]  # Python uses 0-based indexing
df2 = df.iloc[:, 100:150]

# Now you can display these dataframes
print(df1)
print(df2)
st.table(df1)
st.table(df2)
