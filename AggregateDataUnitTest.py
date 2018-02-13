import unittest
import json
from AggregateData import AggregateData


class MyTestCase(unittest.TestCase):
    def test_sixFields(self):
        jsonObject = {}
        ag = AggregateData()

        self.assertTrue(ag.isValid(jsonObject))
        self.assertFalse(ag.isValid(jsonObject))

    def test_isJSON(self):
        array = []
        x = 10
        s = "Hello"
        jsonObject = {}

        ag = AggregateData()
        self.assertFalse(ag.isValid(array))
        self.assertFalse(ag.isValid(x))
        self.assertFalse(ag.isValid(s))
        self.assertTrue(ag.isValid(jsonObject))

    def test_averagePercent(self):
        ag = AggregateData()
        jsonObject = {}
        self.assertEqual(ag.calculateAveragePercent(jsonObject), 10)
        self.assertNotEqual(ag.calculateAveragePercent(jsonObject), 3)

    def test_validAveragePercentUpper(self):
        ag = AggregateData()
        jsonObject = {}
        self.assertLessEqual(ag.calculateAveragePercent(jsonObject), 100)

    def test_validAveragePercentLower(self):
        ag = AggregateData()
        jsonObject = {}
        self.assertGreaterEqual(ag.calculateAveragePercent(jsonObject), -1)

    def test_validTotalLinesMatchedLower(self):
        ag = AggregateData()
        jsonObject = {}
        self.assertGreaterEqual(ag.calculateTotalLines(jsonObject), -1)

    def test_isValidReturn(self):
        ag = AggregateData()
        jsonObject = {}
        self.assertIsInstance(ag.generateJSON(jsonObject), json)


if __name__ == '__main__':
    unittest.main()
