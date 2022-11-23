import sqlite3

def main():
    # Establish Data Connection and Cursor
    conn = sqlite3.connect('chocolates.db')
    cur = conn.cursor()  # Data Manipulator

    # Get the Minimum Price from the user
    while True:
        try:
            min_price = float(input("Enter the Minimum Price: "))

        except ValueError:
            print("Please enter Positive numbers only\n"
            "Greater than Zero. Please enter again.")

        else: 
            break

    # # User Input Validation Validate it later
    # while not min_price.isnumeric():
    #     print("Price cannot be zero or negative number.\n"
    #     "Enter Positive numbers only")

    #     min_price = input("Please enter the correct Input now: ")

    # # Conversion to desired data type Float
    # price = float(min_price)

    # Send the user input to the DBMS Using the SELECT statement
    cur.execute("""SELECT Description, RetailPrice FROM Chocolates WHERE
                RetailPrice >= ? """,(min_price,))

    # Fetch the results
    results = cur.fetchall()

    if len(results) > 0:
        # Display the results
        print("Here are the Results")
        print()
        print("Description \t\t     Price")
        print("-------------------------------------")
        for row in results:
            print(f'{row[0]:30} {row[1]: < 10}')

    else:
        print("No Products found.")

    # Close the database connection
    conn.close()

main()
