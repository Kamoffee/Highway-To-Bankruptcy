import pandas as pd
import sqlite3

# Read the CSV file into a DataFrame
df = pd.read_csv('plus_city_state.csv')

# Connect to sql database or create one if table doesn't exist
conn = sqlite3.connect('NextGen.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Trucker_expenses(
    Date TEXT,
    Description TEXT,
    Amount FLOAT,
    City TEXT,
    State TEXT
    )
''')

# Insert Data into the table
for index, row in df.iterrows():
    cur.execute('''
        INSERT INTO Trucker_expenses(Date, Description, Amount, City, State)
        VALUES(?, ?, ?, ?, ?) 
        ''', tuple(row))

# Commit the action
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
