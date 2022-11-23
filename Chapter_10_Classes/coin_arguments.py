# THIS PROGRAM PASSES A COIN OBJECT AS AN ARGUMENT TO A FUNCTION

import classes_trials


def main():
    # Create a Coin object
    my_coin = classes_trials.Coin()

    # This will display 'Heads'
    print(my_coin.get_side_up())

    # Pass the object to the flip function as an argument
    flip(my_coin)

    # This might display 'Head' or it might display 'Tail'
    print(my_coin.get_side_up())


# The flip function flips a coin
def flip(coin_obj):
    coin_obj.toss()


if __name__ == '__main__':
    main()
