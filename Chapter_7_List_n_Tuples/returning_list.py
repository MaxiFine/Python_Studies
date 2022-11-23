# THIS PROGRAM USES A FUNCTION TO CREATE A LIST
# THE FUNCTION RETURNS A REFERENCE TO THE LIST

def main():
    # Get a list with values stored in it
    numbers = get_values()

    # Display the values in the list
    print('The numbers in the list are:')
    print(numbers)

    sums = 0
    average = 0

    for index in numbers:  # this block will get values in the list and add the numbers
        # together and calculates their average as well
        sums += index
        index += 1

    average = sums / len(numbers)
    print('The sum of the numbers is', sums)
    print("Average is", format(average, ',.2F'))


# The get_values functions gets a series of numbers from the user
# and stores them in a list. tht function returns a reference to the list
def get_values():
    # Create an empty list
    values = []

    # create a variable to control the loop
    again = 'y'

    # Get values from the user and add them to the list
    while again == 'y':
        # Get a number and add it to the list
        num = int(input('Enter a number: '))
        values.append(num)

        # Prompt user to enter number again
        print('Do you want to enter a number again?')
        again = input('y = yes, anything else = no: ')
        print()

    # Return the list
    return values


main()
