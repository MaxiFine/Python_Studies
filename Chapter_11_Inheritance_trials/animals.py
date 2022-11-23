# This is program is a demonstration of Polymorphism

# The Mammal Class represents a generic mammal

class Mammal:
    def __init__(self, species):
        self.__species = species

    # The show_species method displays a message indicating
    # the mammal's species

    def show_species(self):
        print('I am a', self.__species)

    # The make_sound method is the mammal's way of making a
    # generic sound

    def make_sound(self):
        print('Grrrrrrr!!!')


class Dog(Mammal):
    # The __init__ method calls the super class's
    # __init__ method passing 'Dog' as the species

    def __init__(self):  # The Dog inherits its attributes
        # from the Mammal Class
        Mammal.__init__(self, 'Dog')  # Initialization of the parent class for inheritance
        # for overriding the parent init method

    def make_sound(self):
        print('Woof! Woof!')


class Cat(Mammal):

    def __init__(self):
        Mammal.__init__(self, 'Cat')

    def make_sound(self):
        print('Meow! Meow!')



def main():
    # Create a Mammal object, a Dog object, a cat object
    mammal = Mammal('Regular Animal')

    dog = Dog()   # Creating a Dog object
    cat = Cat()   # Creating a cat object


    # Display information about each one.
    print('Here are some animals and \n'
          'the sound they make.')
    print('------------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)


# The show_mammal_info function accepts an object as an argument
# and calls its show_species and make_sound methods
def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


main()
