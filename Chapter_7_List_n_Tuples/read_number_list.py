# This program reads numbers from a file into a list


def main():
    # Open a file for reading
    infile = open('numberslist.txt', 'r')

    # Read the contents of the file into a list
    numbers = infile.readlines()

    # Close file after reading
    infile.close()

    # Convert each element to an integer
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    # Display the contents of the list
    print(numbers)


main()
