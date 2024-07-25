import pandas as pd

# Load the data from a CSV file
df = pd.read_csv('result_20240724195908.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Display the correlation matrix
print(correlation_matrix)
