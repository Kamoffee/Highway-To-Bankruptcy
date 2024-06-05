# import pdftables_api

# conversion = pdftables_api.Client('ngyrt22o5ehq')

# conversion.csv('amex.p.pdf','amex.p.csv')

import os
import pdfplumber
import pandas as pd

# Function to convert PDF to CSV
def pdf_to_csv(pdf_path, csv_path):
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages:
            tables.append(page.extract_table())
    
    # Concatenate all tables into one DataFrame
    df = pd.concat([pd.DataFrame(table) for table in tables])
    
    # Save as CSV
    df.to_csv(csv_path, index=False)

# Directory containing PDF files
pdf_dir = 'Raw_data'

# Directory to save CSV files
csv_dir = 'CSV'

# Iterate over PDF files in the directory
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, filename)
        csv_path = os.path.join(csv_dir, filename[:-4] + '.csv')  # Change extension to CSV
        pdf_to_csv(pdf_path, csv_path)
