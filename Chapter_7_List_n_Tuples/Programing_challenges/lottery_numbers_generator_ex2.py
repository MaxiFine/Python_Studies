# THIS PROGRAM GENERATES RANDOM NUMBERS AND PUT THE IN A LIST FORM
import random


def main():
    # Create a list and fill it 0's and later replace the values
    numbers = [0] * 7
    index = 0

    # the list with the random numbers
    while index < len(numbers):  # the while loop is the best to use to
        # iterate through a list and writes the item to its index
        # in the list
        numbers[index] = random.randint(0, 9)  # the random numbers will be
        # assigned to the index of the list to the last index in the list
        index += 1

    print("The random numbers are:", numbers)
    for item in numbers:
        print(item, ' ', end='')


main()
