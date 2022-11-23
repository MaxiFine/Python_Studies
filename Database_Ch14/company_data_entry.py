import sqlite3

def main():
    conn = None
    try:

        conn = sqlite3.connect('company.db')

        cur = conn.cursor()

        # Entry for the Department Table
        again = 'y'
        while again.lower() == 'y':

            dept_name = input("Please Enter Department's Name: ")

            cur.execute("""INSERT INTO Departments(
                        Department_Name)
                        VALUES(?)""",
                        (dept_name,))
            conn.commit()

            again = input("Enter another details? (y/n): ")

        # Enter for the Location Table
        again_loc = 'y'
        while again_loc.lower() == 'y':

            print("Please Enter Location's Name: ", end='')
            loc_name = input()
            cur.execute("""INSERT INTO Locations(City)
                            VALUES(?)""", (loc_name,))
            conn.commit()

            again_loc = input("Enter details again? (y/n): ")

        # Entry for the Employees Table
        again_emp = 'y'
        while again_emp.lower() == 'y':

            # Enabling of Primary Key Enforcement
            cur.execute('PRAGMA foreign_keys=ON')

            print("Please Enter Employees Details")
            emp_name = input("Name: ")
            emp_Posi = input("Position: ")
            dept_id = int(input("Department ID: "))
            loc_id = int(input("Location ID: "))
            cur.execute("""INSERT INTO Employees(Name, Position, 
                        DeptID, Loc_ID)
                        VALUES(?, ?, ?, ?)""",
                        (emp_name, emp_Posi, dept_id, loc_id))

            conn.commit()

            again_emp = input("Enter details again? (y/n): ")

    # except sqlite3.Error as err:
    #     print(err)

    except ValueError as err1:
        print(err1)

    finally:
        if conn != None:
            conn.close()


if __name__ == '__main__':
    main()
