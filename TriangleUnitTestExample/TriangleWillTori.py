class Triangle:
    def __init__(self, s1, s2, s3):
        self.side1 = str(s1)
        self.side2 = str(s2)
        self.side3 = str(s3)


    def isvalid(self):


        if not self.side1.isdigit() or not self.side2.isdigit() or not self.side3.isdigit():
            return False
        self.side1 = int(self.side1)
        self.side2 = int(self.side2)
        self.side3 = int(self.side3)
        if self.side1 > 0 and self.side2 > 0 and self.side3 > 0:
            if isinstance(self.side1, float) or isinstance(self.side2, float) or isinstance(self.side3, float):
                return False
            else:
                return True
        else:
            return False

    def isisosceles(self):
        if not self.isvalid():
            return False
        if self.side1 == self.side2 != self.side3:
            return True
        elif self.side1 != self.side2 == self.side3:
            return True
        elif self.side1 == self.side3 != self.side2:
            return True
        else:
            return False


    def isscalene(self):
        if not self.isvalid():
            return False
        if self.side1 != self.side2 != self.side3:
            return True
        else:
            return False

    def isequilateral(self):
        if not self.isvalid():
            return False
        if self.side1 == self.side2 == self.side3:
            return True
        else:
            return False

