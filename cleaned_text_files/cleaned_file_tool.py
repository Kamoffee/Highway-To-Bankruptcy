# clean single file
def clean_single_file(input_file, output_file):
    with open('input_file', 'r') as file:
        read_file = file.read()
        clean_file = read_file.replace('\\n', '').replace('\\', '')
            
    with open('output_file', 'w') as new_file:
        new_file.write(clean_file)

