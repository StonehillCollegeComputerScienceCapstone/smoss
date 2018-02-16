import unittest
from Result import Result
from AggregateData import AggregateData


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ag = AggregateData()
        self.results = []
        result1 = Result(1, "Matt", "Armen", "http://moss.stanford.edu/results/299782671/", 90, 70, 20)
        result2 = Result(1, "Matt", "Sam", "http://moss.stanford.edu/results/299782671/", 80, 43, 77)
        result3 = Result(1, "Armen", "Sam", "http://moss.stanford.edu/results/299782670/", 12, 10, 8)
        result4 = Result(2, "Matt", "Armen", "http://moss.stanford.edu/results/299782671/", 33, 70, 45)
        result5 = Result(2, "Matt", "Sam", "http://moss.stanford.edu/results/299782671/", 16, 17, 15)
        result6 = Result(2, "Armen", "Sam", "http://moss.stanford.edu/results/299782670/", 50, 34, 5)
        result7 = Result(3, "Matt", "Armen", "http://moss.stanford.edu/results/299782671/", 76, 79, 20)
        result8 = Result(3, "Matt", "Sam", "http://moss.stanford.edu/results/299782671/", 90, 88, 100)
        result9 = Result(3, "Armen", "Sam", "http://moss.stanford.edu/results/299782670/", 10, 6, 2)
        self.results.append(result1)
        self.results.append(result2)
        self.results.append(result3)
        self.results.append(result4)
        self.results.append(result5)
        self.results.append(result6)
        self.results.append(result7)
        self.results.append(result8)
        self.results.append(result9)

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
        self.assertTrue(self.ag.validPercents(percents))
        percents = [101, 200, 500]
        self.assertFalse(self.ag.validPercents(percents))
    
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
# total()
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
        self.assertTrue("Matt" in self.names)
        self.assertTrue("Armen" in self.names)
        self.assertTrue("Sam" in self.names)

#
# parsePercents()
#
    # Should return an array
    def test_returnsListPercents(self):
        self.assertTrue(isinstance(self.ag.parsePercents(self.results, "Matt"), list))
        self.assertTrue(isinstance(self.ag.parsePercents(self.results, "Armen"), list))
        self.assertTrue(isinstance(self.ag.parsePercents(self.results, "Sam"), list))

    # Should return these values
    def test_returnsMaxPercents(self):
        # Matt
        percents = self.ag.parsePercents(self.results, "Matt")
        self.assertTrue(90 in percents)
        self.assertTrue(33 in percents)

        # Armen
        percents = self.ag.parsePercents(self.results, "Armen")
        self.assertTrue(70 in percents)
        self.assertTrue(70 in percents)
        self.assertTrue(79 in percents)

        # Sam
        percents = self.ag.parsePercents(self.results, "Sam")
        self.assertTrue(43 in percents)
        self.assertTrue(34 in percents)
        self.assertTrue(88 in percents)

#
# parseLines()
#
    # Should return an array
    def test_returnsListLines(self):
        self.assertTrue(isinstance(self.ag.parseLines(self.results, "Matt"), list))
        self.assertTrue(isinstance(self.ag.parseLines(self.results, "Armen"), list))
        self.assertTrue(isinstance(self.ag.parseLines(self.results, "Sam"), list))

#
# sort()
#


if __name__ == '__main__':
    unittest.main()
