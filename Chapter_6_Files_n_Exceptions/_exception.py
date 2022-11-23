# # THIS PROGRAM DISPLAYS THE TOTAL OF THE
# # AMOUNTS IN THE SALES_DATA FILE
#
#
# def main():
#     total = 0  # Accumulator for accumulating total
#
#     try:
#         # open the sales_data.txt file
#         infile = open('sales.txt' 'r')
#
#         # Read values and add the data
#         for line in infile:  # loops through the file
#             amount = float(line)  # gets the data, converts to numerical values
#             total += amount  # accumulates the values here
#
#             # Close the file after reading
#             infile.close()
#
#         # Display the total
#         print(format(total, ',.2f'))
#
#     except IOError:
#         print("An error occurred trying to read the file")
#
#     except ValueError:
#         print("No numerical values found in the file")
#
#     except Exception as err:
#         print("An Error Occurred")
#         print(err)
#
#
# main()

# RESOLVED SALES REPORT PAGE 301

def main():
    total = 0  # Accumulator for accumulating total

    try:
        # open the sales_data.txt file
        infile = open('sales.txt', 'r')

        # Read values and add the data
        for line in infile:  # loops through the file

            amount = float(line)  # gets the data, converts to numerical values

            total += amount  # accumulates the values here

        # Close the file after reading
        infile.close()

    except Exception as err:
        #print("An Error Occurred")
        print(err)
    else:  # the final is executed when there's no error
        # Display the total
        print(format(total, ',.2f'))


main()
