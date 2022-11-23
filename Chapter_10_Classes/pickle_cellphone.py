# THIS PROGRAM PICKLES CELLPHONES OBJECTS

import pickle
import cell_phone


FILENAME = 'cellphone.dat'


def main():
    # Initialize a variable to control the loop
    again = 'y'

    # Open a file
    output_file = open(FILENAME, 'wb')

    # Get data from the user
    while again.lower() == 'y':
        # Get the cell phone data
        man = input('Enter Manufacturer: ')
        mod = input('Enter Model: ')
        retail = float(input('Enter retail price: '))

        # Create a CellPhone object
        phone = cell_phone.CellPhone(man, mod, retail)

        # Pickle the object and write it to the file
        pickle.dump(phone, output_file)

        # Get more cell phone data
        again = input('Enter more phone data? (y/n): ')

    # Close the file
    output_file.close()

    print('The data written to', FILENAME)


main()
