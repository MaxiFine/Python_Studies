# THIS PROGRAM DEMONSTRATES HOW TO GET THE INDEX OF
# AN ITEM IN A LIST AND THEN REPLACE THAT ITEM WITH A NEW ITEM


def main():
    # Create a list with some items
    food = ['Pizza', 'Burgers', 'Chips']

    # Display the list.
    print('Here are the items in the food list: ')
    print(food)

    # Get the item to change
    item = input('Which item should I change? ')

    try:
        # Get the item's index in the list
        item_index = food.index(item)

        # Get the value to replace it with
        new_item = input('Enter the new Food: ')

        # Replace the old item with the new item.
        food[item_index] = new_item

        # Display the list
        print("Here is the updated list")
        print(food)
    except ValueError:
        print('The item was not found in the list')


main()
