import streamlit as st
import pandas as pd

# Define the initial data
data = {'Day4': "", 'Day4Yes': "", 'Day4No': "", 'Day4Dosage': "", 'Day4Freq': "", 'Day4Form': "", 'Day4Route': ""}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data, index=[0])

# Create a function to display the DataFrame as an editable table in Streamlit
def dataframe_input(df):
    for i in range(df.shape[0]):
        cols = st.beta_columns(df.shape[1])
        for j in range(df.shape[1]):
            df.iloc[i, j] = cols[j].text_input(f"Row {i+1} Column {j+1} ({df.columns[j]})", df.iloc[i, j])
    return df

# Call the function
df = dataframe_input(df)

# Display the DataFrame
st.table(df)
