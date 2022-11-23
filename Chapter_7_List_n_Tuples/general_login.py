# Get the first three letters of the first name
# If the name is less than 3 characters, the
# slicing will return the entire first name.


def get_login_name(first, last, id_number):
    # Get the first three letters of the first name
    set1 = first[0:3]

    # Get the first three letters of the last name
    set2 = last[0:3]

    # Get the last three letters of the student ID
    set3 = id_number[-3:]

    # Put the sets of characters together
    login_name = set1 + set2 + set3

    return login_name
