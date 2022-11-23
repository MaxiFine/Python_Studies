# This is a class for Pets with Animals


class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

        # Mutator methods to change data if necessary
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Accessor methods to access values that shall be stored in them
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    print('Welcome to Ady Pets Shop\n')
    name = input('Enter pet\'s name: ')
    animal_type = input('Enter type of animal: ')
    age = input('Enter age of animal: ')

    pet_details = Pet(name, animal_type, age)

    # Display the pet's details
    print()
    print('The name of the pet is', pet_details.get_name())
    print('Animal type is', pet_details.get_animal_type())
    print('Age of the pet is', pet_details.get_age())


if __name__ == '__main__':
    main()


