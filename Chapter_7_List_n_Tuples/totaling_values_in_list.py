# THIS PROGRAM DEMONSTRATES THE TOTAL OF VALUES IN A LIST


def main():
    # Create a list
    numbers = [2, 4, 6, 8, 10]

    # Create a variable to use as an accumulator
    total = 0

    # Calculate the total of the list elements
    for value in numbers:  # this loop will iterate through the list to get
        # all values in the list for computations
        total += value

    # Display the total of the list elements
    print('The total of the elements is', total)


main()
