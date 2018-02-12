#MAtt Peters, Steve MacSwain
import unittest
import sys
from TriangleUnitTestExample.TriangleMattSteve import Triangle

class TestTriangleMethods(unittest.TestCase):

    def testInts(self):
        t=Triangle()
        self.assertTrue(t.isValid(10,10,10))

    def testNegatives(self):
        t = Triangle()
        self.assertFalse(t.isValid(10,-9,1))

    def testZero(self):
        t = Triangle()
        self.assertFalse(t.isValid(0,1,4))

    def testNearZero(self):
        t = Triangle()
        self.assertTrue(t.isValid(.5,1,1))

    def testDecimal(self):
        t = Triangle()
        self.assertTrue(t.isValid(.4, 1.8, 23.7))

    def testTooBigOfInt(self):
        t = Triangle()
        self.assertFalse(t.isValid(1,1,sys.maxsize))

    def testNearTooBigOfInt(self):
        t = Triangle()
        self.assertTrue(t.isValid(1,5,sys.maxsize-1))

    def testEqualateral(self):
        t = Triangle()
        self.assertTrue(t.isEqualateral(5,5,5))

    def testNotEqualateral(self):
        t = Triangle()
        self.assertFalse(t.isEqualateral(5,2,2))

    def testIsosceles(self):
        t = Triangle()
        self.assertTrue(t.isIsosceles(5,5,10))

    def testNotIsosceles(self):
        t = Triangle()
        self.assertFalse(t.isIsosceles(1,4,2))

    def testScalene(self):
        t = Triangle()
        self.assertTrue(t.isScalene(1,5,3))

    def testNotScalene(self):
        t = Triangle()
        self.assertFalse(t.isScalene(1,1,1))


if __name__=='  main  ':
    unittest.main()

