# This program reads a file contents into a list


def main():
    infile = open('cities.txt', 'r')

    # Read the contents of the file into a list
    cities = infile.readlines()

    infile.close()

    # Strip the \n character from each element
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    # Display the contents
    print(cities)


main()

