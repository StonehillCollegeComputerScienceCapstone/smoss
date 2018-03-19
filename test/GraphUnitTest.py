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

        self.JSON = self.g.getJsonObject(self.results)
#
# validResults()
#
    # Results should be an array of Result
    def test_ValidResults(self):
        self.assertTrue(self.g.validResults(self.results))

    # Results should not be empty
    def test_EmptyResults(self):
        results = []
        self.assertFalse(self.g.validResults(results))

    def test_AssignmentNumber(self):
        self.results.append(Result(2, "Tori", "Will", self.validURL, 25, 33, 95))
        self.assertFalse(self.g.validResults(self.results))
        self.results.pop()
#
# getNodes()
#
    def test_GetNamesReturnsList(self):
        names = self.g.getNodes(self.results)
        self.assertTrue(isinstance(names, list))

    def test_NamesGreaterThan1(self):
        names = self.g.getNodes(self.results)
        self.assertGreater(len(names), 1)
#
# chooseGreaterPercent()
#

    #
    # chooseGreaterPercent() with integers
    #
    def test_ChooseGreaterPercent(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertEqual(self.g.chooseGreaterPercent(r), 90)
        self.assertNotEqual(self.g.chooseGreaterPercent(r), 70)
        self.assertNotEqual(self.g.chooseGreaterPercent(r), 20)
        self.assertNotEqual(self.g.chooseGreaterPercent(r), 55)
    #
    # chooseGreaterPercent() returning an integer not a string
    #
    def test_ChooseGreaterPercentNotString(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), str))
        self.assertNotEqual(self.g.chooseGreaterPercent(r), '90')

    #
    # chooseGreaterPercent() not returning a float
    #
    def test_ChooseGreaterPercentNotFloat(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), float))
    #
    #chooseGreaterPercent() returning a value
    #
    def test_ChooseGreaterPercentNotNone(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertTrue(self.g.chooseGreaterPercent(r))
    #
    #chooseGreaterPercent() returning a value which is not a list
    #
    def test_ChooseGreaterPercentNotList(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), list))
    #
    #chooseGreaterPercent() returning a value which is not a dictionary object
    #
    def test_ChooseGreaterPercentNotDict(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.g.chooseGreaterPercent(r), dict))
    #
    #chooseGreaterPercent() returning an Integer for a value
    #
    def test_ChooseGreaterPercentInteger(self):
        r = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertTrue(isinstance(self.g.chooseGreaterPercent(r), int))
#
#Test JSON format
#
    #
    #Test that JSON is a dictionary
    #
    def test_JSONisDict(self):
        self.assertTrue(isinstance(self.JSON, dict))
    #
    #Test that JSON only has nodes and edges
    #
    def test_JSONMaxSize(self):
        self.assertTrue(len(self.JSON) == 2)
    #
    #Test that JSON contains nodes
    #
    def test_JSONForNodes(self):
        self.assertTrue('nodes' in self.JSON)
    #
    #Test that JSON contains edges
    #
    def test_JSONForEdges(self):
        self.assertTrue('edges' in self.JSON)
    #
    #Test that graph has at least two nodes and at least one edge
    #
    def test_GraphMinimumSize(self):
        self.assertTrue(len(self.JSON['nodes']) >= 2)
        self.assertTrue(len(self.JSON['edges']) >= 1)
    #
    #Test that graph does not contain more than [(nodes)*(nodes-1)]/2 edges
    #
    def test_GraphMaxEdges(self):
        numNodes = len(self.JSON['nodes'])
        maxEdges = (numNodes * (numNodes - 1)) / 2
        self.assertTrue(len(self.JSON['edges']) < maxEdges)
    #
    #Test that graph contains nodes which is a list of dictionaries
    #
    def test_NodesIsListOfDict(self):
        self.assertTrue(isinstance(self.JSON['nodes'], list))
        nodes = self.JSON['nodes']
        for node in nodes:
            self.assertTrue(isinstance(node, dict))
    #
    # Test that graph contains edges which is a list of dictionaries
    #
    def test_EdgesIsListOfDict(self):
        self.assertTrue(isinstance(self.JSON['edges'], list))
        edges = self.JSON['edges']
        for edge in edges:
            self.assertTrue(isinstance(edge, dict))
    #
    #Test that the nodes are in valid format
    #
    def test_NodeFormat(self):
        nodes = self.JSON['nodes']
        for node in nodes:
            self.assertTrue('id' in node)
            self.assertTrue('value' in node)
            self.assertTrue('label' in node)
            self.assertTrue(isinstance(node['label'], str))
    #
    #Test that the edges are in valid format
    #
    def test_EdgeFormat(self):
        edges = self.JSON['edges']
        for edge in edges:
            self.assertTrue('from' in edge)
            self.assertTrue('to' in edge)
            self.assertTrue('value' in edge)
            self.assertTrue('title' in edge)
            self.assertTrue(isinstance(edge['title'], str))

if __name__ == '__main__':
    unittest.main()


