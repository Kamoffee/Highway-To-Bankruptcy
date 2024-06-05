# import csv
# import os

# # Input directory containing text files
# txt_dir = 'TXT'

# # Output CSV file
# csv_filename = 'output.csv'

# # Iterate over each text file in the input directory
# with open(csv_filename, 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
    
#     # Iterate over each file in the directory
#     for filename in os.listdir(txt_dir):
#         if filename.endswith('.txt'):  # Check if the file is a text file
#             txt_path = os.path.join(txt_dir, filename)
            
#             # Open the text file for reading
#             with open(txt_path, 'r') as txt_file:
#                 # Read each line and write it to the CSV file
#                 for line in txt_file:
#                     data = line.strip().split()  # Adjust parsing logic as needed
#                     writer.writerow(data)

# print(f"Conversion from text files in '{txt_dir}' to '{csv_filename}' is complete.")

# import pandas as pd
# import os

# def convert_text_to_csv(input_file, output_file):
#     """
#     Convert a text file to CSV format.

#     Args:
#     input_file (str): Path to the input text file.
#     output_file (str): Path to the output CSV file.
#     """
#     # Read text file
#     with open(input_file, 'r') as file:
#         text = file.read()

#     # Parse data (replace this with your actual parsing logic)
#     data = parse_text(text)

#     # Convert to DataFrame
#     df = pd.DataFrame(data)

#     # Write to CSV
#     df.to_csv(output_file, index=False)

# def parse_text(text):
#     """
#     Parse text data and extract relevant information.
    
#     Replace this function with your actual parsing logic.
#     """
#     # Example parsing logic
#     # Split text into lines
#     lines = text.split('\n')
    
#     # Extract relevant information
#     # (This is just a placeholder, replace with your actual parsing logic)
#     data = {'Date': ['2024-01-01', '2024-01-02'],
#             'Description': ['Transaction 1', 'Transaction 2'],
#             'Amount': [100.00, -50.00]}
    
#     return data

# # Directory containing text files
# directory = 'TXT'

# # Output directory for CSV files
# output_directory = 'CSV'

# # Loop through text files in the directory
# for filename in os.listdir(directory):
#     if filename.endswith(".txt"):
#         input_file = os.path.join(directory, filename)
#         output_file = os.path.join(output_directory, filename[:-4] + '.csv')  # Change file extension
#         convert_text_to_csv(input_file, output_file)


import csv

def convert_txt_to_csv(input_file, output_file):
    """
    Convert a text file to CSV format without parsing.

    Args:
    input_file (str): Path to the input text file.
    output_file (str): Path to the output CSV file.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for line in infile:
            # Write each line as a single field in the CSV file
            writer.writerow([line.strip()])

input_file = 'merged_file.txt'
output_file = 'file.csv'
convert_txt_to_csv(input_file, output_file)

