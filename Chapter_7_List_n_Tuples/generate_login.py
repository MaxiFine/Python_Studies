# this program gets the user's fname, lname,
# and ID number to generate a system login

import general_login


def main():
    # Get the details from the user
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    id_num = input("Enter your Students Id number: ")

    # Get the login name
    print('Your system login is:')
    print(general_login.get_login_name(first, last, id_num))


main()
