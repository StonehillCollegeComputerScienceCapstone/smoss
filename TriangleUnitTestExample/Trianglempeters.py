#matt peters, steve macswain
class Triangle:

    s0 = 0;
    s1 = 0;
    s2 = 0;

    def __init__(self):
        s0=0
        s1=0
        s2=0

    def isValid(self, arg1,arg2,arg3):
        one = (isinstance(arg1,int) || isinstance(arg1,float))
        two = (isinstance(arg1,int) || isinstance(arg1,float))


    def isEqualateral(self, arg1,arg2,arg3):
        return (arg1 == arg2 == arg3)

    def isIsosceles(self,arg1,arg2,arg3):
        side1=(arg1==arg2)
        side2=(arg2==arg3)
        side3=(arg3==arg1)
        counter=0
        return(side1 or side2 or side3)

    def isScalene(self,arg1,arg2,arg3):
        return (not self.isEqualateral(self,arg1,arg2,arg3)) and (not self.isIsosceles(self,arg1,arg2,arg3))
