# This program depicts a car

BRAKE = -5
SPEED = 5


# Customer Class
class Customer:
    # Attributes of the Customer class
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Mutator Class
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    # Accessor Methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


# Car class
class Car:
    # Attributes of the car class
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # Mutator Methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    # Accessor Methods
    def get_name(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


# Constant for the sales tax rate
TAX_RATE = 0.05


# Service Quote Class
class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge

    # Mutator Methods
    def set_parts_charge(self, pcharge):
        self.__parts_charges = pcharge

    def set_labour_charge(self, lcharge):
        self.__labor_charges = lcharge

        # Accessor Methods
    def get_parts_charges(self):
        return self.__parts_charges

    def get_labour_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return self.__parts_charges * TAX_RATE

    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + \
               (self.__parts_charges * TAX_RATE)
