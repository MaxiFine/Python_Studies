# This program gets employee data from the user and
# saves it as records in the employee.txt file.

def main():
    # Get the number of employee records to create.
    num_emps = int(input('How many employee records ' +
                         'do you want to create? '))

    # Open a file for writing.
    emp_file = open('employees.txt', 'w')

    # Get each employee's data and write it to
    # the file.
    for count in range(1, num_emps + 1):  # this code will loop the number
        # of employees data to be taken as entered by the user

        # Get the data for an employee.
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')  # takes the name of worker
        id_num = input('ID number: ')  # takes ID number of worker
        dept = input('Department: ')  # takes the department the worker belongs

        # Write the data as a record to the file.
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        # Display a blank line.
        print()  # this will create a space between records for easy reading

    # Close the file.
    emp_file.close()  # this will save anf close the file after mode opereation
    print('Employee records written to employees.txt.')

    main_read()


# This program displays the records that are
# in the employees.txt file.

def main_read():    # function to read the written mode operation
    # Open the employees.txt file.
    emp_file = open('employees.txt', 'r')
    # Read the first line from the file, which is
    # the name field of the first record.
    name = emp_file.readline()  # this will read the name field

    # USING THE WHILE LOOP SYNTAX TO READ THE DATA OF THE FILE
    # If a field was read, continue processing.
    while name != '':
        # Read the ID number field.
        id_num = emp_file.readline()

        # Read the department field.
        dept = emp_file.readline()

        # Strip the newlines from the fields.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Display the record.
        print('Name:', name)
        print('ID:', id_num)
        print('Dept:', dept)
        print()

        # Read the name field of the next record.
        name = emp_file.readline()

    # Close the file.
    emp_file.close()


# Call the main function.
main()
