import pandas as pd
import numpy as np
import streamlit as st

# Load the CSV file
df = pd.read_csv('out1.csv')

# Specify the labels of the values you want to select
column_names = ['Day1', 'Day1Yes', 'Day1No', 'Day2', 'Day2Yes', 'Day2No']

# Select the rows with these labels
selected_data = df[df['column_names'].isin(column_names)]

# Reshape the selected data to have three columns
# The number of rows will be determined by the number of elements in selected_data
reshaped_data = np.reshape(selected_data.values, (-1, 3))

# Convert the reshaped data back to a DataFrame
reshaped_df = pd.DataFrame(reshaped_data)

# Save the reshaped DataFrame to a new CSV file
reshaped_df.to_csv('reshaped_file.csv', index=False)

# Display the DataFrame in Streamlit
st.write(reshaped_df)
