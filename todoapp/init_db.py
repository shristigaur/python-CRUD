import sqlite3

# Connect to database (creates file if it doesn't exist)
connection = sqlite3.connect('database.db')

# Create table
connection.execute('''
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    done INTEGER DEFAULT 0
)
''')

connection.commit()
connection.close()

print("Database created successfully!")