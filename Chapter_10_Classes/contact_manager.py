# This Program manages conacts

import contact
import pickle

# Global constants
LOOK_UP = 1
ADD = 2
CHANGE = 4
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'contacts.dat'


def main():
    # Load the existing contact dictionary and
    # assign it to mycontacts
    my_contacts = load_contacts()

    # Initialize a variable for the user's choice
    choice = 0
    # Process menu selection util the user wants to quit the program
    while choice != QUIT:
        choice = get_menu_choice()

        # Process the choice
        if choice == LOOK_UP:
            look_up(my_contacts)

        elif choice == ADD:
            add(my_contacts)

        elif choice == CHANGE:
            change(my_contacts)

        elif choice == DELETE:
            delete(my_contacts)

    # Save the my_contacts dictionary to a file
    save_contacts(my_contacts)


def load_contacts():
    try:
        # Open the contacts.dat file
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary
        contact_dct = pickle.load(input_file)

        # Close the phone_inventory.dat file
        input_file.close()
    except IOError:
        # Could not open file so create an empty dictionary
        contact_dct = {}

        # Return the dictionary
        return contact_dct


# The get_menu_choice function display  the menu and gets a validated
# choice from the user
def get_menu_choice():
    print()
    print('Menu')
    print('-----------------------------')
    print('1. Look up a new contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()

    # Get the user's choice
    choice = int(input('Enter your choice: '))

    # Validate the choice
    while choice < LOOK_UP > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice
    return choice


# The look_up function looks up an item in the specified dictionary
def look_up(mycontacts):
    # Get a name to look up:
    name = input('Enter a name: ')

    # Look it up in the dictionary
    print(mycontacts.get(name, 'The name is not found'))


# The add function adds a new entry into the specified dictionary
def add(mycontact):
    # Get the contact info
    name = input('Name: ')
    phone = input('Phone: ')
    email = input("Email: ")

    # Create a contact object named entry to add the information
    entry = contact.Contact(name, phone, email)

    # If the name does not exit in the dictionary
    # add it as a key with the entry object as the associated value
    if name not in mycontact:
        mycontact[name] = entry
        print('The entry has been added')
    else:
        print('That name already exists')


# The change function changes an existing entry in the specified dictionary
def change(mycontact):
    # Get a name to look up for in the dictionary
    name = input('Enter a name: ')

    if name in mycontact:
        # Get a new contact details
        phone = input('Enter the new phone number: ')
        email = input('Enter the new email address: ')

        # Create a contact object name entry
        entry = contact.Contact(name, phone, email)

        # Update the entry
        mycontact[name] = entry
        print('Information updated successfully')


# The delete function deletes an entry from the specified dictionary
def delete(mycontact):
    # Get a name to look up
    name = input('Enter a name: ')

    # If the name is found, delete the entry
    if name in mycontact:
        del mycontact[name]
        print('Entry deleted')
    else:
        print('That name is not found')


# The save contact function pickles the specified object and
# saves it to the contacts file
def save_contacts(mycontact):
    # open the file for writing
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it
    pickle.dump(mycontact, output_file)

    # Close the file
    output_file.close()


main()
