import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('out1.csv')

# Convert the DataFrame to a 1D array
data = df.values.flatten()

# Select a range of values. For example, elements from index 10 to 71
selected_data = data[10:72]

# Reshape the selected data to have two columns
# The number of rows will be determined by the number of elements in selected_data
reshaped_data = np.reshape(selected_data, (-1, 2))

# Convert the reshaped data back to a DataFrame
reshaped_df = pd.DataFrame(reshaped_data)

# Save the reshaped DataFrame to a new CSV file
reshaped_df.to_csv('reshaped_file.csv', index=False)
