# Created by Patrick Archer on 26 July 2019
# Copyright to the above author. All rights reserved.

"""
@file is main execution script for project.
"""

"""========== IMPORTS =========="""

import sys
import time
import os

from src.list_comprehensions.module import list_comprehensions
from src.oop.module import oop
from src.fibonacci.module import fib

"""========== GLOBAL VARS =========="""



"""========== MAIN() =========="""

def main():

    # main runtime loop
    while True:

        # display main menu to user; take input; call corresponding function(s)
        menuSelection = input(
            "\n===========================================================================\n"
            "\n\tPlease select an exercise to view (type # then hit enter/return):"
            "\n\t\t0 - QUIT PROGRAM"
            "\n\t\t1 - Fibonacci Sequence Generator"
            "\n\t\t2 - List Comprehensions"
            "\n\t\t3 - Object Oriented Programming"
            "\n\t"
        )
        print("\n===========================================================================\n")
        if (menuSelection == str(0)):
            sys.exit(0)
        elif (menuSelection == str(1)):
            # os.system('cls')
            fib()
            time.sleep(1)
        elif (menuSelection == str(2)):
            # os.system('cls')
            list_comprehensions()
            time.sleep(1)
        elif (menuSelection == str(3)):
            # os.system('cls')
            oop()
            time.sleep(1)
        else:
            # os.system('cls')
            print("[CONSOLE]: Error -> Invalid menu option. Please try again.")


"""========== ADDITIONAL FUNCTIONS =========="""



"""========== \/ SCOPE \/ =========="""

if __name__ == '__main__':
    main()

"""========== \/ @file END \/ =========="""
