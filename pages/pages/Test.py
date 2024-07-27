import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv('latest.csv')

# Select the row, for example, the first row
row = df.iloc[31]

# Transpose the row
transposed_row = pd.DataFrame(row).transpose()

print(transposed_row)
