# EXERCISE ONE TOTAL SALES OF THE WEEK

def main():
    # create a variable to store the sales list
    all_sales = get_sales()

    # sum them up the list of sales by the user
    total_sales = sum_sales(all_sales)  # passes a list as an argument
    # compute and returns the total of the list

    # Display the results
    print("The total sales made is $",
          format(total_sales, ',.2f'), sep='')
    print(all_sales)


def sum_sales(sales_list):

    total = 0

    for index in sales_list:
        total += index
    return total


def get_sales():

    day_sales = []

    # Prompt the user for the sales
    for day in range(6):
        print("Please Enter sales for Day ", day + 1, ': ', sep='', end='')
        sales = float(input())
        day_sales.append(sales)

    return day_sales


main()
