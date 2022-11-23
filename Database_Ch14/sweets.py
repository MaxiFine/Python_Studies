import sqlite3


def main():

    # Create a database connection
    conn = sqlite3.connect('sweet_choco.db')

    # Create a cursor object
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Products
                (ProductID INTEGER PRIMARY KEY NOT NULL, 
                Description TEXT, UnitCost REAL, 
                RetailPrice REAL,
                UnitsOnHand INTEGER)''')

    cur.execute('''INSERT INTO Products(Description, UnitCost, RetailPrice, UnitsOnHand)
                VALUES("Dark Chocolate Bar", 2.99, 5.99, 197)''')

    cur.execute('''INSERT INTO Products(Description, UnitCost,
                RetailPrice, UnitsOnHand)
                VALUES("Medium Dark Chocolate Bar", 2.99, 5.99, 406),
                ("Milk Chocolate Bar", 2.99, 5.99, 266),
                ("Chocolate Truffles", 5.99, 11.99, 398),
                ("Chocolate Caramel Bar", 3.99, 6.99, 272),
                ("Chocolate Raspberry Bar", 3.99, 6.99, 363),
                ("Chocolate and Cashew Bar", 4.99, 9.99, 325),
                ("Hot Chocolate Mix", 5.99, 12.99, 222),
                ("Semisweet Chocolate Chips", 1.99, 3.99, 163),
                ("Semisweet Chocolate Pops", 1.99, 3.99, 163),
                ("White Chocolate Chips", 1.99, 3.99, 293)''')

    cur.execute('''SELECT * FROM Products''')

    products = cur.fetchall()

    # Displaying the items from the database
    print("Choco Name\t Cost\t  \t Retail Price \tShelf Number\n"
          "-----------------------------------------------------------")
    for var in products:
        print(f"{var[0]:5} {var[1]:35} {var[2]:5} {var[3]:5} {var[4]:5}")

    # # Commit the changes
    # conn.commit()  # Commit is more necessary when changes are made to the
    # Database

    # Close the database after manipulation
    conn.close()


main()
