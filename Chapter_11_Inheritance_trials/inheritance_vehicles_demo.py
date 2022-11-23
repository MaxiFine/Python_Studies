# This Automobile class holds general data about
# an automobile in inventory


class Automobile:
    # The __init__ method arguments for the make,
    # model, mileage, and price. It initializes
    # the data attributes with these values
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # The following codes are the mutators methods for the class
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

        # Accessor methods for the class

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price


# The car class represents a car. It is a subclass
# of the Automobile class
class Car(Automobile):
    # The __init__ method accepts arguments for the car's make
    # model, mileage, price, doors
    def __init__(self, make, model, mileage, price, doors):
        # Call the superclasses __init__ method and pass the
        # required arguments. Note that we also have to pass self
        # as an argument
        Automobile.__init__(self, make, model, mileage, price)

        # After that initialize the new attribute of the car
        self.__doors = doors

    # The set_doors method is the mutator for the __doors attribute
    def set_doors(self, doors):
        self.__doors = doors

    # The Accessor method for the __door attribute
    def get_doors(self):
        return self.__doors


# The Truck class represents a pickup truck. It is a subclass of the Automobile class
class Truck(Automobile):
    # The __init__ Method accepts arguments for the Truck's make, model,
    # mileage, price and drive type

    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclass and pass the required arguments
        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the drive type attribute
        self.__drive = drive_type

    # Now create the accessor and mutator methods
    def set_drive_type(self, drive_type):
        self.__drive = drive_type

    def get_drive_type(self):
        return self.__drive


class SUV(Automobile):
    # The init method accepts arguments for the SUV's make, model,
    # mileage price and passenger capacity
    def __init__(self, make, model, mileage, price, pass_cap):

        # Now call the Superclass __init__ method and pass the required
        # arguments to them
        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the new attribute of the SUV class
        self.__pass_cap = pass_cap

    # Mutator methods for the
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # Accessor method
    def get_pass_cap(self):
        return self.__pass_cap

