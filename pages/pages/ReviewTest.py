import streamlit as st
import pandas as pd

# Define the initial data
data = {'Day4': "", 'Day4Yes': "", 'Day4No': "", 'Day4Dosage': "", 'Day4Freq': "", 'Day4Form': "", 'Day4Route': ""}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data, index=[0])

# Use the experimental data editor to make the DataFrame editable
df = st.experimental_data_editor("Editable DataFrame", df)

# Display the DataFrame
st.table(df)
