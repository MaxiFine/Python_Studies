# This program creates an instance of the SavingsAccount class
# and an instance of the CD account

import accounts


def main():
    # Get the account number, interest rate, and account balance for a
    # savings account
    print('Enter the following data for a savings account.\n')
    acc_num = input('Account number: ')
    int_rate = float(input('Interest rate: '))
    balance = float(input('Balance: '))

    # Create an instance of the SavingsAccount object
    savings = accounts.SavingsAccount(acc_num, int_rate, balance)

    # Get the account number, interest rate, account
    # balance, maturity date for a CD
    print('Enter the following data for CD\n')
    acct_num = input('Account number: ')
    inte_rate = float(input('Interest rate: '))
    balance = float(input('Balance: '))
    maturity = input('Maturity date: ')

    # Create an instance of the CD object
    cd = accounts.CD(acct_num, inte_rate, balance, maturity)

    # Display the data entered for the SavingsAccount object
    print('Here is the data you entered:')
    print()
    print('Savings Account')
    print('----------------------------')
    print("Account number:", savings.get_account_num())
    print('Interest rate:', savings.get_int_rate())
    print('Balance: $', format(savings.get_bal(), ',.2f'), sep='')
    print()

    # Display for the CD class data entered
    print('CD')
    print('---------------------------')
    print('Account number:', cd.get_account_num())
    print('Interest rate:', cd.get_int_rate())
    print('Balance: $', format(cd.get_bal(), ',.2f'), sep='')
    print('Maturity date:', cd.get_mat_date())


# Call the main function
if __name__ == '__main__':
    main()
