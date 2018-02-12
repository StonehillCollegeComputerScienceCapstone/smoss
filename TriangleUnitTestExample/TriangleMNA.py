class TriangleMNA:

    def display(self):
        print ("Displays the sides of the triangle")

    def isValidInput(self, a, b, c):
        return False

    def isScalene(self, a, b, c):
        return False

    def isIsosceles(self, a, b, c):
        return False

    def isEquilateral(self, a, b, c):
        return False

    def isValidTriangle(self, a, b, c):
        return False

def main():
    print('Enter three integers:')
    a = input()
    b = input()
    c = input()
    t = TriangleMNA()
    t.isValidInput(a, b, c)

if __name__ == '__main__': main()