# Created by Patrick Archer on 29 July 2019 at 9:00 AM.
# Copyright to the above author. All rights reserved.

"""
@file asks the user how many Fibonacci numbers to generate and then generates them
"""

"""========== IMPORTS =========="""



"""========== GLOBAL VARS =========="""



"""========== MAIN() =========="""

def fib():

    print("\nThis app generates a sequence of Fibonacci numbers for a specified range.\n")
    seqLength = input("How many numbers would you like to generate?\n")
    print("\nResulting sequence:")
    print(str(fibGen(int(seqLength))))

"""========== ADDITIONAL FUNCTIONS =========="""

def fibGen(seqLength):

    fibSeq = []

    for index in range(0, seqLength):

        if index == 0:
            fibSeq.append(0)
        elif index == 1:
            fibSeq.append(1)
        else:
            fibSeq.append(fibSeq[index - 2] + fibSeq[index - 1])

    return fibSeq

"""========== \/ SCOPE \/ =========="""

if __name__ == '__fib__':
    fib()

"""========== \/ @file END \/ =========="""
