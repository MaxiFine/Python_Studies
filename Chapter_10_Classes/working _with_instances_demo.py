# This program imports the coin module and creates three
# instances of the Coin class

import classes_trials


def main():
    coin1 = classes_trials.Coin()
    coin2 = classes_trials.Coin()
    coin3 = classes_trials.Coin()

    # Display the side ups
    print(coin1.get_side_up())
    print(coin2.get_side_up())
    print(coin3.get_side_up())

    # Toss the coin
    print('Tossing the coin...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Display the side of each coin that is facing up
    print('Here are the sides that are facing Up now:')
    print(coin1.get_side_up())
    print(coin2.get_side_up())
    print(coin3.get_side_up())


main()
