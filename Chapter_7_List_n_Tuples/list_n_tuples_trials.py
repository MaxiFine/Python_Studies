# even_numbers = [2, 4, 6, 8, 10]
#
# names = ['Max', 'Welly', 'Andy', 'Sandy', 'Randy']
#
# print(even_numbers)
# print()
#
# nam = list(range(5))
# print(nam)
# print()
#
# nums = list(range(1, 10, 2))
# print(nums)
# print()
#
# my_list = [41, 56, 30, 29, 33]
#
#
# #   ITERATING THROUGH A LIST USING [INDEX]
# index = 0
# while index < 5:
#     print(my_list[index])
#     index += 1
# print()
#
# # USING THE FOR LOOP
# for array in my_list:
#     print(array)
# print()
#
#
# # THE LEN FUNCTION RETURNS THE SIZE OF A LIST
# # THE len FUNCTION HELPS TO PREVENT IndexError exceptions
# size = len(my_list)
# print(size)
# print()
#
#
# index1 = 0
# while index1 < len(my_list):
#     print(my_list[index1])
#     index1 +=1


# # The NUM_DAYS constant holds the number of
# # days we will gather sales data for
#
# NUM_DAYS = 5
#
#
# def main():
#     # Create a list to hold the sales for each day
#     sales = [0] * NUM_DAYS  # repetition structure here
#
#     # Variable to hold the index using the while loop
#     index = 0
#
#     amount = 0.0
#
#     print("Enter the sales for each day.")
#
#     # Get the sales for each day
#     for index in range(NUM_DAYS):
#         print("Day #", index + 1, ': ', sep='', end='')  # this code makes
#         # the input command to continue on the same line
#         sales[index] = int(input())
#         index += 1
#
#     # Display the values entered by the user
#     print("Here are the values you entered\n")
#
#     for value in sales:
#         amount += float(value)
#         print(value)
#     print()
#     print(amount)
#     print('Great!')
#
#
# main()


# THIS PROGRAM DEMONSTRATES THE
# IN OPERATOR USED WITH A LIST to SEARCH for an item


def main():
    # Create a list of product numbers
    prod_nums = ['V475', 'F987', 'Q143', "R688"]

    # Get a product number to search for
    search = input('Enter a product number: ')

    # Determine whether the item is present in the list
    if search not in prod_nums:
        print(search, 'was not found in the list, thank you')
    else:
        print(search, 'was found in the list')


main()
