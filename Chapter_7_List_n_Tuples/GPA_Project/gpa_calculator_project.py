# THIS PROGRAM IS A GPA CALCULATOR THAT USES A LIST TO TAKE INPUTS
# FROM THE USER CALCULATES THE POINTS RETURNS THE CLASS BY THE GRADE
# POINTS GOTTEN FROM THE GRADES


def main():
    # Input function to get the grades and credit hours in list
    # prompt user for the number of courses taken
    print("\n\tGPA Calculator\n")
    try:
        semester_courses = int(input("Enter courses undertaken for the semester: "))
    except ValueError:
        print('ERROR! \nPlease enter an integer number only')
        semester_courses = int(input("Enter courses undertaken for the semester: "))

    # Input validation to avoid user from entering any other thing other than int literals
    while not isinstance(semester_courses, int):
        print('ERROR\nPlease enter integer numbers only')
        print('Please enter number of courses: ', end='')
        semester_courses = int(input())

    stu_name = input("Enter Your name: ")
    stud_program = input('Enter Program of study: ')

    grades_n_credit_hours = get_grades_n_hours(semester_courses)

    grades_list = grades_n_credit_hours[0]  # for the grade list
    credit_list = grades_n_credit_hours[1]  # for the credit list

    # get the grade points in a list to be worked with

    print(grades_list)
    print(credit_list)

    grade_points_list = get_grade_points_type_2(grades_list)  # points list

    print(grade_points_list)
    # at here now
    # Getting the gpa, grade points and credit hours totals
    gpa_calculation = calc_gpa(grade_points_list, credit_list)

    gpa = gpa_calculation[0]
    grade_points = gpa_calculation[2]
    credit_hours = gpa_calculation[1]

    # Get the class
    user_class = get_class(gpa)
    print(gpa, grade_points, credit_hours)
    print(user_class)
    print(gpa_calculation)

    # Displaying the portal
    print('\n`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`')
    print('Students Name:', stu_name, '\t\t', 'Study Program:', stud_program, '\n')
    print('GPA Class:', user_class)
    print()
    print('Courses \t', 'Credit\t\t', 'Grade\t\t', 'Points')

    for index in range(int(semester_courses)):
        print('Course', index + 1, '\t', credit_list[index], '\t\t',
              grades_list[index], '\t\t ', ' ', grade_points_list[index])

    print('\n Total Credit Hours:', credit_hours, '\tTotal Grade Points:',
          grade_points, '\t GPA:', format(gpa, '.2f'))
    print('\n`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-')


# this function takes the grades and credit hours of the and returns
# the data in list form
def get_grades_n_hours(num_courses):
    grade_list = []  # to keep the grades from the user
    credit_list = []  # to keep the credit hours from the user

    # getting the inputs from the user
    for index in range(num_courses):
        print("Enter grade for course #", index + 1, ': ',
              sep='', end='')  # this will make it appear on a straight line
        grade = input()  # input for the grade

        # Input Validation for to validate user grades within a range from A - F
        while grade != 'A' and grade != 'B+' and grade != 'B' and grade != 'C+' \
                and grade != 'C' and grade != 'D+' and grade != 'D' and grade != 'E' and \
                grade != 'F' and grade != 'a' and grade != 'b+' and grade != 'b' and grade != 'c+' \
                and grade != 'c' and grade != 'd+' and grade != 'd' and grade != 'e' and grade != 'f':
            print("ERROR\nPlease enter grades from A to F\n")
            print("Enter grade for course #", index + 1, ': ',
                  sep='', end='')  # this will make it appear on a straight line
            grade = input()  # input for the grade
        grade_list.append(grade.upper())  # appending grade to the list in upper cases

        # Taking the credit hours
        print("Enter credit hour for course #", index + 1, ': ', sep='', end='')
        credit_hours = input()  # input for credit hours
        #if credit_hours != isinstance(credit_hours, int):
        while credit_hours != credit_hours.isdigit():
            print('ERROR!\nPlease enter integers only')
            print('Enter credit hour for course #', index + 1, ': ', sep='', end='')
            credit_hours = input()
            # try:
            #     print("ERROR! Credit hours must be a number, not a string\nPlease enter again")
            #     print("Enter credit hour for course #", index + 1, ': ', sep='', end='')
            #     credit_hours = int(input())  # input for credit hours
            # except ValueError:
            #     pass
            #     continue
            credit_list.append(int(credit_hours))  # appending credit hours to list if user enters
            # anything other than an integer literal

    return grade_list, credit_list  # when the function is called, it will
    # return the grades and credit hours in a list form


# this function returns the grades points in a list
def get_grade_points_type_2(items):
    points = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0]  # for the points list
    list_points = []
    index = 0

    while index < len(items):
        if items[index] == 'A':
            point: float = points[0]
            list_points.append(point)

        elif items[index] == 'B+':
            point: float = points[1]
            list_points.append(point)

        elif items[index] == 'B':
            point: float = points[2]
            list_points.append(point)

        elif items[index] == 'C+':
            point: float = points[3]
            list_points.append(point)

        elif items[index] == 'C':
            point: float = points[4]
            list_points.append(point)

        elif items[index] == 'D+':
            point: float = points[5]
            list_points.append(point)

        elif items[index] == 'D':
            point: float = points[6]
            list_points.append(point)

        elif items[index] == 'E':
            point: float = points[7]
            list_points.append(point)

        elif items[index] == 'F':
            point: float = points[8]
            list_points.append(point)

        index += 1

    return list_points


# Getting the total grade points and total credit hours
# passing two lists as the arguments and returns the gpa
# def determine_g_points(user_grades):
#
#     points_flag = [0] * len(user_grades)  # to hold the grade points
#     index = 0  # for the indexing
#
#     while index < len(user_grades):
#         if user_grades[index] == 'a' or user_grades[index] == 'A':
#             points_flag[index] = 4.0
#
#         elif 'b+' == user_grades[index] or user_grades[index] == 'B+':
#             points_flag[index] = 3.5
#
#         elif 'b' == user_grades[index] or user_grades[index] == 'B':
#             points_flag[index] = 3.0
#
#         elif 'c+' == user_grades[index] or user_grades[index] == 'C+':
#             points_flag[index] = 2.5
#
#         elif 'c' == user_grades[index] or user_grades[index] == 'C':
#             points_flag[index] = 2.0
#
#         elif 'd+' == user_grades[index] or user_grades[index] == 'D+':
#             points_flag[index] = 1.5
#
#         elif 'd' == user_grades[index] or user_grades[index] == 'D':
#             points_flag[index] = 1.0
#
#         elif 'e' == user_grades[index] or user_grades[index] == 'E':
#             points_flag[index] = 0.5
#
#         elif 'f' == user_grades[index] or user_grades[index] == 'F':
#             points_flag[index] = 0.0
#
#         index += 1
#
#     return points_flag


def calc_gpa(grade_points, credit_list):
    total_grade_points = 0  # sum of all the grade points
    total_hours = 0  # sum of the credit hours

    # multiply the grade points by the credit hour
    index = 0
    while index < len(credit_list):
        product = credit_list[index] * grade_points[index]  # Multiplication
        # of the point by the credit hours
        total_grade_points += product  # totalling the grade points here
        index += 1

    # Getting the total credit hours
    for item in credit_list:
        total_hours += item  # totalling the credit hours

    # calculating the gpa of the user
    gpa = total_grade_points / total_hours

    return gpa, total_hours, total_grade_points


def get_class(gpa_points):
    if gpa_points >= 3.60:
        return 'First Class'

    elif gpa_points >= 3.00 or gpa_points >= 3.59:
        return 'Second Class Upper'

    elif gpa_points >= 2.00 or gpa_points >= 2.99:
        return 'Second Class Lower'

    elif gpa_points >= 1.50 or gpa_points <= 1.99:
        return 'Third Class'

    elif gpa_points >= 1.00 or gpa_points <= 1.49:
        return 'Pass'

    else:
        return 'Fail'


main()
