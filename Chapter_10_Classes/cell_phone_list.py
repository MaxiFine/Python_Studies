# The program creates five Cellphone objects and stores them in a list

import cell_phone


def main():
    # Get a list of CellPhone containing 5 data objects
    phones = make_list()

    # Display the data in the list
    # the
    print('Here is the data you entered:')
    display_list(phones)

    for item in phones:
        print(item.get_retail_price())
    print()

    for item in phones:
        print(item.get_model())
    print()

    for item in phones:
        print(item.get_manufact())
    print()


# This make_list function gets data from the user for five phone.
# The function returns list of CellPhone objects containing the data
def make_list():
    # Create an empty list
    phone_list = []

    # Add five Cellphone objects to the list
    print('Enter data for five phones')
    for count in range(1, 6):
        # Get the phone data
        print('Phone number ' + str(count) + ':')
        man = input('Enter the manufacture: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the retail price: '))
        print()

        # Create a new CellPhone object in memory
        phone = cell_phone.CellPhone(man, mod, retail)

        # Add the object the list
        phone_list.append(phone)

    return phone_list


# The display_list function accepts a list containing CellPhone objects
# as an argument and displays the data stored in each object
def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()


main()
