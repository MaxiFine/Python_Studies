import sqlite3

# THIS PROGRAM WILL USE PARAMETERIZED QUERIES TO
# INSERT DATA INTO THE DATABASE AND MANIPULATE IT LATER

def main():
    # Establish Database Connection and Cursor
    conn = sqlite3.connect('chocolates.db')

    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Chocolates(
                ChocoID INTEGER PRIMARY KEY NOT NULL, Description TEXT,
                UnitCost REAL, RetailPrice REAL, UnitsOnHand INTEGER)''')

    # Filling table with data Using values of Variables
    again = 'y'  # Looper
    while again == 'y':
        # User inputs for database
        choco_des = input('Chocolate\'s Description: ')
        unit_price = float(input('Enter Price: '))
        retailPrice = float(input('Retail Price: '))
        units_left = int(input('Items on shelve: '))

        # Data insertion
        cur.execute('''INSERT INTO Chocolates(Description, 
                    UnitCost, RetailPrice, UnitsOnHand)
                VALUES(?, ?, ?, ?)''',
                (choco_des, unit_price, 
                retailPrice, units_left))

        conn.commit()  # Save changes to the database

        again = input('Add another item? (y/n): ')

    cur.execute("""SELECT * FROM Chocolates""")

    items = cur.fetchall()

    for row in items:
        print(f"{row[0]:6} {row[1]:35} {row[2]:5} {row[3]:5} {row[4]:5}")

    conn.close()  # Close after commiting changes to database

main()
