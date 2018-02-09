import unittest
import TriangleMNA

class TriangleUnitTestMNA(unittest.TestCase):

    # Tests if all input values are ints
    def test_isValidInput(self):
        self.assertTrue(TriangleMNA.isValidInput(1, 1, 1))

    # Tests if all input values are not strings
    def test_isStringInput(self):
        self.assertFalse(TriangleMNA.isValidInput('hello', 'world', 'string'))
        self.assertFalse(TriangleMNA.isValidInput(' ', ' ', ' '))

    # Tests if all input values are not doubles
    def test_isDoubleInput(self):
        self.assertFalse(TriangleMNA.isValidInput(3.14, 2.718, 0.5))

    # Tests if all input values are not strings
    def test_isNoneInput(self):
        self.assertFalse(TriangleMNA.isValidInput(None, None, None))

    # Tests if all input values are not negative
    def test_isNegativeInput(self):
        self.assertFalse(TriangleMNA.isValidInput(-1, -2, -3))

    # Tests if all input values are not zero
    def test_isZeroInput(self):
        self.assertFalse(TriangleMNA.isValidInput(0, 0, 0))

    # Tests if all input values are different
    def test_isScalene(self):
        self.assertTrue(TriangleMNA.isScalene(2, 3, 4))

    # Tests if any two input values are the same
    def test_isIsosceles(self):
        self.assertTrue(TriangleMNA.isIsosceles(2, 2, 3))
        self.assertTrue(TriangleMNA.isIsosceles(2, 3, 2))
        self.assertTrue(TriangleMNA.isIsosceles(3, 2, 2))

    # Tests if all input values are the same
    def test_isEquilateral(self):
        self.assertTrue(TriangleMNA.isEquilateral(1, 1, 1))

    # Triangle inequality theorem
    def test_isValidTriangle(self):
        self.assertFalse(TriangleMNA.isValidTriangle(2, 1, 1))
        self.assertFalse(TriangleMNA.isValidTriangle(1, 2, 1))
        self.assertFalse(TriangleMNA.isValidTriangle(1, 1, 2))
        self.assertFalse(TriangleMNA.isValidTriangle(3, 1, 1))
        self.assertFalse(TriangleMNA.isValidTriangle(1, 3, 1))
        self.assertFalse(TriangleMNA.isValidTriangle(1, 1, 3))


if __name__ == '__main__':
    unittest.main()
