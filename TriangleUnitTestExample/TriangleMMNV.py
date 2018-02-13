#!/usr/bin/python3

class TriangleMMNV:

    def display(self):
        print ("Displays the sides of the triangle")



    def isValidInput(self, a, b, c):
        try:
            allNotNone = a is not None and b is not None and c is not None

        except: return False

        try:
            allInt = type (a) is type (b) is type (c) is type (1)

        except: return False

        try:
            allPositive = (a > 0) and (b > 0) and (c > 0)

        except:return False

        return allNotNone and allInt and allPositive






    def isScalene(self, a, b, c):
        testAB = a is not b
        testBC = b is not c
        testCA = c is not a

        return testAB and testBC and testCA






    def isIsosceles(self, a, b, c):
        AB = a is b
        BC = b is c
        CA = c is a
        ABC = a is b is c

        return (AB or BC or CA) and not ABC







    def isEquilateral(self, a, b, c):
        testAB = a is b
        testBC = b is c
        testCA = c is a

        return testAB and testBC and testCA






    def isValidTriangle (self, a, b, c):
        GT_c = (a + b) > c
        GT_a = (b + c) > a
        GT_b = (a + c) > b

        return GT_a and GT_b and GT_c





def main ():
    print ("Triangle Program")


if __name__ == '__main__':
    main ()