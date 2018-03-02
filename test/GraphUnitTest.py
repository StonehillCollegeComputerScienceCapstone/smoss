import unittest
from Graph import Graph
from Result import Result
import json

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.results = []
        self.validURL = "http://moss.stanford.edu/results/11690537/" # Change this when URL expires
        self.results.append(Result(1, "Matt", "Armen", self.validURL, 90, 70, 20))
        self.results.append(Result(1, "Stephen", "Sam", self.validURL, 80, 43, 77))
        self.results.append(Result(1, "Matt", "Tori", self.validURL, 33, 70, 45))
        self.results.append(Result(1, "Armen", "Tori", self.validURL, 50, 34, 5))
        self.results.append(Result(1, "Matt", "Stephen", self.validURL, 76, 79, 20))
        self.results.append(Result(1, "Matt", "Will", self.validURL, 90, 88, 100))
        self.results.append(Result(1, "Armen", "Sam", self.validURL, 10, 6, 2))

        self.g = Graph(self.results)

# Testing validResults

    # Results should be an array of Result
    def test_isValidResults(self):
        self.assertTrue(self.g.validResults(self.results))

    # Results should not be empty
    def test_isEmptyResults(self):
        results = []
        self.assertFalse(self.g.validResults(results))

    def testAssignmentNumber(self):
        self.results.append(Result(2, "Tori", "Will", self.validURL, 25, 33, 95))
        self.assertFalse(self.g.validResults(self.results))
        self.results.pop()

#Testing getNames

    def testGetNamesReturnsList(self):
        names = self.g.getNodes(self.results)
        self.assertTrue(isinstance(names, list))

    def testNamesGreaterThan1(self):
        names = self.g.getNodes(self.results)
        self.assertGreater(len(names), 1)

#Testing chooseGreaterPercent

    def testChooseGreaterPercent(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertEqual(self.g.chooseGreaterPercent(r), 90)
        self.assertNotEqual(self.g.chooseGreaterPercent(r), 70)
        self.assertNotEqual(self.g.chooseGreaterPercent(r), 20)
        self.assertNotEqual(self.g.chooseGreaterPercent(r), 55)

    def testChooseGreaterPercentNotString(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), str))
        self.assertNotEqual(self.g.chooseGreaterPercent(r), '90')

    def testChooseGreaterPercentNotFloat(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), float))

    def testChooseGreaterPercentNotNone(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertTrue(self.g.chooseGreaterPercent(r))

    def testChooseGreaterPercentNotList(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), list))

    def testChooseGreaterPercentNotDict(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), dict))

    def testChooseGreaterPercentInteger(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertTrue(isinstance(self.g.chooseGreaterPercent(r), int))

#Test createJSON
    def testJSON(self):
        JSON = self.g.getJsonObject(self.results)
        self.assertTrue(isinstance(JSON, dict))






if __name__ == '__main__':
    unittest.main()


