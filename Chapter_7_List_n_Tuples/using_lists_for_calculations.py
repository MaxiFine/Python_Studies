# THIS PROGRAM CALCULATES THE GROSS PAY FOR EACH
# OF MEGAN'S BARISTAS, tried with exceptions value error


NUM_EMPLOYEES = 6  # CONSTANT FOR THE LIST SIZE


def main():
    try:
        # Create a list to hold employee hours
        hours = [0] * NUM_EMPLOYEES

        # Now each employee's hours worked
        for index in range(NUM_EMPLOYEES):  # this loop will get the values from the user
            # and puts the in the list
            print('Enter the hours worked by employee ',
                  index + 1, ': ', sep='', end='')

            hours[index] = float(input())  # this will get the values from the user

        # Get the hourly pay rate
        pay_rate = float(input('Enter the hourly pay rate: '))

        # Display each employee's gross pay
        for index in range(NUM_EMPLOYEES):
            gross_pay = hours[index] * pay_rate
            print("Gross pay for Employee ", index + 1, ': $',
                  format(gross_pay, ',.2f'), sep='')

    except ValueError:  # If the user should enter string instead of
        # number is handled by the code below
        print("You must Enter digits not letters")


main()
