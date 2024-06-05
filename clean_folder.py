from pathlib import Path

def clean_files_in_folders(source_file, destination_file):
    # Create Path objects for input and output folders
    input_folder = Path(source_file)
    output_folder = Path(destination_file)

    # Create the output folder if it doesn't exist(parents: create parent dir if doesn't exits, exit_ok: handling errors)
    output_folder.mkdir(parents=True, exist_ok=True)

    # Iterate through each file in the input folder(iterdir(returns an iterator over the files in the dir)
    for file_path in input_folder.iterdir():
        if file_path.is_file():
            # Read the content of the file
            with open(file_path, 'r') as file:
                file_content = file.read()

            # Remove newline and other impurities from the text 
            clean_files = file_content.replace('\\n', ' ').replace('\\', ' ')

            # Write the cleaned content to a new file(combines the output_folder with the filename to create the output file path)
            output_file_path = output_folder / file_path.name
            with open(output_file_path, 'w') as cleaned_file:
                cleaned_file.write(clean_files)

source_folder = 'TXT'
destination_folder = 'cleaned_text_files'
clean_files_in_folders(source_folder, destination_folder)

