import re
import csv
lst = []
with open('merged_file.txt', 'r') as file:
    fhand = file.read()
    pattern = (r'\d{2}/\d{2}/\d{4}\s+[\w\s#-]+?\s-?\d+\.\d{2}' r'|'
     r'\d{2}/\d{4}\s+[\w\s#-]+?\s-?\d+\.\d{2}' r'|'
    r'\d{2}/\d{2}\s+[\w\s#-]+?\s-?\d+\.\d{2}')
    matches = re.findall(pattern, fhand)
    lst.extend(matches)

with open('converted_file.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['Date', 'Description', 'Amount'])
    # Extract the title of each column using another re to make sure is written in the right order
    for order in lst:
        order_pattern = re.match(r'(\d{2}/\d{2}/\d{4}|\d{2}/\d{4}|\d{2}/\d{2})\s+(.+?)\s(-?\d+\.\d{2})', order)
        if order_pattern:
            date, description, amount = order_pattern.groups()
            writer.writerow([date, description, amount])