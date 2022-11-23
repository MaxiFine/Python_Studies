# THIS PROGRAM GETS A SERIES OF TEST SCORES AND CALCULATES THE AVERAGE
# OF THE SCORES WITH THE LOWEST SCORE DROPPED


def main():
    # Get the test scores from the user
    scores = get_scores()

    # Get the total of the test scores
    total = get_total(scores)

    # Get the lowest test score
    lowest = min(scores)

    # Subtract the lowest from the total
    total -= lowest

    # Calculate the average. Note that we divided by 1 less than the number
    # of scores because the lowest scores was dropped.
    average = total / (len(scores) - 1)

    # Display the average
    print('The average, with the lowest score dropped is: ', average)


def get_scores():
    # Create an empty list
    test_score = []

    # create a variable to control loop
    again = 'y'

    # Get the scores from the user and add them to  the list
    while again == 'y':  # A Sentinel loop
        # Get a score and add it to the list
        value = float(input('Enter a test score: '))
        test_score.append(value)

        # Letting the user control the program
        print("Do you want to add another number")
        again = input('y = yes anything else is = no: ')
        print()

    return test_score


def get_total(value_list):
    # This function gets a list as an argument and returns the sum of the list
    total = 0  # this will be an accumulator to hold the summation of values

    # Get items and add them
    for value in value_list:
        total += value

    return total


main()
