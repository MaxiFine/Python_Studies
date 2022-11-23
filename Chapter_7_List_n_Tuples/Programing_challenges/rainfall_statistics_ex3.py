# THIS PROGRAM GETS THE TOTAL RAINFALL FROM THE USER AND COMPUTES THEM

def main():
    # Get inputs from the user
    rainfall = get_rainfalls()  # Stores rainfall in a list form

    # Gets the total rainfall from the list
    total_rainfall = calc_rainfall(rainfall)  # A list is passed as an
    # argument

    # Gets the average rainfall from the list using the total rainfall
    # and the number of months
    average = get_average(total_rainfall, len(rainfall))

    # Gets min and max rainfalls from the list
    min_rain = min(rainfall)
    max_rain = max(rainfall)

    print("The total rainfall for the year is", format(total_rainfall, ',.2f'), sep='')
    print('With an average rain of', format(average, ',.2f'),
          'rainfall in a month')
    print("The maximum rainfall in the year was", max_rain, '\n'
          'The minimum rainfall in the year was', min_rain)


def get_rainfalls():

    months = 12  # for the number of iterations
    rain_list = []

    for index in range(months):  # using the for loop
        print("Enter rainfall for month ", index + 1, ': ',
              sep='', end='')
        rain = float(input())
        rain_list.append(rain)

    return rain_list


def calc_rainfall(rain_total):

    total = 0

    for item in rain_total:
        total += item

    return total


def get_average(total_rain, months):

    average_rainfall = total_rain / months

    return average_rainfall


main()
