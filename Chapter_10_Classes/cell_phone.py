# The CellPhone class holds data about a cell phone

class CellPhone:
    # The __init__ method initializes the attributes of the class
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.retail_price = price

    # The set_manufact method accepts an argument for
    # the phone's manufacturer
    def set_manufact(self, manufact):
        self.__manufact = manufact

    # The set_model method accepts an argument for the
    # phone's model number
    def set_model(self, model):  # Mutator methods
        self.__model = model

    # The set_retail price method accepts an argument for the phone's
    # retail price
    def set_retail_price(self, price):
        self.retail_price = price

    # The get_manufact, get-model, get_price methods returns
    # the phone's manufacturer, model and price
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.retail_price


