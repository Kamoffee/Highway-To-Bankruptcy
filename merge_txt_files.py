import os

def merge_text_files(input_dir, output_file):
    """
    Merge multiple text files into one big file.

    Args:
    input_dir (str): Path to the directory containing text files.
    output_file (str): Path to the output merged text file.
    """
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):
                with open(os.path.join(input_dir, filename), 'r') as infile:
                    outfile.write(infile.read())


input_directory = 'cleaned_text_files'
output_file = 'merged_file.txt'
merge_text_files(input_directory, output_file)