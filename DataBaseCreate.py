import sqlite3

# Open a connection to the SQLite database
connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()

# Create the contacts table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone_number TEXT)")

# Insert the contacts into the table
contacts = [
    ("John Doe", "1234567890"),
    ("Jane Smith", "9876543210"),
    ("Michael Johnson", "5551234567"),
    ("Emily Brown", "1112223333"),
    ("David Wilson", "4445556666"),
    ("Olivia Davis", "8889990000"),
    ("William Taylor", "7776665555"),
    ("Sophia Anderson", "2223334444"),
    ("Liam Martinez", "9998887777"),
    ("Emma Thomas", "6667778888")
]
cursor.executemany("INSERT INTO contacts VALUES (?, ?)", contacts)

connection.commit()
connection.close()

print("contacts.db file created successfully.")
