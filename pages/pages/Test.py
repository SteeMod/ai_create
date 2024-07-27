import pandas as pd
import numpy as np
import streamlit as st

# Load the CSV file
df = pd.read_csv('out1.csv')

# Convert the DataFrame to a 1D array
data = df.values.flatten()

# Specify the indices of the values you want to select
indices = [30,31,32,
37,38,39,
44,45,46,
51,52,53,
58,59,60,
65,66,67,
72,73,74,
79,80,81,
86,87,88,
93,94,95,
100,101,102]


# Select the values at these indices
selected_data = data[indices]

# Reshape the selected data to have three columns
# The number of rows will be determined by the number of elements in selected_data
reshaped_data = np.reshape(selected_data, (-1, 3))

# Convert the reshaped data back to a DataFrame
reshaped_df = pd.DataFrame(reshaped_data)

# Save the reshaped DataFrame to a new CSV file
reshaped_df.to_csv('reshaped_file.csv', index=False)

# Display the DataFrame in Streamlit
st.write(reshaped_df)
