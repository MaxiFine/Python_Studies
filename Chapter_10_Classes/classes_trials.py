# THIS PROGRAM SIMULATES A COIN THAT IS TOSSED
import random


# The Coin Class simulates a coin that can be flipped
class Coin:
    # The __init__ method initializes the
    # side-up data attribute with Heads
    def __init__(self):
        self.__side_up = 'Heads'  # this is a data attribute that can work
        # with the methods in this class

    # The toss method generates a random number in the range of 0 through 1
    # If the number is 0 the side up is set to Tail
    def toss(self):
        if random.randint(0, 1) == 0:  # this will generate a random
            # number and for the number of tossing
            self.__side_up = 'Heads'
        else:
            self.__side_up = 'Tails'

    # The get_side_up method returns the value referenced by the side_up
    def get_side_up(self):  # this method returns the value of the
        # init attribute
        return self.__side_up


def main():
    # Create an object from the Coin Class
    my_coin = Coin()  # the my_coin variable is the new object

    # Display the side of the coin that is facing up
    print('This side is up:', my_coin.get_side_up())

    # Toss the coin
    print('Tossing the coin 10 times ...')
    for item in range(10):
        my_coin.toss()
        print(my_coin.get_side_up())

    # Display the side of the coin that is facing up
    print('This side is up:', my_coin.get_side_up())


if __name__ == '__main__':
    main()
