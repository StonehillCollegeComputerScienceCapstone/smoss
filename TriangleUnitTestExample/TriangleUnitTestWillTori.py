import unittest
from TriangleWillTori import Triangle
class TestTriangles(unittest.TestCase):

    def test_validIntegers(self):
        t= Triangle(3, 4, 5)
        self.assertTrue(t.isvalid())

    def test_invalidString(self):
        t = Triangle("a", 5, 6)
        self.assertFalse(t.isvalid())

    def test_invalidSymbol(self):
        t = Triangle("&", 5, 6)
        self.assertFalse(t.isvalid())

    def test_invalidFloat(self):
        t = Triangle(3.5, 5, 6)
        self.assertFalse(t.isvalid())

    def test_invalidZero(self):
        t = Triangle(0, 5, 6)
        self.assertFalse(t.isvalid())

    def test_isoscelesGivenScalene(self):
        t = Triangle(1, 2, 3)
        self.assertFalse(t.isisosceles())

    def test_isoscelesGivenEquilateral(self):
        t = Triangle(2, 2, 2)
        self.assertFalse(t.isisosceles())

    def test_isoscelesSide1andSide2(self):
        t = Triangle(2, 2, 3)
        self.assertTrue(t.isisosceles())

    def test_isoscelesSide2andSide3(self):
        t = Triangle(2, 3, 3)
        self.assertTrue(t.isisosceles())

    def test_isoscelesSide1andSide3(self):
        t = Triangle(2, 3, 2)
        self.assertTrue(t.isisosceles())

    def test_isoscelesGivenStrings(self):
        t = Triangle("a", "b", "c")
        self.assertFalse(t.isisosceles())

    def test_Equilateral(self):
        t = Triangle(2, 2, 2)
        self.assertTrue(t.isequilateral())

    def test_equilateralGivenStrings(self):
        t = Triangle("a", "b", "c")
        self.assertFalse(t.isequilateral())

    def test_equilateralRounded(self):
        t = Triangle(3, 3, 3.1)
        self.assertFalse(t.isequilateral())

    def test_equilateralGivenScalene(self):
        t = Triangle(1, 2, 3)
        self.assertFalse(t.isequilateral())

    def test_equilateralGivenIsosceles(self):
        t = Triangle(2, 2, 3)
        self.assertFalse(t.isequilateral())

    def test_scaleneGivenEquilateral(self):
        t = Triangle(2, 2, 2)
        self.assertFalse(t.isscalene())

    def test_scaleneGivenIsosceles(self):
        t = Triangle(2, 2, 3)
        self.assertFalse(t.isscalene())

    def test_Scalene(self):
        t = Triangle(1, 2, 3)
        self.assertTrue(t.isscalene())

    def test_scaleneGivenStrings(self):
        t = Triangle("a", "b", "c")
        self.assertFalse(t.isscalene())
