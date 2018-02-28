import unittest
from Graph import Graph
from Result import Result


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 1;


#     def setUp(self):
#         self.results = []
#         self.validURL = "http://moss.stanford.edu/results/11690537/" # Change this when URL expires
#         self.results.append(Result(1, "Matt", "Armen", self.validURL, 90, 70, 20))
#         self.results.append(Result(1, "Stephen", "Sam", self.validURL, 80, 43, 77))
#         self.results.append(Result(1, "Matt", "Tori", self.validURL, 33, 70, 45))
#         self.results.append(Result(1, "Armen", "Tori", self.validURL, 50, 34, 5))
#         self.results.append(Result(1, "Matt", "Stephen", self.validURL, 76, 79, 20))
#         self.results.append(Result(1, "Matt", "Will", self.validURL, 90, 88, 100))
#         self.results.append(Result(1, "Armen", "Sam", self.validURL, 10, 6, 2))
#
#         self.g = Graph(self.results)
#
# #
# # validResults()
# #
#     # Results should be an array of Result
#     def test_isValidResults(self):
#         self.assertTrue(self.g.validResults(self.results))
#
#     # Results should not be empty
#     def test_isEmptyResults(self):
#         results = []
#         self.assertFalse(self.g.validResults(results))
#
#     def testAssignmentNumber(self):
#         self.results.append(Result(2, "Tori", "Will", self.validURL, 25, 33, 95))
#         self.assertFalse(self.g.validResults(self.results))
#         self.results.pop()
#
# #Testing getNames
#     def testNamesGreaterThan1(self):
#         names = self.g.getNames(self.results)
#         self.assertGreater(len(names), 1)
#
# #Testing createNodes
#
#     def testGreaterThanOneNode(self):
#         self.assertGreater(self.g.graph.number_of_nodes(), 1)
#
#     def testNumNamesMatchNumNodes(self):
#         names = self.g.getNames(self.results)
#         self.assertEqual(len(names), self.g.graph.number_of_nodes())
#
#
# #Testing chooseGreaterPercent
#
#     def testChooseGreaterPercent(self):
#         r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
#         self.assertEqual(self.g.chooseGreaterPercent(r), 90)
#         self.assertNotEqual(self.g.chooseGreaterPercent(), 70)
#         self.assertNotEqual(self.g.chooseGreaterPercent(), 20)
#         self.assertNotEqual(self.g.chooseGreaterPercent(), 55)
#
#     def testChooseGreaterPercentNotString(self):
#         r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
#         self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), str))
#         self.assertNotEqual(self.g.chooseGreaterPercent(r), '90')
#
#     def testChooseGreaterPercentNotFloat(self):
#         r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
#         self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), float))
#
#     def testChooseGreaterPercentNotNone(self):
#         r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
#         self.assertTrue(self.g.chooseGreaterPercent(r))
#
#     def testChooseGreaterPercentNotList(self):
#         r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
#         self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), list))
#
#     def testChooseGreaterPercentNotDict(self):
#         r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
#         self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), dict))
#
#     def testChooseGreaterPercentInteger(self):
#         r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
#         self.assertTrue(isinstance(self.g.chooseGreaterPercent(r), int))
#
# #Testing createEdges
#
#     def testPositiveEdges(self):
#         self.assertGreater(self.g.graph.number_of_edges(), 0)
#
#     def testNumResultsMatchNumEdges(self):
#         self.assertEqual(len(self.results), self.g.graph.number_of_edges())
#
#     def testMaxEdges(self):
#         numNodes = self.g.graph.number_of_nodes()
#         maxNodes = ((numNodes*(numNodes-1))/2)
#         self.assertLessEqual(self.g.graph.number_of_edges(), maxNodes)
#
#     def testEdgeWeight(self):
#         self.assertEqual(self.g.graph["Matt"]["Armen"]['weight'], 90)
#         self.assertEqual(self.g.graph["Stephen"]["Sam"]['weight'], 80)
#         self.assertEqual(self.g.graph["Armen"]["Sam"]['weight'], 10)
#         self.assertNotEqual(self.g.graph["Armen"]["Tori"]['weight'], 34)

if __name__ == '__main__':
    unittest.main()


