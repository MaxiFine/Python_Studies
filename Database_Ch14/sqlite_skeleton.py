import sqlite3

# THIS IS A SKELETON OF A DATABSE IN PYTHON


def main():

    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()

    # Insert code here to perform operations on the database.
    # THESE ARE THE CODES FOR THE MANIPULATIONS OF THE DATABASE

    conn.commit()  #THE COMMIT SAVE THE CHANGES MADE TO THE DATABASE
    conn.close()  # CLOSES THE DATABASE AFTER USING

    # Execute the main function
if __name__ == '__main__':
    main()
