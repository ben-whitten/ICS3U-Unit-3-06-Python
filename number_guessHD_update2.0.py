#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which makes you guess a number.

import random


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    print("")
    print("I am thinking of a number...")

    while True:

        guessed_number = input("What do you think it is?: ")

        try:
            integer_as_number = int(guessed_number)
            if integer_as_number == random.randint(1, 9+1):
                print("")
                print(color.PURPLE + 'You did it, you won!' + color.END)
                print(color.BOLD + color.UNDERLINE + color.YELLOW
                      + 'Thanks for playing!' + color.END)
                break
            else:
                print("")
                print("")
                print(color.UNDERLINE + color.RED
                      + 'WRONG! Try again.' + color.END)
        except Exception:
            print("")
            print("")
            print(color.GREEN + color.UNDERLINE +
                  'Sorry that was not a number' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
