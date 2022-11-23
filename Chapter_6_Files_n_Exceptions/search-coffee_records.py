# THIS PROGRAM ALLOWS THE USER TO SEARCH FOR FILES IN THE COFFEE.TXT
# FILE RECORDS FOR MATCHING A DESCRIPTION
# MODIFYING RECORDS DEMO

import os


def main():
    # create a boolean variable to use as your flag in the program
    found = False  # A flag

    # Get the search value from user
    search = input("Enter a description to search for: ")
    new_qty = float(input("Description: "))

    # open the original file coffee.txt
    coffee_file = open('coffee.txt', 'r')

    # open the temporary file
    temp_file = open('temp.txt', 'w')

    # read the first record's description field
    descr = coffee_file.readline()

    # read the reat of the file
    while descr != '':
        # read the quantity as well
        qty = float(coffee_file.readline())

        # strip the \n from the string
        descr = descr.rstrip('\n')

        # Write either this record to the temporary file
        # or the new record if this is the one that is to be modified
        if descr == search:
            # write the modified record to the temp file
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')

            # set flag to True
            found = True
        else:
            # Write the original record to the temp file
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

        # read the next description
        descr = coffee_file.readline()

    # Close the coffee file and the temporary file
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file
    #os.remove('coffee.txt')

    # Rename the temporary file
    #os.rename('temp.text', 'coffee.txt')

    # If the search value was not found in the
    # file Display a message
    if found:
        print("The file has been updated.")
    else:
        print("That item was not found in the file")


# call the main function
main()
