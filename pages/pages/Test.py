import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('out1.csv')

# Convert the DataFrame to a 1D array
data = df.values.flatten()

# Reshape the array to have 31 rows and 2 columns
reshaped_data = np.reshape(data, (31, 2))

# Convert the reshaped array back to a DataFrame
reshaped_df = pd.DataFrame(reshaped_data)

# Save the reshaped DataFrame to a new CSV file
reshaped_df.to_csv('reshaped_file.csv', index=False)
