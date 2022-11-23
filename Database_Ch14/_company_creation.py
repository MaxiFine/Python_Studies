import sqlite3


def main():

    conn = sqlite3.connect('company.db')

    cur = conn.cursor()

    # Table Creation for the various Tables
    cur.execute('''CREATE TABLE IF NOT EXISTS Departments(
                DeptID INTEGER PRIMARY KEY NOT NULL,
                Department_Name TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Locations(Loc_ID INTEGER PRIMARY KEY NOT NULL,
                City TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Employees(
                Employ_ID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT,
                Position TEXT,
                DeptID INTEGER,
                Loc_ID INTEGER,
                FOREIGN KEY (DeptID) REFERENCES
                Departments (DeptID),
                FOREIGN KEY (Loc_ID) REFERENCES
                Locations (Loc_ID))''')


if __name__ == '__main__':
    main()