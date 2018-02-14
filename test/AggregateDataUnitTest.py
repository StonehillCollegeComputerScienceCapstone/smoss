import unittest
from Result import Result
from AggregateData import AggregateData


class MyTestCase(unittest.TestCase):

    def test_isValidArray(self):
        results = []
        result1 = Result(1, "file1", "file2", "http://moss.stanford.edu/results/299782671/", 90, 70, 20)
        result2 = Result(2, "file1", "file2", "http://moss.stanford.edu/results/299782670/", 50, 10, 5)
        results.append(result1)
        results.append(result2)

        ag = AggregateData()

        self.assertTrue(ag.isValid(results))

    def test_isEmptyArray(self):
        results = []
        ag = AggregateData()
        self.assertFalse(ag.isValid(results))

    def test_averagePercentArrayEmpty(self):
        ag = AggregateData()
        percents = []
        self.assertFalse(ag.percentsValid(percents))

    def test_averagePercentArrayExists(self):
        ag = AggregateData()
        percents = [1, 2, 3]
        self.assertTrue(ag.percentsValid(percents)

    # Percents should be only numbers
    # Percents should be only positive

    def test_averagePercentRoundUp(self):
        ag = AggregateData()
        percents = [55, 28, 90, 70]
        self.assertEqual(ag.calculateAveragePercent(percents), 61)

    def test_averagePercentRoundDown(self):
        ag = AggregateData()
        percents = [55, 28, 90, 70, 73]
        self.assertEqual(ag.calculateAveragePercent(percents), 63)












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

    def test_isValidReturnObject(self):
        ag = AggregateData()
        jsonObject = {}
        self.assertIsInstance(ag.generateJSON(jsonObject), json)

    def test_isValidReturnNames(self):
        ag = AggregateData()
        jsonObject = {}
        data = ag.generateJSON(jsonObject)
        self.assertIsNotNone(data.names)

    def test_isValidReturnPercentages(self):
        ag = AggregateData()
        jsonObject = {}
        data = ag.generateJSON(jsonObject)
        self.assertIsNotNone(data.percentages)

    def test_isValidReturnAverages(self):
        ag = AggregateData()
        jsonObject = {}
        data = ag.generateJSON(jsonObject)
        self.assertIsNotNone(data.averages)


if __name__ == '__main__':
    unittest.main()
