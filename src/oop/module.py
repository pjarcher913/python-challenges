# Created by Patrick Archer on 27 July 2019.
# Copyright to the above author. All rights reserved.

"""
@file is an exercise on Object-Oriented Programming.
"""

"""========== IMPORTS =========="""

import sys
import string

"""========== GLOBAL VARS =========="""



"""========== MAIN() =========="""

def oop():

    p1 = Person("Person1", 21, 70000)
    p2 = Person("Person2", 50, 21000)

    print(p1.getName())

    p1.changeName("Person1-NEW")

    print(p1.getAllInfo())
    
    p3 = Admin("Person3", 12, 40000, "Moderator")

    print(p3.getAllInfo())

"""========== ADDITIONAL FUNCTIONS =========="""

class Person:

    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self. pay = pay

    def getAllInfo(self):
        return "\nName: {}\nAge: {}\nPay: {}\n".format(self.name, self.age, self.pay)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getPay(self):
        return self.pay

    def changeName(self, newName):
        self.name = newName

    def changeAge(self, newAge):
        self.age = newAge

    def changePay(self, newPay):
        self.pay = newPay

class Admin(Person):

    def __init__(self, name, age, pay, role):
        super().__init__(name, age, pay)
        self.role = role

    def getAllInfo(self):
        return "\nName: {}\nAge: {}\nPay: {}\nRole: {}\n".format(self.name, self.age, self.pay, self.role)

    def getRole(self):
        return self.role

    def changeRole(self, newRole):
        self.role = newRole


"""========== \/ SCOPE \/ =========="""

if __name__ == '__oop__':
    oop()

"""========== \/ @file END \/ =========="""
