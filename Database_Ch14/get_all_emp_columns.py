import sqlite3

# This Program demonstrates a menu-driven Program to
# Display Tables of the Company Database

DEPT_TABLE = 1
LOC_TABLE = 2
EMP_TABLE = 3


def main():
    # Display the Menu
    choice = display_msg()

    # Decide on the User's Selection
    if choice == DEPT_TABLE:
        print("Department_ID \t\t  Department_Name")
        print("---------------------------------------------")
        dept_table()

    elif choice == LOC_TABLE:
        print("Location_ID  \t\t   Location_Name")
        print("-----------------------------------------------")
        loc_table()

    elif choice == EMP_TABLE:
        print("Employee_ID \t   Name \t     Position \t     "
              "Dept_ID     \t  Loc_ID      ")
        emp_table()


def display_msg():

    print()
    print("--- Database Preview Operator ---")
    print("1. Department Table\n"
          "2. Location Table\n"
          "3. Employment Table\n")
    print("Please Enter Operation to Perform: ", end='')

    choice = input()

    while not choice.isdigit():
        print("Enter Numbers from 1-3 only \n"
              "Please enter correct input Only: ", end='')

        choice = input()

    item = int(choice)

    return item


def dept_table():

    conn = None

    try:
        conn = sqlite3.connect('company.db')

        cur = conn.cursor()

        cur.execute('''Select * From Departments''')

        results = cur.fetchall()

        for row in results:
            # Please Remember to print Columns to print Data into
            print(f"{row[0]:3} \t\t {row[1]:20}")

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()


def loc_table():
    # Please remember to add Columns to print data into
    conn = None

    try:

        conn = sqlite3.connect('company.db')

        cur = conn.cursor()

        cur.execute('Select * From Locations')

        result = cur.fetchall()

        for row in result:
            print(f"{row[0]:3} \t\t {row[1]:10}")

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()


def emp_table():

    conn = None

    try:

        conn = sqlite3.connect('company.db')

        cur = conn.cursor()

        cur.execute('Select * From Employees')

        result = cur.fetchall()

        for row in result:
            print(f"{row[0]:3} \t {row[1]:20} \t {row[2]:15} \t {row[3]:3} \t"
                  f"{row[4]:3}")

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()


if __name__ == '__main__':
    main()
