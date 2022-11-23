import sqlite3

def main():
    conn = sqlite3.connect('chocolates.db')

    cur = conn.cursor()

    # SELECTION OF THE DATA FROM EVERY ROW
    cur.execute("SELECT * FROM Chocolates")

    # Fetch the data after the selection into a varible
    items = cur.fetchall()

    print("NumberID\t Name\t Price\tRetail Price\t Shelve")
    print('````````````````````````````````````````````````````')
    for row in items:
        print(f'{row[0]:3} {row[1]:30} {row[2]:5} {row[3]:5} {row[4]:5}')

    cur.close()


if __name__ == '__main__':
    main()
