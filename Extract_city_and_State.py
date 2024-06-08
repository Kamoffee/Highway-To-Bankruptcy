import pandas as pd
import re

# Read the CSV file
df = pd.read_csv("converted_file.csv")


# Define a function to extract city and state from the Description
def extract_city_state(description):
    match = re.search(r'([A-Za-z]+)\s([A-Z]{2})\b', description)
    if match:
        city = match.group(1)
        state = match.group(2)
        description = description.replace(city, '').replace(state, '').strip()
        return city, state, description
    else:
        return None, None, description


# Apply function to the Description column and create new columns
df['City'], df['State'], df['Description'] = zip(*df['Description'].apply(extract_city_state))

# Make a new csv file with the new columns created
df.to_csv('plus_city_state.csv', index=False)
