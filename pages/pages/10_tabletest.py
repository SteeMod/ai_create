# Creating a table in Python using PrettyTable library
from prettytable import PrettyTable

# Initialize the table
table = PrettyTable()

# Define the columns
table.field_names = ["Day1", "Day1 Yes", "Day1 No"]

# Add a row (example row, replace with actual data)
table.add_row(["Data for Day1", "Yes", "No"])

# Print the table
print(table)