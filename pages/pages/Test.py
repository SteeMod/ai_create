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
44,45,46]

# Select the values at these indices
selected_data = data[indices]

# Reshape the selected data to have two columns
# The number of rows will be determined by the number of elements in selected_data
reshaped_data = np.reshape(selected_data, (-1, 2))

# Convert the reshaped data back to a DataFrame
reshaped_df = pd.DataFrame(reshaped_data)

# Save the reshaped DataFrame to a new CSV file
reshaped_df.to_csv('reshaped_file.csv', index=False)

# Display the DataFrame in Streamlit
st.write(reshaped_df)
