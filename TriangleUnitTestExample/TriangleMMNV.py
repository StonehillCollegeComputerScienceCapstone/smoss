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
        return False

    def isIsosceles(self, a, b, c):
        return False

    def isEquilateral(self, a, b, c):
        return False

    def isValidTriangle (self, a, b, c):
        return False


def main ():
    print ("Triangle Program")


if __name__ == '__main__':
    main ()