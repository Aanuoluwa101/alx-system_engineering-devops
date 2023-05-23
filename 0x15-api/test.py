#!/usr/bin/python3
import csv

data = {'Name': 'John', 'Age': 30, 'City': 'New York'}

# Specify the fieldnames to use as column headers, excluding the 'Age' key
fieldnames = [key for key in data.keys() if key != 'Age']

# Specify the path of the output CSV file
csv_file = 'output.csv'

# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the column headers
    writer.writeheader()

    # Write the dictionary values as a row, excluding the 'Age' key
    writer.writerow(data)

print("done")
