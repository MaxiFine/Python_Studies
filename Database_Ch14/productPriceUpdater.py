import sqlite3

def main():
    # Connect the Database
    conn = sqlite3.connect('chocolates.db')
    
    cur = conn.cursor()

    # Get a product ID from the User
    
    pid = input("Enter a product ID: ")

    # Input validation 
    while not pid.isdigit() or (int(pid) < 1):
        print("Please enter positive integers Only")

        pid = input("Enter Correct input now: ")

    item = int(pid)

    cur.execute('''SELECT Description, RetailPrice From Chocolates
                    Where ChocoID == ?''', (item,))

    results = cur.fetchone()

    # If the product ID was found, continue
    if results != None:
        # Print the current price
        print(f'The current price for {results[0]}'
                f'is ${results[1]:.2f}')

        # Get the new price 
        new_price = float(input('Enter the new price: '))

        # Update the price in the Product table
        cur.execute("""UPDATE Chocolates 
                        SET RetailPrice = ? 
                        WHERE ChocoID == ?
                    """, (new_price, item))

        # Commit the changes made
        conn.commit()
        print('The price was changed')
    else: 
        print(f'Product ID {item} not found')

    conn.close()

main()
