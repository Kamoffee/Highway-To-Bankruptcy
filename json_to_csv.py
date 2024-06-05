import os
import pandas as pd
import json

# Directory containing JSON files
json_dir = 'CSV'

# List to hold DataFrames of all JSON files
dfs = []

# Iterate over JSON files in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        json_path = os.path.join(json_dir, filename)
        with open(json_path, 'r') as file:
            json_data = json.load(file)
            df = pd.DataFrame(json_data)
            dfs.append(df)

# Concatenate all DataFrames into one
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a CSV file
csv_filename = 'merged_data.csv'
merged_df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' created successfully.")
