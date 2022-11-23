# This program tests the CellPhone Class

import cell_phone


def main():
    # Get the phone's data
    man = input('Enter phone\'s manufacturer: ')
    mod = input('Enter model number: ')
    retail = float(input('Enter retail price: '))

    # Create an instance the CellPhone class
    phone = cell_phone.CellPhone(man, mod, retail)

    # Display the data that was entered
    print('Here is the data you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price:', format(phone.get_retail_price(), ',.2f'), sep='')


if __name__ == '__main__':
    main()
