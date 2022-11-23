import sqlite3

def main():
    conn = sqlite3.connect('chocolates.db')

    cur = conn.cursor()

    # Get the Minimum Price
    cur.execute('''SELECT MIN(RetailPrice) FROM Chocolates''')
    minPrice = cur.fetchone()[0]

    # Get the Maximum Price
    cur.execute('''SELECT Max(RetailPrice) FROM Chocolates''')
    highPrice = cur.fetchone()[0]

    # Get the average Price Of Product
    cur.execute('''SELECT AVG(RetailPrice) FROM Chocolates''')
    averagePrice = cur.fetchone()[0]


    # Display The Results
    print(f'Lowest Price: ${minPrice:.2f}')
    print(f'Highest Price: ${highPrice:.2f}')
    print(f'Average Price: ${averagePrice:.2f}')

    conn.close()


main()

