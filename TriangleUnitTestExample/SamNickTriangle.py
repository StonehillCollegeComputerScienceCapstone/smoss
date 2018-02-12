import unittest
import sys
import math

class SamNickTriangle:
    sides = []
    index = 0
    def __init__(self):
        self.sides = []
        self.index = 0
       # print("object made")

    def addSide(self,side):
        if(side == None):
            return False
        if isinstance(side,(int,float)):
            if(side<=0.00001):
                return False #tests for zero and negative
            max_size = math.sqrt(sys.maxsize)
            if (side > max_size):
                return False
            if (len(self.sides) == 3):
                return False
            self.sides.append(side)
            return True
        else:
            return False #tests for upper case / lower case / special characters / any string

    #need to check if adding extra side
    def triangle_type(self):
        if (len(self.sides) < 3):
            return False
        elif (self.sides[0] == self.sides[1] and self.sides[1] == self.sides[2]):
            return "Equilateral"
        elif (self.sides[0] != self.sides[1] and self.sides[1] != self.sides[2] and self.sides[0] != self.sides[2]):
            return "Scalene"
        else:
            return "Isosceles"

    def valid_triangle(self):
        if (len(self.sides) != 3):
            return False
        if (((self.sides[0] + self.sides[1]) > self.sides[2]) and ((self.sides[0] + self.sides[2]) > self.sides[1]) and ((self.sides[1] + self.sides[2]) > self.sides[0])):
            return True
        return False

def main():
    print ("Start")


if __name__ == '__main__':
    unittest.main()
