# THIS PROGRAM DEMONSTRATES HOW TO USE THE REMOVE
# METHOD TO REMOVE AN ITEM FROM A LIST.


def main():
    # Create a list with some items
    food = ['Pizza', 'Burgers', 'Chips']

    # Display the list
    print('Here are the items in the food list:')
    print(food)

    # Get the item to change
    f_name = input('Which item should I remove: ')

    try:
        # Removing an item
        food.remove(f_name)

        # Displaying after operation
        print("Here is the revised list:")
        print(food)

    except ValueError:
        print('That item was not found in the list.')


main()
