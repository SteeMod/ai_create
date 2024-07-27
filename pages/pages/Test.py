import csv, operator

# Open the CSV file
with open('out1.csv', 'r') as csvfile:
    # Read the CSV file
    data = csv.reader(csvfile)
    # Sort the data by the first column (change the index to sort by a different column)
    sorted_data = sorted(data, key=operator.itemgetter(0))  # Change 0 to the index of the column you want to sort by

# Print each row of the sorted data
for row in sorted_data:
    print(row)
