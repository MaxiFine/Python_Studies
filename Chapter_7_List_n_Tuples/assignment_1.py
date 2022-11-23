# Assignment using the iF statement


def main():
    print("Welcome to Exams Grader")

    score = input("Please enter your score: ")

    while not score.isdigit() or not (int(score) > 0 and int(score) <= 100):
        error_msg()
        score = input()

    grade = score_grade(int(score))

    print(grade)


def score_grade(marks):

    if marks > 79 and marks <= 100:
        return "Grade is: A"
    elif marks > 74 and marks <= 79:
        return "Grade is: B+"
    elif marks > 69 and marks <= 74:
        return 'Grade is: B'
    elif marks > 64 and marks <= 69:
        return 'Grade is: C+'
    elif marks > 59 and marks <= 64:
        return 'Grade is: C'
    elif marks > 54 and marks <= 59:
        return 'Grade is: D+'
    elif marks > 49 and marks <= 54:
        return 'Grade is D'
    elif marks > 44 and marks <= 49:
        return
    elif marks > 0 and marks < 45:
        return 'Your grade is: F'
    else:
        print('ERROR!\nExam scores ranges from 1 to 100\n'
              'Please rerun the program')


def error_msg():
    print("ERROR!\nExam score should not be or less than zero\n"
          "Scores ranges from 1 to 100\n"
          "Please enter score again: ", end='')


main()
