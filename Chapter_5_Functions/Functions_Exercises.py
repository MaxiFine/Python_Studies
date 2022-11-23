# ALGORITHM WORKBENCH

# def main():
#     number = int(input("Please Enter Number: "))
#
#     print("The Half is ", half(number), "thank you")
#
#
# def half(number):
#     product = number / 2
#     return product
#
# main()


# # EXERCISE 1 KILOMETER CONVERTER EXERCISE
#
# miles_unit = 0.06214
#
# def main():
#
#     distant = float(input("Please Enter Distance: "))
#
#     mile_convert(distant)
#
#     print("The Convert is", format(mile_convert(distant), ',.2f'), "miles thank you")
#
# def mile_convert(distant):
#     miles = distant * miles_unit
#     return miles
#
# main()


# # 1. COUNTY AND STATE TAX CALCULATOR
#
# # CONSTANTS
# COUNTY_TAX = 0.025
# STATE_TAX = 0.05
#
# choice = 'Y'
#
#
# def main():
#
#     item_price = float(input("Please Enter Item's Price: "))
#
#     total_state = state_tax(item_price)
#     total_county = county_tax(item_price)
#
#     total_tax = total_state + total_county
#
#     total_amount = item_price + total_tax
#
#     print("The State's Tax is $", format(total_state, ',.2f'), sep='')
#     print("The County's Tax is $", format(total_county, ',.2f'), sep='')
#     print("The Total Tax to pay is $", format(total_tax, ',.2f'), sep='')
#     print("Total Amount to pay is $", format(total_amount, ',.2f'), sep='')
#
#
# def state_tax(item_price):
#     tax = item_price * STATE_TAX
#     return tax
#
#
# def county_tax(item_tax):
#     tax = item_tax * COUNTY_TAX
#     return tax
#
#
# main()

# #    USING THE TO CONTROL THE NUMBER OF TIMES IT
# #    SHOULD PERFORM THE TASK FOR THE USER
#
# INSURE_RATE = 0.8
#
#
# def main():
#
#     loop = 'y'
#
#     while loop.upper() == "Y":
#         insurance = float(input("Please Enter The Cost: "))
#
#         in_rate = insure_rate(insurance)
#
#         print("The minimum Insurance to be Paid is $", format(in_rate, ',.2f'), sep='')
#
#         loop = input("Do you want to Calculate again? "
#                      "\nPress 'y' to Calculate again or 'n' to Quit: ")
#
#
# def insure_rate(insurance):
#     rate = INSURE_RATE * insurance
#     return rate
#
#
# main()

# # EXERCISE 6 FAT AND CARBOHYDRATE CALCULATIONS
# # USING A LOOP FOR THE USER TO CONTROL THE NUMBER
# # OF TIMES THAT THE PROGRAM SHOULD RUN
#
# FAT_CONS = 9          # FAT CONSTANT
# CABO_CONS = 4         # CARB CONSTANT
#
#
# def main():
#
#     looper = "Y"      # LOOP INITIATOR
#
#     while looper.upper() == "Y": # LOOP TO ENABLE USER CONTROL THE PROGRAM
#
#         fatcalos = float(input("Please Enter Calories from Fat: "))
#
#         carbcalos = float(input("Please Enter Calories from Carbohydrate: "))
#
#         calos_from_fat(fatcalos)
#         calos_from_carbo(carbcalos)

#           # DISPLAYING THE RESULTS FOR FAT
#         print("Calories from fat is ",
#               format(calos_from_fat(fatcalos), ',.2f'), 'g', sep='')

#           # DISPLAYING THE RESULTS FOR CARBO
#         print("Calories from Carbohydrate is ",
#               format(calos_from_carbo(carbcalos), ',.2f'), 'g', sep='')

#           # PROMPTING USER TO CALCULATE AGAIN
#         looper = input("Do you want to calculate again? \n"
#                        "Enter 'y' to calculate again or 'n' to Quit: ")
#
#   # FUNC FOR FAT_GRAMS
# def calos_from_fat(fat_grams):
#     fatgrams = fat_grams * FAT_CONS
#     return fatgrams
#
#       #UNC
# def calos_from_carbo(carbo_grams):
#     carbgrams = carbo_grams * CABO_CONS
#     return carbgrams
#
#
# main()


# # EXERCISE 12 MAXIMUM OF TWO VALUES
#
#
# def main():
#
#     looper = "y"  # THIS WILL RUN THE LOOP
#
#     while looper.upper() == "Y":
#
#         num1 = int(input("Please Enter first number: "))
#
#         num2 = int(input("Please Enter second number: "))
#
#         max_(_1num=num1, _2num=num2)
#
#            #THIS WILL EITHER BREAK OR RUN THE PROGRAM BY USER
#         looper = input("Do you want to calculate again?"
#                        "\nEnter Y'yes' or N'no' to Quit: ")
#
#
# def max_(_1num, _2num):
#
#     if _1num > _2num:
#         return print("The greater value is", _1num)
#     elif _2num > _1num:
#         return print(_2num, "is the Greater Value entered.")
#
#
# main()


# # EXERCISE 13 FALLING DISTANCE PROGRAM
#
# GRAVITY = 9.8
#
#
# def main():
#
#     iterator = 10
#
#     print("Time \tDistance")
#     print("-------------------")
#
#     for checker in range(iterator):
#         checker += 1
#
#         falling_distance(checker)
#
#         print(checker, "\t\t", format(falling_distance(check=checker),
#                                       ',.2f'), "m", sep='')
#
#
# def falling_distance(check):
#     distance = 0.5 * GRAVITY * check ** 2
#     return distance
#
#
# main()

# # EXERCISE 14 KINETIC ENERGY
# # (USE LOOP TO ENABLE USER CONTROL THE PROGRAM)
#
#
# CONSTANT = 0.5
#
#
# def main():
#
#     looper = 'y'  # condition to control the loop
#
#     while looper.upper() == "Y":  # loop condition
#
#         # mass inout
#         mass = float(input("Please enter the mass of the object: "))
#
#         # velocity input
#         velocity = float(input("Please enter the velocity: "))
#
#         # calling the function to job and passing the inputs as its args to work with
#         k_energy = kinetic_energy(mass, velocity)
#
#         # Displaying the result of the Program
#         print("The Kinetic Energy of the object is ", format(k_energy, ',.2f'),
#               "m/s", sep='')
#
#         # if user wants to calculate again
#         looper = input("Enter y to Calculate again "
#                        "or any number to quit: ")
#
#
# def kinetic_energy(para_mass, para_velo):
#     energy = para_velo**2 * para_mass * CONSTANT
#     return energy
#
#
# main()


# EXERCISE 15  TEST AVERAGE AND GRADE
# (THIS PROGRAM WILL ALLOW THE USER TO
# CALCULATE THE DESIRED NUMBER OF TESTS TAKEN),
# (USING THE FOR LOOP)


def main():

    test_taken = 5

    for item in range(test_taken):
            
        test_score = int(input(f"Please enter your Score for test {item + 1} : "))

        if test_score > 89:
            print('90 - 100', '\t\t', determine_grade(test_score))

        elif test_score > 79 and test_score <=89:
            print('80 - 89', '\t\t', determine_grade(test_score))

        elif test_score > 69 and test_score <= 79:
            print('70 - 79', '\t\t', determine_grade(test_score))
                
        elif test_score > 59 and test_score <= 69:
            print('60 -69', '\t\t', determine_grade(test_score))



        getAverage = calc_average(test1=test_score, test2=test_score, \
                    test3=test_score, test4=test_score, test5=test_score, test_taken=test_taken)

    # get_average = calc_average(accumulator, test_taken)

    # Displaying the Average of score for the test taken
    print("The Average Score is ", format(getAverage, ',.2f'), sep='')


def determine_grade(score):

    
    if score >= 90 and score <= 100:
        grade = "A"

    elif score >= 80 and score <= 89:
        grade = "B"

    elif score > 69 and score <= 79:
        grade = "C"

    elif score > 59 and score <= 69:
        grade = "D"

    elif score < 60:
        grade = "F"


    return grade


def calc_average(test1, test2, test3, test4, test5, test_taken):
    average_score = float(test1 + test2 + test3 + test4 + test5 ) / test_taken
    return average_score


main()
