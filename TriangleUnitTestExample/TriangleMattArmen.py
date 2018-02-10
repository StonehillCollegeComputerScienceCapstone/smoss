class TriangleMattArmen:

    def display(self):
        print ("Displays the sides of the triangle")

    def isValidInput(self, a, b, c):
        # Checks if all are integers
        if ((not isinstance(a, int)) or (not isinstance(b, int)) or (not isinstance(c, int))):
            return False
        # Checks if all are greater than 0
        if ((a <= 0) or (b <=0) or (c <= 0)):
            return False
        return True

    def isScalene(self, a, b, c):
        if ((a == b) or (a == c) or (b == c)):
            return False
        return True

    def isIsosceles(self, a, b, c):
        if ((a != b) and (a != c) and (b != c)):
            return False
        return True

    def isEquilateral(self, a, b, c):
        return False

    def isValidTriangle(self, a, b, c):
        if ((a + b < c) or (a + c < b) or (b + c < a)):
            return False
        return True

def main():
    print('Enter three integers:')
    a = input()
    b = input()
    c = input()
    t = TriangleMattArmen()
    t.isValidInput(a, b, c)
    t.isValidTriangle(a, b, c)

    if (t.isEquilateral(a, b, c)):
        print ('Triangle is equilateral')
    elif (t.isIsosceles(a, b, c)):
        print ('Triangle is isosceles')
    elif (t.isScalene(a, b, c)):
        print('Triangle is scalene')

if __name__ == '__main__': main()