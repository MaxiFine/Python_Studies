import sqlite3

# Global Variables
MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5


def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()

        elif choice == READ:
            read()

        elif choice == UPDATE:
            update()

        elif choice == DELETE:
            delete()


def display_menu():
    print('\n----- Inventory Menu -----')
    print('1. Create a new Item')
    print('2. Read an Item')
    print('3. Update an  Item')
    print('4. Delete an Item')
    print('5. Exit the Program')


# Get get_menu_choice function gets the user's menu choice
def get_menu_choice():
    # Get the user's choice
    choice = input('Enter your choice: ')

    # User input validation to ensure accurate input
    while not choice.isdigit() or int(choice) < 1:
        print("Please enter Positive numbers only.: ", end='')

        choice = input()

    rChoice = int(choice)

    # Validation of input within program range
    while rChoice < MIN_CHOICE or rChoice > MAX_CHOICE:
        print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}')

        rChoice = int(input("Enter Correct Choice: "))

    return rChoice


def create():
    print('Create a new Item')
    name = input('Item Name: ')
    price = input('Price')
    insert_row(name, price)


def read():
    name = input('Enter an item name to search for: ')
    num_found = display_item(name)
    print(f'{num_found} row(s) found')


# The update function updates an existing item's data
def update():
    # First let the user search for the row
    read()

    # Get the ID of the selected item 
    selected_id = int(input("Select an ID: "))

    # Get the new values for item name and price
    name = input('Enter the item name: ')
    price = input('Enter the new price: ')

    # Update the row
    num_updated = update_row(selected_id, name, price)
    print(f'{num_updated} row(s) updated.')


def delete():
    # First let the user search for the row
    read()

    # Get the ID of the Selected item
    selected_id = int(input("Select an item to delete: "))

    # Confirm the deletion
    sure = input('Are you sure you want to delete this item? (y/n): ')
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} row(s) deleted.')


def insert_row(name, price):
    conn = None

    try:
        conn = sqlite3.connect('Inventory.db')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                    VALUES (?, ?)''', (name, price))

        conn.commit()
    except sqlite3.Error as err:
        print('Database Error', err)

    finally:
        if conn != None:
            conn.close()


# The display_item function displays all items
# with a matching ItemName
def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('Inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Inventory
                        WHERE lower(ItemName) == ?''',
                    (name.lower(),))
        results = cur.fetchall()

        for row in results:
            print(f"ID: {row[0]:<3} Name: {row[1]:<15}"
                  f"Price: {row[2]:<6}")
    except sqlite3.Error as err:
        print('Database Error ', err)

    finally:
        if conn != None:
            conn.close()

    # Return the number of Matching rows
    return len(results)


# The update_row function updates an existing row with a new
# ItemName and Price. The number of rows updated is returned
def update_row(id, name, price):

    conn = None

    try:
        conn = sqlite3.connect('Inventory.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Inventory
                        SET ItemName = ?, Price = ?
                        WHERE ItemID == ?''',
                    (name, price, id))
        conn.commit()
        num_updated = cur.rowcount

    except sqlite3.Error as err:
        print('Database Error', err)

    finally:
        if conn != None:
            conn.close()

    return num_updated


# The delete_row function deleted an existing item
# The number of rows deleted id returned
def delete_row(id):
    conn = None

    try:
        conn = sqlite3.connect('Inventory.db')
        cur = conn.cursor()

        cur.execute('''DELETE FROM Inventory
                    WHERE ItemID == ?''',
                    (id,))
        # Commit the Changes made
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)

    finally:
        if conn != None:
            conn.close()

    return num_deleted


if __name__ == '__main__':
    main()
