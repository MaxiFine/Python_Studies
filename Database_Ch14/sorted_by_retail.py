import sqlite3

# THIS PROOGRAM DEMONSTRATES HOW TO SORT A RESULT 
# USING THE SELECT STATEMENT QUERY

def main():
    # Connect Database and Cursor
    conn = sqlite3.connect('chocolates.db')
    
    # For manipulation
    cur = conn.cursor()

    # Select all columns from each row from the Products table
    cur.execute('''SELECT Descr iption, RetailPrice 
                    FROM Chocolates ORDER BY RetailPrice''')

    results = cur.fetchall() # Fetcht the data and Print the results
    
    # Displaying the items 
    for row in results:  # 
        print(f"{row[0]:30} {row[1]:5}")

    cur.close()

main()
