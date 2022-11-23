# THIS PROGRAM DEMONSTRATES HOW THE APPEND METHOD CAN
# BE USED TO ADD ITEM TO A LIST

def main():
    # Firs Create an empty list
    name_list = []

    # Create a variable to control the loop
    loop = 'y'

    # Add some names to the list
    while loop == 'y':
        # Get name from User
        name = input("Please enter a name: ")

        # Now append the name value to the list
        name_list.append(name)  # the syntax to append a list

        # Add another one
        print("Do you want to add another name? ")
        loop = input('y = yes, anything else = no: ')
        print()

    # Display the names that was entered
    print("Here are the names you entered")

    for name in name_list:
        print(name)

    print(name_list[0], name_list[1], name_list[2])


main()
