# THIS PROGRAM ADDS COFFEE INVENTORY RECORDS TO THE COFFEE.TXT FILE


def main():
    # create a variable to control loop
    looper = 'Y'

    # create the coffee.txt file with the append mode operation
    coffee_file = open('coffee.txt', 'a')

    # Add some records to the file
    while looper.upper() == 'Y':
        # Get the coffee records data
        print("Enter the following coffee data:")
        description = input("Description: ")
        quantity = float(input("Quantity (in pounds): "))

        # Append the data to the coffee file
        coffee_file.write(description + '\n')
        coffee_file.write(str(quantity) + '\n')

        # Determine whether the user wants to add more records
        print("Do you want to enter data again?")
        looper = input("Enter Y = 'yes' or N = 'no' to Quit: ")

    coffee_file.close()
    print("Data successfully written to the file")
    print("\n\t Now let's read the files ")

    # Call the display function to display it
    read_function()


# this function will read data written to the coffee
# file and display it to the user
def read_function():
    # so we'll open the file to start working with it
    read_coffee = open('coffee.txt', 'r')

    # read the first record's description
    describe = read_coffee.readline()

    # now read the rest of the files, using loop to test
    # first if not empty string
    while describe != "":
        quanty = float(read_coffee.readline())

        # Strip the \n from the records for proper display
        describe = describe.rstrip('\n')

        # Display the Records
        print('Description:', describe)
        print("Quantity:", quanty)

        # read the next description to continue loop
        describe = read_coffee.readline()

    read_coffee.close()


main()
