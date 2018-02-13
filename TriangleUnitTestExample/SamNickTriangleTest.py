import unittest
import math
import sys
from SamNickTriangle import SamNickTriangle

class SamNickTriangleTest(unittest.TestCase):
    def test_valid_int(self):
        x = SamNickTriangle()
        self.assertTrue(x.addSide(7))
    def test_valid_double(self):
        x = SamNickTriangle()
        self.assertTrue(x.addSide(1.2))
    def test_invalid_upper_case(self):
        x = SamNickTriangle()
        self.assertFalse(x.addSide('A')) #upper case
    def test_invalid_lower_case(self):
        x = SamNickTriangle()
        self.assertFalse(x.addSide('a')) #lower case
    def test_invalid_special_character(self):
        x = SamNickTriangle()
        self.assertFalse(x.addSide('!')) #special character
    def test_invalid_string(self):
        x = SamNickTriangle()
        self.assertFalse(x.addSide("invalid"))
    def test_invalid_null_value(self):
        x = SamNickTriangle()
        self.assertFalse(x.addSide(None)) #null value
    def test_invalid_zero(self):
        x = SamNickTriangle()
        self.assertFalse(x.addSide(0))  #zero value
    def test_invalid_negative(self):
        x = SamNickTriangle()
        self.assertFalse(x.addSide(-1))
    def test_addingExtraSides(self):
        x = SamNickTriangle()
        x.addSide(7)
        x.addSide(2)
        x.addSide(5)
        self.assertFalse(x.addSide(1.2))
    def test_scalene(self):
        x = SamNickTriangle()
        x.addSide(10)
        x.addSide(9)
        x.addSide(8)
        self.assertEqual(x.triangle_type(), "Scalene")
    def test_equilateral(self):
        x = SamNickTriangle()
        x.addSide(10)
        x.addSide(10)
        x.addSide(10)
        self.assertEqual(x.triangle_type(), "Equilateral")
    def test_isosceles(self):
        x = SamNickTriangle()
        x.addSide(10)
        x.addSide(9)
        x.addSide(9)
        self.assertEqual(x.triangle_type(), "Isosceles")
    def test_valid_side_dimensions(self):
        x = SamNickTriangle()
        x.addSide(7)
        x.addSide(10)
        x.addSide(5)
        self.assertTrue(x.valid_triangle())
    def test_max_side_size(self):
        x = SamNickTriangle()
        max_size = math.sqrt(sys.maxsize)
        self.assertTrue(x.addSide(max_size))
        self.assertFalse(x.addSide(max_size + 0.0001))
    def test_min_side_size(self):
        x = SamNickTriangle()
        self.assertTrue(x.addSide(0.0001))
    def test_less_sides_triangle_type(self):
        x = SamNickTriangle()
        x.addSide(10)
        self.assertFalse(x.triangle_type())
        self.assertFalse(x.valid_triangle())


def main():
    print("Start")


if __name__ == '__main__':
    unittest.main()
