#matt peters, steve macswain
import sys
class Triangle:

    s0 = 0;
    s1 = 0;
    s2 = 0;

    def __init__(self):
        s0=0
        s1=0
        s2=0

    def isValid(self, arg1,arg2,arg3):
        one = ((isinstance(arg1,int) or isinstance(arg1,float))) and (arg1 > 0) and arg1<sys.maxsize
        two = (isinstance(arg2,int) or isinstance(arg2,float)) and arg2 > 0 and arg2< sys.maxsize
        three = (isinstance(arg3, int) or isinstance(arg3, float)) and arg3 > 0 and arg3 < sys.maxsize
        return (one and two and three)

    def isEqualateral(self, arg1,arg2,arg3):
        return (arg1 == arg2 == arg3)

    def isIsosceles(self,arg1,arg2,arg3):
        side1=(arg1==arg2)
        side2=(arg2==arg3)
        side3=(arg3==arg1)
        counter=0
        return(side1 or side2 or side3)

    def isScalene(self,arg1,arg2,arg3):
        return (not self.isEqualateral(arg1,arg2,arg3)) and (not self.isIsosceles(arg1,arg2,arg3))
