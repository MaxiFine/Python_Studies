import sqlite3

def main():
    conn = None  # This technique enables database to be closed
    # after the database operations are performed

    try:
        conn = sqlite3.connect('company.db')

        cur = conn.cursor()

        # Enable foreign key enforcement
        cur.execute('PRAGMA foreign_keys=ON')

        # Retrieve employee names, departments, and cities
        cur.execute('''SELECT
                        Employees.Name,
                        Departments.Department_Name,
                        Locations.City
                       FROM 
                        Employees, 
                        Departments, 
                        Locations
                       WHERE 
                        Employees.DeptID == Departments.DeptID AND
                        Employees.Loc_ID == Locations.Loc_ID''')

        results = cur.fetchall()

        for row in results:
            print(f"{row[0]:15} {row[1]:25} {row[2]}")

    except sqlite3.Error as err:
        print(err)

    finally:
        # If the connection is open, close it
        if conn != None:
            conn.close()


if __name__ == '__main__':
    main()
