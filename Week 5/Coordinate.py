# -*- coding: utf-8 -*-

"""
Created on Fri Jul 19 16:33:27 2019

@author: Ujju
"""



'''Consider the following code from the last lecture video:
Your task is to define the following two methods for the Coordinate class:
    1. Add an __eq__ method that returns True if coordinates refer to same point
    in the plane (i.e., have the same x and y coordinate)
    2. Define __repr__, a special method that returns a string that looks like
    a valid Python expression that could be used to recreate an object with the
    same value. In other words, eval(repr(c)) == c given the definition of
    __eq__ from part 1.
'''

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's x coordinate.
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ', ' + str(self.getY()) + '>'

    # returns True if coordinates refer to same point in the plan
    def __eq__(self,other):
        assert type(other) == type(self)
        return self.getX() == other.getX() and self.getY() == other.getY()
    

    # returns a string that looks like a valid Python expression that could be
    # used to recreate an object with the same value.
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'


c = Coordinate(3,4)
d = Coordinate(2,4)

print(c == d)
print(c.__repr__())