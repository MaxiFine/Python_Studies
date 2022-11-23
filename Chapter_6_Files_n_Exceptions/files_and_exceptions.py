# # THIS PROGRAM SHOWS HOW TO OPEN AN OUTPUT FILE,
# # WRITE DATa TO IT AND THEN CLOSES IT
#
#
# def main():
#
#     # creating a file named philosophers.txt
#     outfile = open('philosophers.txt', 'w')
#
#     # write=ing data to the file
#     outfile.write('John Locke\n')
#     outfile.write('Edmond Hume\n')
#     outfile.write('Davis Burke\n')
#     outfile.write('Maxwell is a Great Programmer...\n')
#     outfile.write("Try without escape sequence \n")
#
#     # closing the file after writing
#     outfile.close()
#
#
# # calling the main to execute the code
# main()
#


# # THE CODE BELOW READS THE CONTENT OF A FILE


# def main():
#
#     # syntax for opening a text file
#     infile = open('philosophers.txt', 'r')
#
#     # reading the text file contents
#     # create a variable to hold the opened file being read
#     file_contents = infile.read()
#
#     # close after reading
#     infile.close()
#
#     # print the data that was read
#     print(file_contents)
#     print('Hi reading the written file, fun!')
#
#
# # call the main to run to print
# main()
#
# # THIS CODE READS THE LINES OF THE FILE
#
#
# def main():
#     # opening the file
#     infile = open('philosophers.txt', 'r')
#
#     # read the lines from the file
#     line1 = infile.readline()
#     line2 = infile.readline()
#     line3 = infile.readline()
#     line4 = infile.readline()
#
#     # close the file after reading
#     infile.close()
#
#     # Displaying the file that was read into memory
#     print(line1)
#     print(line2)
#     print(line3)
#     print(line4)
#
#
# main()


# CONCATENATING A NEWLINE TO A STRING
# THIS PROGRAM GET 3 INPUTS FROM THE USER AND WRITES THEM TO A FILE
# READS THE DATA IN LINE, STRIPS THE \N FROM THE STRING AND PRINTS IT OUT AGAIN

#
# def main():
#     # get the names
#     print("Name 3 of your friends.")
#     name1 = input('Name 1: ')
#     name2 = input('Name 2: ')
#     name3 = input('Name 3: ')
#
#     # create/open a file to write the data to it
#     myfile = open('friends.txt', 'w')
#
#     # writing the data to the file
#     myfile.write(name1 + '\n')
#     myfile.write(name2 + '\n')
#     myfile.write(name3 + '\n')
#
#     # close the file after writing
#     myfile.close()
#
#     # showing the content and reading the file
#     file_content = open('friends.txt', 'r')
#     show_content1 = file_content.readline()
#     show_content2 = file_content.readline()
#     show_content3 = file_content.readline()
#
#     # STRIPING THE ESCAPE CHARACTER FROM THE STRING
#     strip1 = show_content1.rstrip('\n')
#     strip2 = show_content2.rstrip('\n')
#     strip3 = show_content3.rstrip('\n')
#
#     # close the file after performing mode on the
#     # file and displaying it
#     file_content.close()  # closing is not necessary though because
#     # the file is stored in a variable already
#
#     print("The content of the file is written to the friends.txt")
#     print("reviewing the info writing")
#     print('\nUnstrapped Characters')
#     print(show_content1)
#     print(show_content2)
#     print(show_content3)
#     print("The Striped character")
#     print(strip1)
#     print(strip2)
#     print(strip3)
#
#
# main()

#   # NUMERICAL FILES AND ITS SYNTAX OPERATIONS
#
# def main():
#     # open a file for writing
#     outfile = open('numbers.txt',  'w')
#
#     # getting inputs from the user
#     num1 = int(input("Enter number: "))
#     num2 = int(input("Enter another number: "))
#     num3 = int(input("Enter another number: "))
#
#     # writing the data to the lines of the file
#     outfile.write(str(num1) + '\n')
#     outfile.write(str(num2) + '\n')
#     outfile.write(str(num3) + '\n')
#
#     # striping the escape character from the number before displaying it
#     # closing the file after the write mode operation on the file
#     outfile.close()
#
#     # Displaying the data with the stripped ones.
#     print(num1)
#     print(num2)
#     print(num3)
#     print("That was fun!")
#
#
# main()


# # PERFORMING COMPUTATIONS IN A FILE
# # THIS PROGRAM DEMONSTRATES HOW NUMBERS
# # THAT ARE READ FROM A FILE MUST BE CONVERTED
# # FROM STRINGS BEFORE THEY ARE USED IN A MATH OPERATION
#
#
# def main():
#     # open the file for reading
#     infile = open('numbers.txt', 'r')
#
#     # read the lines of data from the file
#     line1 = int(infile.readline())
#     line2 = int(infile.readline())
#     line3 = int(infile.readline())
#
#     # close the file after mode operation
#     infile.close()
#
#     # performing computations on the file
#     adding = line1 + line2 + line3
#
#     # another computation
#     multiply = line1 * line2 * line3
#
#     # Displaying the output
#     print("The sum of the numbers is: ", format(adding, ',.2f'), sep='')
#     print("The product of the data is: ", format(multiply, ',.2f'), sep='')
#
#
# main()

# # USING LOOPS TO PROCESS FILES. THIS PROGRAM WROTE DATA TO A FILE,
# # READ IT AGAIN MADE COMPUTATIONS TO IT AND DISPLAYED THE OUTCOME
#
#
# def main():
#     # Get number of days from the user
#     num_days = int(input("Please enter the number of days: "))
#
#     # Create a file to write the data to it
#     sales_file = open('sales.txt', 'w')
#
#     # using a loop, get the sales made for each day
#     for count in range(1, num_days + 1):
#         # get the sales made in day
#         sales = float(input("Enter sales for day " + str(count) + ": "))
#
#         # write the data to the file after every loop
#         sales_file.write(str(sales) + '\n')
#
#     # close file after writing the data
#     sales_file.close()
#     print("Data is written to the file, open and read to perform desired operation...")
#
#     # this continuation is to read the data and display it
#     read_n_print = open('sales.txt', 'r')  # the file is open for reading
#
#     # note that the data read are now formatted as an int data type
#     line1 = float(read_n_print.readline())
#     line2 = float(read_n_print.readline())
#     line3 = float(read_n_print.readline())
#     line4 = float(read_n_print.readline())
#     line5 = float(read_n_print.readline())
#
#     # close file after data loss
#     read_n_print.close()
#
#     # performing a computation with the data entered after reading
#
#     total_sales = line1 + line2 + line3 + line4 + line5
#     print("Total Sales made within five days is $", format(total_sales, ',.2f'), sep='')
#
#
# main()


# THIS PROGRAM READS ALL THE VALUES IN THE SALES.TXT
# AND DISPLAYS THE DATA READ FROM THE FILE USING THE WHILE LOOP


def main():
    # open the sales.txt file and read it
    read_data = open('sales.txt', 'r')

    # reading the first line of data to test for an empty string
    line = read_data.readline()

    # testing for an empty string as long as an empty string is not
    # returned from readline, continue processing
    while line != '':
        # format the line to numerical data type
        amount = float(line)

        # print after formatting data
        print(format(amount, ',.2f'))

        # read the next line
        line = read_data.readline()

    # close file after reading the data
    read_data.close()


main()

# # USING THE FOR LOOP TO READ FILES
#
# def main():
#
#     total = 0.0  # accumulator
#
#     # open the file as usual
#     for_loop_demo = open('sales.txt', 'r')
#
#     # set the for loop to read the files
#     for line in for_loop_demo:  # iterate through the lines of data in the sales file
#         # convert the data to numerical data
#         data = float(line)
#
#         # format and display the data read from the file
#         print(format(data, ',.2f'))
#
#         # performing computations on files
#         total += float(line)
#     print("The sum is $", format(total, ',.2f'), sep='')
#
#     # close after all data is read from the file
#     for_loop_demo.close()
#
#
# main()
