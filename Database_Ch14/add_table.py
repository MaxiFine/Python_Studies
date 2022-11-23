import sqlite3

def main():

    # Connect to the database
    conn = sqlite3.connect('inventory.db')

    # Get a cursor.
    cur = conn.cursor()

    # Add the inventory table
    cur.execute('''CREATE TABLE IF NOT EXISTS Inventory(
            ItemID INTEGER PRIMARY KEY NOT NULL,
                    ItemName TEXT,
                Price REAL) ''')

    # Commit the changes to the Database
    conn.commit()

    # Close after manipulation
    conn.close()

# Execute the main
main()
 