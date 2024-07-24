import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('out1.csv')

# Select columns from 'Day1Yes' to 'Day31Yes'
selected_columns = df.loc[:, 'Day1Yes':'Day31Yes']

# Count 'Yes' entries for each day
yes_counts = selected_columns.apply(lambda x: (x == 'Yes').sum())

# Create a pie chart
plt.figure(figsize=(10, 6))
plt.pie(yes_counts, labels=yes_counts.index, autopct='%1.1f%%')
plt.title('Distribution of "Yes" Entries from Day1 to Day31')
plt.show()
