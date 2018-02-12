
#!/usr/bin/python3

import unittest
from TriangleMMNV import TriangleMMNV

class TriangleUnitTestMMNV (unittest.TestCase):

    # Tests if all input values are ints
    def test_isValidInput(self):
        t = TriangleMMNV ()
        self.assertTrue(t.isValidInput(1, 1, 1))

    # Tests if all input values are not strings
    def test_isStringInput(self):
        t = TriangleMMNV ()
        self.assertFalse(t.isValidInput('hello', 'world', 'string'))
        self.assertFalse(t.isValidInput(' ', ' ', ' '))

    # Tests if all input values are not doubles
    def test_isDoubleInput(self):
        t = TriangleMMNV ()
        self.assertFalse(t.isValidInput(3.14, 2.718, 0.5))

    # Tests if all input values are not strings
    def test_isNoneInput(self):
        t = TriangleMMNV ()
        self.assertFalse(t.isValidInput(None, None, None))
        self.assertFalse(t.isValidInput(1, None, None))
        self.assertFalse(t.isValidInput(None, 1, None))
        self.assertFalse(t.isValidInput(None, None, 1))
        self.assertFalse(t.isValidInput(1, 1, None))
        self.assertFalse(t.isValidInput(None, 1, 1))
        self.assertFalse(t.isValidInput(1, None, 1))

    # Tests if all input values are not negative
    def test_isNegativeInput(self):
        t = TriangleMMNV ()
        self.assertFalse(t.isValidInput(-1, -2, -3))

    # Tests if all input values are not zero
    def test_isZeroInput(self):
        t = TriangleMMNV ()
        self.assertFalse(t.isValidInput(0, 0, 0))

    # Tests if all input values are different
    def test_isScalene(self):
        t = TriangleMMNV ()
        self.assertTrue(t.isScalene(2, 3, 4))
        self.assertFalse(t.isScalene(2, 2, 3))
        self.assertFalse(t.isScalene(2, 3, 2))
        self.assertFalse(t.isScalene(3, 2, 2))
        self.assertFalse(t.isScalene(1, 1, 1))

    # Tests if any two input values are the same
    def test_isIsosceles(self):
        t = TriangleMMNV ()
        self.assertTrue(t.isIsosceles(2, 2, 3))
        self.assertTrue(t.isIsosceles(2, 3, 2))
        self.assertTrue(t.isIsosceles(3, 2, 2))
        self.assertFalse(t.isIsosceles(2, 3, 4))
        self.assertFalse(t.isIsosceles(1, 1, 1))

    # Tests if all input values are the same
    def test_isEquilateral(self):
        t = TriangleMMNV ()
        self.assertTrue(t.isEquilateral(1, 1, 1))
        self.assertFalse(t.isEquilateral(2, 3, 4))
        self.assertFalse(t.isEquilateral(2, 2, 3))
        self.assertFalse(t.isEquilateral(2, 3, 2))
        self.assertFalse(t.isEquilateral(3, 2, 2))

    # Triangle inequality theorem
    def test_isValidTriangle(self):
        t = TriangleMMNV ()
        self.assertTrue(t.isValidTriangle(3, 2, 2))
        self.assertTrue(t.isValidTriangle(2, 3, 2))
        self.assertTrue(t.isValidTriangle(2, 2, 3))
        self.assertFalse(t.isValidTriangle(3, 1, 1))
        self.assertFalse(t.isValidTriangle(1, 3, 1))
        self.assertFalse(t.isValidTriangle(1, 1, 3))

if __name__ == '__main__':
    unittest.main()
