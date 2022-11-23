import sqlite3

def main():
    # Loop-control variable
    again = 'y'

    while (again == 'y'):
        # Get the item ID, name, and price
        item_id = int(input('Item ID: '))
        item_name = input('Item Name: ')
        price = float(input("Price: "))

        # Add the item to the database
        add_item(item_id, item_name, price)

        # Add another item to the database
        again = input('Add another item? (y/n): ')

# The add_item function adds an item to the database
def add_item(item_id, name, price):
    # Initialize connection variable
    #conn = None

    try:
        # Connect to the Database
        conn = sqlite3.connect('inventory.db')

        cur = conn.cursor()

        # Perform the type of DBMS Operation
        # Add the item to the Inventory table
        cur.execute('''INSERT INTO Inventory (itemID, ItemName, Price)
                    VALUES(?,?,?)''', (item_id, name, price))

        cur.execute('''SELECT * From Inventory''')

        results = cur.fetchall()

        for row in results:
            print(f"{row[0]:3} {row[1]:3} {row[2]:5} ")

        # Commit the Changes
        conn.commit()

    except sqlite3.Error as err: 
            print(err)

    finally:
        # Close the connection
        if conn != None:
            conn.close()

main()
