# This Program strengthens the understanding of list
# the same shall be done java as well


def main():
    print("Welcome to the List Manipulator\n"
          "Please Enter 10 numbers Below\n")

    user_numbers = get_numbers()

    print(user_numbers)

    print("Insertion of Exceptional numbers\nat Desired Positions")
    user_numbers.insert(user_numbers[-8], -20)
    print(user_numbers)
    user_numbers.insert(user_numbers[-3], 15)
    print(user_numbers)
    user_numbers.remove(user_numbers[1])
    print(user_numbers)
    user_numbers.insert(user_numbers[9], -30)
    print()

    print(user_numbers)
    print("Thank You!")


# def get_user_nums():  # This function will use the for loop
#     inputs = []
#
#     # Use a for loop to iterate the number of inputs
#     for item in range(1,11):
#
#         # Getting the user inputs
#         print("Please enter number #", item, ": ", sep='', end='')
#         user_num = input()
#
#         while not user_num.isdigit() or (int(user_num) < 0):
#             error_msg()
#             user_num = input()
#
#         convert = int(user_num)
#
#         # append the number to the list
#         inputs.append(convert)
#
#     return inputs


def get_numbers():  # This function will use the while loop

    inputs_list = [0] * 10

    index = 0
    while index < len(inputs_list):

        # Getting the user inputs
        print("Please enter number #", index + 1, ": ", sep='', end='')
        user_num = input()

        # Validation of user inputs
        while not user_num.isdigit() or int(user_num) < 0:
            error_msg()
            user_num = input()

        convert = int(user_num)

        inputs_list[index] = convert  # Replacement of elements in a list
        # using indexing method

        index += 1  # index counter

    return inputs_list


def error_msg():  # Function for Error message
    print("Numbers can be any number\n"
          "But not negative numbers or Strings\n"
          "Please enter the correct input: ", sep='', end='')


if __name__ == '__main__':
    main()
