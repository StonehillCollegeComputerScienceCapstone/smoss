import unittest
import math
import sys
from SamNickTriangle import Triangle


class TriangleTestCases(unittest.TestCase):
    def test_valid_int(self):
        x = Triangle()
        self.assertTrue(x.addSide(7))
    def test_valid_double(self):
        x = Triangle()
        self.assertFalse(x.addSide(1.2))
    def test_invalid_upper_case(self):
        x = Triangle()
        self.assertFalse(x.addSide('A')) #upper case
    def test_invalid_lower_case(self):
        x = Triangle()
        self.assertFalse(x.addSide('a')) #lower case
    def test_invalid_special_character(self):
        x = Triangle()
        self.assertFalse(x.addSide('!')) #special character
    def test_invalid_string(self):
        x = Triangle()
        self.assertFalse(x.addSide("invalid"))
    def test_invalid_null_value(self):
        x = Triangle()
        self.assertFalse(x.addSide(None)) #null value
    def test_invalid_zero(self):
        x = Triangle()
        self.assertFalse(x.addSide(0))  #zero value
    def test_invalid_negative(self):
        x = Triangle()
        self.assertFalse(x.addSide(-1))
    def test_addingExtraSides(self):
        x = Triangle()
        x.addSide(7)
        x.addSide(2)
        x.addSide(5)
        self.assertFalse(x.addSide(1.2))
    def test_scalene(self):
        x = Triangle()
        x.addSide(10)
        x.addSide(9)
        x.addSide(8)
        self.assertEqual(x.triangle_type, "Scalene")
    def test_equilateral(self):
        x = Triangle()
        x.addSide(10)
        x.addSide(10)
        x.addSide(10)
        self.assertEqual(x.triangle_type, "Equilateral")
    def test_isosceles(self):
        x = Triangle()
        x.addSide(10)
        x.addSide(9)
        x.addSide(9)
        self.assertEqual(x.triangle_type, "Isosceles")
    def test_valid_side_dimensions(self):
        x = Triangle()
        x.addSide(10)
        x.addSide(1)
        self.assertFalse(x.addSide(1))
        self.assertFalse(x.addSide(100))
    def test_max_side_size(self):
        x = Triangle()
        max_size = math.sqrt(sys.maxint)
        self.assertTrue(x.add(max_size))
        self.assertFalse(x.add(max_size + 0.0001))
    def test_min_side_size(self):
        x = Triangle()
        self.assertTrue(x.addSide(0.0001))

def main():
    print "Start"


if __name__ == '__main__':
    unittest.main()
