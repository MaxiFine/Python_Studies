# DRIVER'S LICENSE EXAM WITH TEXT FILES


def main():

    # a list of answers
    answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

    # Open the student's answers to read them
    infile_answers = open('driver_license_exam_stu.txt', 'r')

    # Read the file to the
    stu_answers = infile_answers.readlines()

    infile_answers.close()

    get_stu_list = stu_answer_list(stu_answers)  # a list of student's answers

    # Get the scores from comparing students answers to the system
    # answers and display to the user
    index = 0  # item to control the loop
    flag = 0   # flag to count if the condition is true
    while index < len(answers):
        if answers[index] == get_stu_list[index]:
            flag += 1
        else:  # Note to bring the main logic
            # of the program into the main
            pass
        index += 1

    print("\nAnswers\n", answers)
    print("\nYour Answers\n", get_stu_list)

    print("\n\tYour total score for the Exam is", flag)


def stu_answer_list(infile):  # will read the student's answers
    # into a list and strip the \n character

    index = 0
    while index < len(infile):
        infile[index] = infile[index].rstrip('\n')
        index += 1

    return infile


if __name__ == '__main__':
    main()
