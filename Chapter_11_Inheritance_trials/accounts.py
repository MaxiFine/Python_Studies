# The SavingsAccount class represents a savings accounts


class SavingsAccount:
    # Class Attributes
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__int_rate = int_rate
        self.__balance = bal

    # The following methods are for mutator and accessor methods for data
    # distribution

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_int_rate(self, int_rate):
        self.__int_rate = int_rate

    def set_bal(self, bal):
        self.__balance = bal

    def get_account_num(self):
        return self.__account_num

    def get_int_rate(self):
        return self.__int_rate

    def get_bal(self):
        return self.__balance


class CD(SavingsAccount)  #  The CD is inheriting from the Savings Account
    # Initializer for CD class attributes
    def __init__(self, account_num, int_rate, bal, mat_date):  # Mat_date is the unique
        # attribute for the  CD class

        # Calling the superclass __init__ method for the attributes
        SavingsAccount.__init__(self, account_num, int_rate, bal)

        # Initializer for the maturity date's unique attribute
        self.__maturity_date = mat_date

    # Mutator method
    def set_mat_date(self, mat_date):
        self.__maturity_date = mat_date

    # Accessor method
    def get_mat_date(self):
        return self.__maturity_date
