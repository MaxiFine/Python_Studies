# This Program uses the WRITELINES method to
# save a list of strings toa file

#
# def main():
#     # Create a list of string
#     cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
#
#     # Open a file for writing
#     outfile = open('cities.txt', 'w')
#
#     # Write the list to the file
#     outfile.writelines(cities)
#
#     # Close after mode operation
#     outfile.close()
#
#
# main()


def for_loop_reading_list():  # this function will read
    # the lines of the file and prints it out

    # A list of string
    cities = ['New YOrk', 'Boston', "Atlanta", 'Dallas']

    # Read the list items from the file
    outfile = open('cities.txt', 'w')

    # write the list to the file
    for item in cities:
        outfile.write(item + '\n')

    # Close the file after operation
    outfile.close()


for_loop_reading_list()
