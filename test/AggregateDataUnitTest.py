import unittest
from Result import Result
from AggregateData import AggregateData


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ag = AggregateData()

#
# validResults()
#
    def test_isValidArray(self):
        results = []
        result1 = Result(1, "file1", "file2", "http://moss.stanford.edu/results/299782671/", 90, 70, 20)
        result2 = Result(2, "file1", "file2", "http://moss.stanford.edu/results/299782670/", 50, 10, 5)
        results.append(result1)
        results.append(result2)

        self.assertTrue(self.ag.validResults(results))

    def test_isEmptyArray(self):
        results = []
        self.assertFalse(self.ag.validResults(results))

#
# validArray()
#
    # Array should not be empty
    def test_arrayEmpty(self):
        percents = []
        self.assertFalse(self.ag.validArray(percents))

    # Array should have values
    def test_arrayExists(self):
        percents = [1, 2, 3]
        self.assertTrue(self.ag.validArray(percents))

    # Array should only be numbers
    def test_arrayNumbers(self):
        percents = [1, 2, 3]
        self.assertTrue(self.ag.validArray(percents))

    # Array should not be decimals
    def test_arrayDecimals(self):
        percents = [1.5, 2.1, 3.99]
        self.assertFalse(self.ag.validArray(percents))

    # Array should not be None
    def test_arrayNone(self):
        percents = [None, None, None]
        self.assertFalse(self.ag.validArray(percents))

    # Array should not be Strings
    def test_arrayString(self):
        percents = ["Hello", "world", "!"]
        self.assertFalse(self.ag.validArray(percents))

    # Array should be positive
    def test_arrayNegative(self):
        percents = [-1, -2, -3]
        self.assertFalse(self.ag.validArray(percents))

    # Array should not have more than one data type
    def test_arrayMixed(self):
        percents = [-1, "Hello", None, 2, 4.5]
        self.assertFalse(self.ag.validArray(percents))

#
# validPercents()
#
    # Percents should not exceed 100
    def test_percentsUpperBound(self):
        percents = [99, 100, 1]
        self.assertTrue(self.ag.validArray(percents))
        percents = [101, 200, 500]
        self.assertFalse(self.ag.validArray(percents))
    
#
# averagePercent()
#
    def test_averagePercent(self):
        percents = [1, 2, 3]
        self.assertEqual(self.ag.averagePercent(percents), 2)
    
    def test_averagePercentRoundUp(self):
        percents = [55, 28, 90, 70]
        self.assertEqual(self.ag.averagePercent(percents), 61)

    def test_averagePercentRoundDown(self):
        percents = [55, 28, 90, 70, 73]
        self.assertEqual(self.ag.averagePercent(percents), 63)


    def test_validAveragePercentUpper(self):
        self.assertLessEqual(self.ag.calculateAveragePercent(jsonObject), 100)

    def test_validAveragePercentLower(self):
        self.assertGreaterEqual(self.ag.calculateAveragePercent(jsonObject), -1)

    def test_validTotalLinesMatchedLower(self):
        self.assertGreaterEqual(self.ag.calculateTotalLines(jsonObject), -1)

    def test_isValidReturnObject(self):
        self.assertIsInstance(self.ag.generateJSON(jsonObject), json)

    def test_isValidReturnNames(self):
        data = self.ag.generateJSON(jsonObject)
        self.assertIsNotNone(data.names)

    def test_isValidReturnPercentages(self):
        data = self.ag.generateJSON(jsonObject)
        self.assertIsNotNone(data.percentages)

    def test_isValidReturnAverages(self):
        data = self.ag.generateJSON(jsonObject)
        self.assertIsNotNone(data.averages)


if __name__ == '__main__':
    unittest.main()
