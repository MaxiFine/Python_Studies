# THIS PROGRAM IS A GPA CALCULATOR THAT USES THE USER'S GRADES AND
# CREDIT HOURS TO COMPUTE THE TOTAL GPA OF THE USER


def main():
    print('\tGPA CALCULATOR')

    user_inputs = user_grades_credit_hours()

    # Separating the user inputs for display
    grades_list = user_inputs[0]  # for user grades
    credit_hours = user_inputs[1]  # for user's credit hours
    user_name = user_inputs[2]  # for user's name
    user_prog = user_inputs[3]  # for user's program of study
    num_courses = user_inputs[4]  # for number of courses iterations

    grading_points = determine_g_points(grades_list)  # conversion of grades
    # to  grading points according to user grades

    # two lists are passed as the arguments to this function
    user_gpa = get_gpa(grading_points, credit_hours)  # Calculating the
    # gpa, total grade points, total credit hours

    user_class = determine_class(user_gpa[0])  # using the gpa to
    # determine the user's class

    # Displaying to the portal
    print('\n`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`')
    print('Students Name:', user_name, '\t\t', 'Study Program:', user_prog, '\n')
    print('GPA Class:', user_class)
    print()
    print('Courses \t', 'Grades\t\t', 'Credits\t\t', 'Points')

    for index in range(num_courses):
        print('Course', index + 1, '\t', grades_list[index], '\t\t',
              credit_hours[index], '\t\t ', ' ', grading_points[index])

    print('\n Total Credit Hours:', user_gpa[1], '\tTotal Grade Points:',
          format(user_gpa[2], '.2f'), '\t GPA:', format(user_gpa[0], '.2f'))
    print('\n`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-')


# Displays Error message for correct input
def course_num_error():
    print('ERROR\nPlease enter integer numbers only.\n'
          'Enter a number ranging from 4 to 13\n'
          'Please enter correct number now: ', end='')


# This function takes all the user inputs and returns them
# in a tuple for processing
def user_grades_credit_hours():
    # Taking Students details
    stu_name = input('Please enter your name: ')  # Student's name
    prog_name = input('Please enter program of study: ')  # Program of study

    # The grades and credit hours will be stored  in a list
    # and be returned to the program
    grade_list = []  # for the grades of the user
    credit_hours = []  # for the credit hours of the user

    print('Please enter number of courses taken: ', sep='', end='')
    courses_num = input()

    # Input Validation to avoid user from entering anything other than
    # integer literals only and within range as well
    while not courses_num.isnumeric() and (courses_num.isdigit() > 3 or courses_num.isdigit() > 13):
        course_num_error()
        courses_num = input()  # for correct input

    correct_range = int(courses_num)

    # Using the for loop to iterate the number of times as the number
    # of courses undertaking in the semester
    for index in range(correct_range):
        print('Enter grade for course #', index + 1, ': ', sep='', end='')
        grade = input()

        # Validation of inputs to ensure user enters the correct input
        # for processing within the desired range
        expected_inputs = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E', 'F']
        while grade.upper() not in expected_inputs:
            print('ERROR\nPlease enter grade from only A-F only')
            print('Please enter grade for course #', index + 1, ': ', sep='', end='')
            grade = input()

        # append grade after validating if correct input
        grade_list.append(grade.upper())

        # For the credit hours
        print('Enter credit hours for course #', index + 1, ': ', sep='', end='')
        hours = input()

        # validation of user inputs of credit hours to ensure user enters
        # integer data inputs only
        while not hours.isnumeric():
            print('ERROR!\nPlease enter integer numbers only.\n'
                  'From 2 to 10')
            print('Enter credit hours for course #', index + 1, ': ', sep='', end='')
            hours = input()

        # Validation to avoid user from entering 0's and negative integers
        # or beyond expected values
        check_hours = int(hours)  # converting to integer for processing
        while check_hours < 2 or check_hours > 10:
            print("ERROR\nCredit hours can't be 0, 1 or negative values\n"
                  "Please enter numbers from 2 to 10\n", end=''
                  "Enter number again: ")
            hours = input()
            check_hours = int(hours)  # Conversion of string input to integer
            # data type for processing

        # Appending data to the credit list
        credit_hours.append(check_hours)

    # The return will be a tuple to work with
    return grade_list, credit_hours, stu_name, prog_name, correct_range

# Getting the total grade points and total credit hours
# passing two lists as the arguments and returns the gpa
def determine_g_points(user_grades):

    points_flag = [0] * len(user_grades)  # to hold the grade points
    index = 0  # for the indexing

    while index < len(user_grades):
        if user_grades[index] == 'A':
            points_flag[index] = 4.0

        elif user_grades[index] == 'B+':
            points_flag[index] = 3.5

        elif user_grades[index] == 'B':
            points_flag[index] = 3.0

        elif user_grades[index] == 'C+':
            points_flag[index] = 2.5

        elif user_grades[index] == 'C':
            points_flag[index] = 2.0

        elif user_grades[index] == 'D+':
            points_flag[index] = 1.5

        elif user_grades[index] == 'D':
            points_flag[index] = 1.0

        elif user_grades[index] == 'E':
            points_flag[index] = 0.5

        elif user_grades[index] == 'F':
            points_flag[index] = 0.0

        index += 1

    return points_flag

# this function will return gpa, total grade points and credit hours
def get_gpa(g_points, c_hours, ):
    total_grade_points = 0  # accumulator for grade points
    total_hours = 0  # accumulator or credit hours

    # multiply the grade points by the credit hour
    index = 0
    while index < len(g_points):
        product = g_points[index] * c_hours[index] # Multplication
        total_grade_points += product  # totalling grade points here
        index += 1  

    # Getting the total credit hours
    for item in c_hours:
        total_hours += item  # totalling the credit hours

    # calculating the gpa of the user
    gpa = total_grade_points / total_hours

    return gpa, total_hours, total_grade_points

# This function will determine user's class according to the gpa
def determine_class(gpa):
    if gpa >= 3.60:
        return 'First Class'
    elif gpa >= 3.00 or gpa >= 3.59:
        return 'Second Class Upper'
    elif gpa >= 2.00 or gpa >= 2.99:
        return 'Second Class Lower'
    elif gpa >= 1.50 or gpa <= 1.99:
        return 'Third Class'
    elif gpa >= 1.00 or gpa <= 1.49:
        return 'Pass'
    else:
        return 'Fail'

main()
