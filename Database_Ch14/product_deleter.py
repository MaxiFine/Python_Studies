import sqlite3


def main():
    # Connection of Database and Cursor
    conn = sqlite3.connect('chocolates.db')

    cur = conn.cursor()

    # Get a ProductID from the User
    pid = input('Enter a product ID to Delete: ')\

    # input validation
    while not pid.isdigit() or int(pid) < 1:
        error_msg()

        pid = input()

    id_num = int(pid)

    cur.execute("""SELECT Description FROM Chocolates
                   WHERE ChocoID == ?
                    """, (id_num,))

    # The Fetch Method returns None when the item does not Exist
    results = cur.fetchone()

    # The item is found, continue
    if results is not None:
        # Confirm user Deletion
        sure = input(f'Are your sure you want to delete '
                     f'{results[0]}? (y/n): ')

        # If so Delete the record
        if sure.lower() == 'y':
            cur.execute('''DELETE FROM Chocolates
                            WHERE ChocoID == ?''', (id_num,))

            # Commit the Changes
            conn. commit()
            print('The product was deleted.')

    else:
        # Error Message
        print(f'The Product ID {id_num} was not found')

    conn.close()


def error_msg():
    print("Please Enter Positive Integers only\n"
          "Enter the Correct Product ID now: ", end='')


if __name__ == '__main__':
    main()
