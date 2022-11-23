# THIS PROGRAM GERATES A RANDOM LIST AND A NUMBER AND PRINTS THE NUMBERS THAT
# ARE GREATER THAN THE NUMBER

import random


def main():
    # Create a list with elements and a random number
    random_number = random.randint(1, 15)
    random_list = [0] * 15

    # Generate random numbers to fill the list
    index = 0
    while index < len(random_list):
        random_list[index] = random.randint(1, 15)
        index += 1

    print("The random number is", random_number)
    print(random_list)

    get_total = random_function(random_number, random_list)

    print(get_total)


def random_function(rand_number, rand_list):  # a number and a list
    # are passed as the arguments to the function

    great_numbers = []  # and empty list to keep the numbers that shall
    # be greater than the random number

    for index in rand_list:  # for every item in the list
        if rand_number < index:  # check whether it is greater than the random number
            great_numbers.append(index)  # if true add it to the list

    return great_numbers


main()
