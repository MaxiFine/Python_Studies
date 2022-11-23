# ACCOUNT VALIDATION PROGRAM


def main():
    # Open the file to read inputs from
    infile = open('charge_accounts.txt', 'r')

    # Reading the contents into a list
    account_list = infile.readlines()

    # Close file after mode operation
    infile.close()

    # Convert them into desired data types to work with and striping
    # the \n from it
    index = 0
    while index < len(account_list):
        account_list[index] = account_list[index].rstrip('\n')
        index += 1

    # print(account_list)

    # Get the item from user to search for
    search = input("Enter account number to validate: ")
    # Searching for the item in a list
    if search in account_list:
        print(search, "The Account number is found and valid")
    else:
        print(f"Account  Number {search} is not valid")


main()
