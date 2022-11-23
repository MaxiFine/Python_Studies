# THIS PROGRAM IS A GPA CALCULATOR THAT USES THE USER'S GRADES AND
# CREDIT HOURS TO COMPUTE THE TOTAL GPA OF THE USER


def main():
    print('\tGPA CALCULATOR')

    user_inputs = user_grades_credit_hours()

    # Separating the user inputs for display and use
    grades_list = user_inputs[0]
    credit_hours = user_inputs[1]
    user_name = user_inputs[2]
    user_prog = user_inputs[3]
    num_courses = user_inputs[4]

    grading_points = determine_g_points(grades_list)  # conversion of grades
    # to  grading points according to user grades

    # two lists are passed as the arguments to this function
    user_gpa = get_gpa(grading_points, credit_hours)  # Calculating the
    # gpa, total grade points, total credit hours

    user_class = determine_class(user_gpa[0])  # using the gpa to
    # determine the user's class

    display_function(user_name, user_prog, user_class, num_courses, grades_list,
                     credit_hours, grading_points, user_gpa[1], user_gpa[2], user_gpa[0])



# For displaying the user results to the console
def display_function(u_name, u_prog, u_class, course_num, grd_list, crt_list,
                     grdn_points, user_gpa_1, user_gpa_2, user_gpa_0):
    print('\n`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`')
    print('Students Name:', u_name, '\t\t', 'Study Program:', u_prog, '\n')
    print('GPA Class:', u_class)
    print()
    print('Courses \t', 'Grades\t\t', 'Credits\t\t', 'Points')

    for index in range(course_num):
        print('Course', index + 1, '\t', grd_list[index], '\t\t',
              crt_list[index], '\t\t ', ' ', grdn_points[index])

    print('\n Total Credit Hours:', user_gpa_1, '\tTotal Grade Points:',
          format(user_gpa_2, '.2f'), '\t GPA:', format(user_gpa_0, '.2f'))
    print('`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-')


# This function takes all the user inputs and returns them
# in a tuple for processing
def user_grades_credit_hours():
    # Taking Students details
    stu_name = input('Please enter your name: ')  # Student's name
    prog_name = input('Please enter program of study: ')  # Program of study

    grade_list = []  # for the grades of the user
    credit_hours = []  # for the credit hours of the user

    print('Please enter number of courses taken: ', sep='', end='')
    courses_num = input()

    # Input Validation to avoid user from entering anything other than
    # integer literals only and within range as well
    while not courses_num.isdigit() or (int(courses_num) < 4 or int(courses_num) > 13):
        num_course_error()
        courses_num = input()

    correct_range = int(courses_num)  # CONVERSION TO RUN LOOP

    # Using the for loop to iterate the number of times as the number
    # of courses undertaking in the semester
    for index in range(correct_range):
        print('Enter grade for course #', index + 1, ': ', sep='', end='')
        grade = input()

        # Validating user inputs to ensure correct input
        # for processing within the desired range
        expected_inputs = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E', 'F']
        while grade.upper() not in expected_inputs:
            grade_error_msg()
            print('Enter grade for course #', index + 1, ': ', sep='', end='')
            grade = input()
        grade_list.append(grade.upper())  # append grade after validating if correct input

        # For credit hours
        print('Enter credit hours for course #', index + 1, ': ', sep='', end='')
        hours = input()
        # validation of user input to ensure user enters
        # integer values only and within range as well
        while not hours.isdigit() or (int(hours) < 2 or int(hours) > 10):
            credit_error_msg()
            print('Enter credit hours for course #', index + 1, ': ', sep='', end='')
            hours = input()

        check_hours = int(hours)  # converting to integer for processing
        credit_hours.append(check_hours)  # Appending data to the credit list

    return grade_list, credit_hours, stu_name, prog_name, correct_range

# ERROR MESSAGE FUNCTIONS
def num_course_error():
    print("ERROR!\nPlease enter integer numbers only\n"
          "Ranging from 4 to 13 only.\n"
          "Enter the correct range now: ", end='')

def grade_error_msg():
    print('ERROR!!!\nPlease enter grade from A to F only')

def credit_error_msg():
    print("ERROR!\nCredit hours must be positive digits only\n"
          "Enter digits ranging from 2 to 10")

def determine_g_points(user_grades):

    points = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0]  # for the points list
    points_flag = [] # to hold the grade points
    index = 0  # for the indexing

    while index < len(user_grades):
        if user_grades[index] == 'A':
            points_flag.append(points[0])

        elif user_grades[index] == 'B+':
            points_flag.append(points[1])

        elif user_grades[index] == 'B':
            points_flag.append(points[2])

        elif user_grades[index] == 'C+':
            points_flag.append(points[3])

        elif user_grades[index] == 'C':
            points_flag.append(points[4])

        elif user_grades[index] == 'D+':
            points_flag.append(points[5])

        elif user_grades[index] == 'D':
            points_flag.append(points[6])

        elif user_grades[index] == 'E':
            points_flag.append(points[7])

        elif user_grades[index] == 'F':
            points_flag.append(points[8])

        index += 1

    return points_flag

# This function will return gpa, total grade points and credit hours
def get_gpa(g_points, c_hours, ):
    total_grade_points = 0  # accumulator for grade points
    total_hours = 0  # accumulator or credit hours

    # multiply the grade points by the credit hour
    index = 0
    while index < len(g_points):
        product = g_points[index] * c_hours[index] 
        total_grade_points += product  
        index += 1  

    # Getting the total credit hours
    for item in c_hours:
        total_hours += item  

    # calculating the gpa of the user
    gpa = total_grade_points / total_hours

    return gpa, total_hours, total_grade_points

# This function will determine user's class according to the gpa
def determine_class(gpa):
    if gpa > 3.59:
        return 'First Class'
    elif gpa > 2.99 and gpa <= 3.59:
        return 'Second Class Upper'
    elif gpa > 1.99 and gpa <= 2.99:
        return 'Second Class Lower'
    elif gpa > 1.49 and gpa <= 1.99:
        return 'Third Class'
    elif gpa > 0.99 and gpa <=1.49:
        return 'Pass'
    else:
        return 'Fail'

if __name__ == '__main__':
    main()
