# Created by Patrick Archer on 26 July 2019.
# Copyright to the above author. All rights reserved.

"""
DIRECTIONS:
    Randomly generate two lists and write a program that returns a list that contains only the elements that are common
    between the lists (without duplicates).
"""

"""========== IMPORTS =========="""

import sys
import random
import time

"""========== GLOBAL VARS =========="""



"""========== MAIN() =========="""

def list_comprehensions():

    print("This program generates two lists of random sizes and element values and returns a list that contains only "
          "elements common between the two (without duplicates, sorted ascending).\n")

    # save start time of program
    startTime = time.process_time()
    # print(startTime)

    # randomly generate list1 and list2 sizes (sizes >=1 && <= 20)
    list1Size = random.randint(1, 20)
    list2Size = random.randint(1, 20)

    # initialize empty lists (to be filled w/ randomly-generated element values)
    list1 = []
    list2 = []

    # randomly generate list1 and list2 element values
    for index in range(list1Size):
        list1.append(random.randint(1,100))
    for index in range(list2Size):
        list2.append(random.randint(1, 100))

    print("List 1 size = " + str(list1Size))
    print("List 2 size = " + str(list2Size))
    print("List #1 = " + str(list1))
    print("List #1 = " + str(list2))

    # find common elements and add them to separate array
    result = commonElementFinder(list1, list2)

    # sort ascending
    result.sort()

    print("\nThe common elements between the two lists are: ")
    print(str(result))

    # save end time of program
    endTime = time.process_time()
    # print(endTime)

    # display total run-time of program
    print("\n[CONSOLE]: The program took %.3f milliseconds to execute." % (1000 * (endTime - startTime)))

"""========== ADDITIONAL FUNCTIONS =========="""

def commonElementFinder(l1, l2):

    commonElements = []

    for a in range(len(l1)):
        for b in range(len(l2)):
            if l1[a] == l2[b] & l1[a] not in commonElements:
                commonElements.append(l1[a])

    return commonElements

"""========== \/ SCOPE \/ =========="""

if __name__ == '__list_comprehensions__':
    list_comprehensions()

"""========== \/ @file END \/ =========="""
