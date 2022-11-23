# THIS PROGRAM CALCULATES THE AVERAGE OF THE VALUES IN THE LIST


def main():
    # Generate a list
    scores = [2.5,7.3,6.5,4.0,5.2]

    # Create an accumulator
    total = 0.0

    # Total all the values
    for value in scores:
        total += value

    # Calculate the average of the elements in the list
    average = total / len(scores)  # the len function will return
    # the size of the list to be used for average computation

    # Display the results
    print('The total is', average)


main()


