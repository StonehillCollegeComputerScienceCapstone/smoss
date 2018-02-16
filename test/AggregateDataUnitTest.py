import unittest
from Result import Result
from AggregateData import AggregateData


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ag = AggregateData()
        self.results = []
        result1 = Result(1, "file1", "file2", "http://moss.stanford.edu/results/299782671/", 90, 70, 20)
        result2 = Result(2, "file1", "file3", "http://moss.stanford.edu/results/299782670/", 50, 10, 5)
        self.results.append(result1)
        self.results.append(result2)
        self.names = self.ag.populateNames(self.results)

#
# validResults()
#
    # Results should be an array of Result
    def test_isValidResults(self):
        self.assertTrue(self.ag.validResults(self.results))

    # Results should not be empty
    def test_isEmptyResults(self):
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
    # Average should return the correct value
    def test_averagePercentCorrect(self):
        percents = [1, 2, 3]
        self.assertEqual(self.ag.average(percents), 2)
        percents = [2, 2, 2]
        self.assertEqual(self.ag.average(percents), 2)

    # Average should be an int
    def test_averagePercentReturnInt(self):
        percents = [1, 2, 3]
        self.assertTrue(isinstance(self.ag.average(percents), int))

    # Average should round up when > .5
    def test_averagePercentRoundUp(self):
        percents = [55, 28, 90, 70]
        self.assertEqual(self.ag.average(percents), 61)

    # Average should round up when = .5
    def test_averagePercentRoundHalf(self):
        percents = [3.5, 3.5, 3.5]
        self.assertEqual(self.ag.average(percents), 4)

    # Average should round down when < .5
    def test_averagePercentRoundDown(self):
        percents = [55, 28, 90, 70, 73]
        self.assertEqual(self.ag.average(percents), 63)

    # Average should not be more than 100
    def test_averagePercentUpper(self):
        percents = [55, 28, 90, 70, 73]
        self.assertLessEqual(self.ag.average(percents), 100)

    # Average should not be negative
    def test_averagePercentLower(self):
        percents = [55, 28, 90, 70, 73]
        self.assertGreaterEqual(self.ag.average(percents), 0)

#
# totalLines()
#
    # Total lines should be the correct value
    def test_totalLinesCorrect(self):
        lines = [1, 2, 3]
        self.assertEqual(self.ag.total(lines), 6)

    # Total lines should be greater than or equal to 0
    def test_totalLinesLower(self):
        lines = [1, 2, 3]
        self.assertGreaterEqual(self.ag.total(lines), 0)

#
# populateNames()
#
    # Should return an array
    def test_returnsList(self):
        self.assertTrue(isinstance(self.names, list))

    # Should return an array of strings
    def test_returnsListStrings(self):
        for name in self.names:
            self.assertTrue(isinstance(name, str))

    # Should return an array of the correct names
    def test_returnsListNames(self):
        self.assertTrue(self.names[0] == "file1")
        self.assertTrue(self.names[1] == "file2")
        self.assertTrue(self.names[2] == "file3")

#
# parsePercents()
#
    # Should return an array
    def test_returnsListPercents(self):
        self.assertTrue(isinstance(self.ag.parsePercents(self.results, "file1"), list))
        self.assertTrue(isinstance(self.ag.parsePercents(self.results, "file2"), list))
        self.assertTrue(isinstance(self.ag.parsePercents(self.results, "file3"), list))

#
# parseLines()
#
    # Should return an array
    def test_returnsListLines(self):
        self.assertTrue(isinstance(self.ag.parseLines(self.results, "file1"), list))
        self.assertTrue(isinstance(self.ag.parseLines(self.results, "file2"), list))
        self.assertTrue(isinstance(self.ag.parseLines(self.results, "file3"), list))

#
# sort()
#


if __name__ == '__main__':
    unittest.main()
