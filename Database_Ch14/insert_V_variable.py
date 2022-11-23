import sqlite3

# THIS PROGRAM DEMONSTRATE HOW TO USE PYTHON TO ADD DATA
# TO A TABLE USING VALUES A VARIABLE

def main():
    # Loop-control Variable
    again = 'y'

    # Connect the database
    conn = sqlite3.connect('Inventory.db')

    # Get a Cursor
    cur = conn.cursor()  # Use the sql object to create the cursor Object

    while again == 'y':
        # Get the item's name and Price
        item_name = input('Item name: ')
        price = float(input('Price: '))

        cur.execute('''INSERT INTO Inventory(itemName, Price)
                    VALUES(?, ?) ''',
                    (item_name, price))


        # Add Another data to the Table
        again = input('Add another item? (y/n): ')

    cur.execute('SELECT * FROM Inventory')

    results = cur.fetchall()  # getting all data inserted so far

    for row in results:
        print(f'{row[0]:5} {row[1]:15} {row[2]:5}')

    # Commit the changes to the database
    conn.commit

    # Close after manipulation
    conn.close()

if __name__ == '__main__':
    main()
