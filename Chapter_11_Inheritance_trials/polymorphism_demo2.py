# This program demonstrates polymorphism

import animals


def main():
    # Create an object, a Dog object, and a Cat object
    mammal = animals.Mammal("Regular Animal")

    # Creating objects from classes to work with
    dog = animals.Dog()
    cat = animals.Cat()

    # Display information about each one.
    print('Here are some animals and \n'
          'the sound they make.')
    print('------------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)


def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print("That's not a Mammal!")


if __name__ == '__main__':
    main()
