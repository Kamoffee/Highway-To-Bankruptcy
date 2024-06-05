import os
import json
import pytesseract
from pdf2image import convert_from_path

# Function to extract text from PDF using OCR
def extract_text_from_pdf(pdf_path):
    text = ''
    # Convert each page of the PDF to an image and extract text using OCR
    pages = convert_from_path(pdf_path)
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text

# Directory containing bank statement PDF files
pdf_dir = 'Raw_data'

# Directory to save JSON files
json_dir = 'CSV'

# Iterate over bank statement PDF files in the directory
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, filename)
        text = extract_text_from_pdf(pdf_path)
        # Save extracted text as JSON
        json_path = os.path.join(json_dir, filename[:-4] + '.json')  # Change extension to JSON
        with open(json_path, 'w') as json_file:
            json.dump(text, json_file, indent=4)
