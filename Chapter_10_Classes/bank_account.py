# THE BANK ACCOUNT CLASS SIMULATES A BANK ACCOUNT


class BankAccount:

    # The __init__ method accepts an argument for the account's balance.
    # It is assigned to the __balance attribute

    # The __init__ works as a Constructor
    def __init__(self, bal):  # Declaration of attributes to work with
        self.__balance = bal
        self.name = 'Maxwell'

    # The deposit method makes a deposit into the account
    def deposit(self, amount):  # Mutator Method
        self.__balance += amount

    # The withdrawal method withdraws an amount from the account
    def withdraw(self, amount):  # Mutator Method
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

    def get_balance(self):  # Accessor method
        return self.__balance


def main():
    # Get the Starting balance of the account
    start_balance = float(input('Enter your starting balance: '))

    # Create a BankAccount object
    savings = BankAccount(start_balance)

    # Deposit the user's paycheck
    pay = float(input('How much were you paid this week? '))
    print('Amount deposited into your account')
    savings.deposit(pay)

    # Display the balance now
    print('Your account balance is $', \
          format(savings.get_balance(), ',.2f'), sep='')

    # Get the amount to withdraw
    cash = float(input('How much do you want to withdraw? '))
    savings.withdraw(cash)

    # Display the balance
    print(savings.name, ' Your account balance is $', \
          format(savings.get_balance(), ',.2f'), sep='')


if __name__ == '__main__':
    main()
