# This program assigns random numbers to a two-dimension list

import random

ROWS = 3
COLUMNS = 4


def main():
    # Create a two-dimensional list
    values = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]


    # Fill the list with random values
    for rows in range(ROWS):
        for columns in range(COLUMNS):
            values[rows][columns] = random.randint(1, 100)
            print(values[rows][columns])

    print(values)


main()
