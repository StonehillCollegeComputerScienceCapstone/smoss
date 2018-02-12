import unittest
import sys


class Triangle:
    sides = None
    index = 0
    def __init__(self):
        print "object made"
    def addSide(self,side):
        if(side == None):
            return False
        if isinstance(side,(int,float)):
            if(side==0):
                return False

        else:
            return False

def main():
    print "Start"


if __name__ == '__main__':
    unittest.main()
