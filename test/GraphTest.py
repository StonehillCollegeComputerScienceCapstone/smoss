import unittest
from Config import Config
from Graph import Graph
from Result import Result


class MyTestCase(unittest.TestCase):

    # -getValidResults()  # Results should be an array of Result
    # -getValidResults()  # Results should not be empty
    # -getValidResults() # All assignment numbers should match
    # -getNodes()  #tests that it returns a list
    # -getNodes() #Test that it returns a list of dictionaries
    # -getNodes() #test that it is greater than 1
    # -getNodes() #Test that each node has an ID attribute
    # -getNodes() #Test that each node has a value attribute
    # -getNodes() #Test that each node has a label attribute
    # -getNodes() #Test that each node has an group attribute
    # -getNodes() #Test that you get currentYear nodes
    # -getNodes() Test there are no current year node in a data set of all previous year results
    # -getNodes() #Test that you get previous nodes
    # -getNodes() Test there are no previous year node in a data set of all current year results
    # -getNodes() #Test no duplicate named nodes
    # -getGreaterPercentage() #with integers
    # -getGreaterPercentage() #returning an integer not a string
    # -getGreaterPercentage() #not returning a float
    # -getGreaterPercentage() #returning a value
    # -getGreaterPercentage() #returning a value which is not a list
    # -getGreaterPercentage() #returning a value which is not a dictionary object
    # -getGreaterPercentage() #returning an Integer for a value
    # -Test JSON format #Test that JSON is a dictionary
    # -Test JSON format #Test that JSON only has nodes and edges
    # -Test JSON format #Test that JSON contains nodes
    # -Test JSON format #Test that JSON contains edges
    # -Test JSON format #Test that graph has at least two nodes and at least one edge
    # -Test JSON format #Test that graph does not contain more than [(nodes)*(nodes-1)]/2 edges
    # -Test JSON format #Test that graph contains nodes which is a list of dictionaries
    # -Test JSON format #Test that graph contains edges which is a list of dictionaries
    # -Test JSON format #Test that the nodes are in valid format
    # -Test JSON format #Test that the edges are in valid format
    # -getEdges() #Test number of edges is the same as number of results
    # -getEdges() #Test that it returns a list
    # -getEdges() #Test that it is a list of dictionaries
    # -getEdges() #Tests that it is greater than 1
    # -getEdges() #Test that each edge has a from attribute
    # -getEdges() #Test edge 'from' is int
    # -getEdges() #Test that each edge has a to attribute
    # -getEdges() #Test edge 'to' is int
    # -getEdges() #Test that each edge has a value attribute
    # -getEdges() #Test edge 'value' is int
    # -getEdges() Test edge 'value' is positive
    # -getEdges() #Test that each edge has a title attribute
    # -getEdges() #Test edge 'title' is str
    # -getEdges() #Test that each edge has an assignment attribute
    # -getEdges() #Test edge 'assignment' is int
    # -getEdges() #Test that each edge has a color attribute

    def setUp(self):
        self.config = Config()
        self.validURL = self.config.getPalindrome()

        self.results = []
        self.results.append(Result(1, "matt_SquareRoot.java", "armen_SquareRoot.java", self.validURL, 90, 70, 20))
        self.results.append(Result(1, "stephen_SquareRoot.java", "previous_sam_SquareRoot.java", self.validURL, 80, 43, 77))
        self.results.append(Result(1, "matt_SquareRoot.java", "previous_tori_SquareRoot.java", self.validURL, 33, 70, 45))
        self.results.append(Result(1, "armen_SquareRoot.java", "previous_tori_SquareRoot.java", self.validURL, 50, 34, 5))
        self.results.append(Result(1, "matt_SquareRoot.java", "stephen_SquareRoot.java", self.validURL, 76, 79, 20))
        self.results.append(Result(1, "matt_SquareRoot.java", "will_SquareRoot.java", self.validURL, 90, 88, 100))
        self.results.append(Result(1, "previous_bob_SquareRoot.java", "previous_nick_SquareRoot.java", self.validURL, 55, 42, 81))
        self.results.append(Result(1, "previous_nick_SquareRoot.java", "previous_sam_SquareRoot.java", self.validURL, 34, 21, 44))

        self.allCurrent = []
        self.allCurrent.append(Result(1, "matt_SquareRoot.java", "armen_SquareRoot.java", self.validURL, 90, 70, 20))
        self.allCurrent.append(Result(1, "will_SquareRoot.java", "stephen_SquareRoot.java", self.validURL, 50, 40, 10))
        self.allCurrent.append(Result(1, "tori_SquareRoot.java", "matt_SquareRoot.java", self.validURL, 55, 65, 53))
        self.allCurrent.append(Result(1, "armen_SquareRoot.java", "will_SquareRoot.java", self.validURL,65, 71, 100))

        self.allPrevious = []
        self.allPrevious.append(Result(1, "previous_matt_SquareRoot.java", "previous_armen_SquareRoot.java", self.validURL, 90, 70, 20))
        self.allPrevious.append(Result(1, "previous_will_SquareRoot.java", "previous_stephen_SquareRoot.java", self.validURL, 50, 40, 10))
        self.allPrevious.append(Result(1, "previous_tori_SquareRoot.java", "previous_matt_SquareRoot.java", self.validURL, 55, 65, 53))
        self.allPrevious.append(Result(1, "previous_armen_SquareRoot.java", "previous_tori_SquareRoot.java", self.validURL,65, 71, 100))

        self.graph = Graph(self.results)

        self.JSON = self.graph.getJsonObject(self.results)
#
# getValidResults()
#
    # Results should be an array of Result
    def test_ValidResults(self):
        self.assertTrue(self.graph.getValidResults(self.results))

    # Results should not be empty
    def test_EmptyResults(self):
        results = []
        self.assertFalse(self.graph.getValidResults(results))

    # All assignment numbers should match
    def test_AssignmentNumber(self):
        self.results.append(Result(2, "Tori", "Will", self.validURL, 25, 33, 95))
        self.assertFalse(self.graph.getValidResults(self.results))
        self.results.pop()
#
# getNodes()
#

    #Test that it returns a list
    def test_GetNamesReturnsList(self):
        names = self.graph.getNodes(self.results)
        self.assertTrue(isinstance(names, list))

    #Test that it is a list of dictionaries
    def test_ListOfDictionaries(self):
        names = self.graph.getNodes(self.results)
        dicts = True
        for name in names:
            if not isinstance(name, dict):
                dicts = False
        self.assertTrue(dicts)

    #Tests that it is greater than 1
    def test_NamesGreaterThan1(self):
        names = self.graph.getNodes(self.results)
        self.assertGreater(len(names), 1)

    #Test that each node has an id attribute
    def test_ID(self):
        names = self.graph.getNodes(self.results)
        hasID = True
        for name in names:
            if 'id' not in name:
                hasID = False
        self.assertTrue(hasID)

    #Test that each node has a value attribute
    def test_Value(self):
        names = self.graph.getNodes(self.results)
        hasValue = True
        for name in names:
            if 'value' not in name:
                hasValue = False
        self.assertTrue(hasValue)

    #Test that each node has a label attribute
    def test_Label(self):
        names = self.graph.getNodes(self.results)
        hasLabel = True
        for name in names:
            if 'label' not in name:
                hasLabel = False
        self.assertTrue(hasLabel)

    #Test that each node has a group attribute
    def test_Group(self):
        names = self.graph.getNodes(self.results)
        hasGroup = True
        for name in names:
            if 'group' not in name:
                hasGroup = False
        self.assertTrue(hasGroup)

    #Test that you get current year nodes
    def test_CurrentYearNodes(self):
        names = self.graph.getNodes(self.results)
        curr = False
        for name in names:
            if name["group"] == "currentYear":
                curr = True
        self.assertTrue(curr)

    # Test there are no current year node in a data set of all previous year results
    def test_NoCurrentYearNodes(self):
        names = self.graph.getNodes(self.allPrevious)
        curr = False
        for name in names:
            if name["group"] == "currentYear":
                curr = True
        self.assertFalse(curr)

    #Test that you get previous year nodes
    def test_PreviousYearNodes(self):
        names = self.graph.getNodes(self.results)
        prev = False
        for name in names:
            if name["group"] == "previousYear":
                prev = True
        self.assertTrue(prev)

    #Test there are no previous year node in a data set of all current year results
    def test_NoPreviousYearNodes(self):
        names = self.graph.getNodes(self.allCurrent)
        prev = False
        for name in names:
            if name["group"] == "previousYear":
                prev = True
        self.assertFalse(prev)


    #Test no duplicate named nodes
    def test_NoDuplicateNames(self):
        names = self.graph.getNodes(self.results)
        seenNames = []
        duplicateNames = False
        for name in names:
            if name["label"] not in seenNames:
                seenNames.append(name["label"])
            else:
                duplicateNames = True
        self.assertFalse(duplicateNames)


#
# getGreaterPercentage()
#

    # getGreaterPercentage() with integers
    def test_ChooseGreaterPercent(self):
        result = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertEqual(self.graph.getGreaterPercentage(result), 90)
        self.assertNotEqual(self.graph.getGreaterPercentage(result), 70)
        self.assertNotEqual(self.graph.getGreaterPercentage(result), 20)
        self.assertNotEqual(self.graph.getGreaterPercentage(result), 55)

    # getGreaterPercentage() returning an integer not a string
    def test_ChooseGreaterPercentNotString(self):
        result = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.graph.getGreaterPercentage(result), str))
        self.assertNotEqual(self.graph.getGreaterPercentage(result), '90')

    # getGreaterPercentage() not returning a float
    def test_ChooseGreaterPercentNotFloat(self):
        result = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.graph.getGreaterPercentage(result), float))

    #getGreaterPercentage() returning a value
    def test_ChooseGreaterPercentNotNone(self):
        result = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertTrue(self.graph.getGreaterPercentage(result))

    #getGreaterPercentage() returning a value which is not a list
    def test_ChooseGreaterPercentNotList(self):
        result = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.graph.getGreaterPercentage(result), list))

    #getGreaterPercentage() returning a value which is not a dictionary object
    def test_ChooseGreaterPercentNotDict(self):
        result = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertFalse(isinstance(self.graph.getGreaterPercentage(result), dict))

    #getGreaterPercentage() returning an Integer for a value
    def test_ChooseGreaterPercentInteger(self):
        result = Result(1, "Matt", "Armen", self.validURL, 90, 70, 20)
        self.assertTrue(isinstance(self.graph.getGreaterPercentage(result), int))
#
#Test JSON format
#
    #Test that JSON is a dictionary
    def test_JSONisDict(self):
        self.assertTrue(isinstance(self.JSON, dict))

    #Test that JSON only has nodes and edges
    def test_JSONMaxSize(self):
        self.assertTrue(len(self.JSON) == 2)

    #Test that JSON contains nodes
    def test_JSONForNodes(self):
        self.assertTrue('nodes' in self.JSON)

    #Test that JSON contains edges
    def test_JSONForEdges(self):
        self.assertTrue('edges' in self.JSON)

    # Test that graph has at least two nodes and at least one edge
    def test_GraphMinimumSize(self):
        self.assertTrue(len(self.JSON['nodes']) >= 2)
        self.assertTrue(len(self.JSON['edges']) >= 1)

    #Test that graph does not contain more than [(nodes)*(nodes-1)]/2 edges
    def test_GraphMaxEdges(self):
        numNodes = len(self.JSON['nodes'])
        maxEdges = (numNodes * (numNodes - 1)) / 2
        self.assertTrue(len(self.JSON['edges']) < maxEdges)

    #Test that graph contains nodes which is a list of dictionaries
    def test_NodesIsListOfDict(self):
        self.assertTrue(isinstance(self.JSON['nodes'], list))
        nodes = self.JSON['nodes']
        for node in nodes:
            self.assertTrue(isinstance(node, dict))

    # Test that graph contains edges which is a list of dictionaries
    def test_EdgesIsListOfDict(self):
        self.assertTrue(isinstance(self.JSON['edges'], list))
        edges = self.JSON['edges']
        for edge in edges:
            self.assertTrue(isinstance(edge, dict))

    #Test that the nodes are in valid format
    def test_NodeFormat(self):
        nodes = self.JSON['nodes']
        for node in nodes:
            self.assertTrue('id' in node)
            self.assertTrue('value' in node)
            self.assertTrue('label' in node)
            self.assertTrue(isinstance(node['label'], str))
            self.assertTrue('group' in node)

    #Test that the edges are in valid format
    def test_EdgeFormat(self):
        edges = self.JSON['edges']
        for edge in edges:
            self.assertTrue('from' in edge)
            self.assertTrue('to' in edge)
            self.assertTrue('value' in edge)
            self.assertTrue('title' in edge)
            self.assertTrue(isinstance(edge['title'], str))
            self.assertTrue('assignment' in edge)
            self.assertTrue('color' in edge)

#
# getEdges()
#

    #Test number of edges is the same as number of results
    def test_NumOfEdges(self):
        edges = self.graph.getEdges(self.results)
        self.assertTrue(len(edges) == len(self.results))

    #test that it returns a list
    def test_getEdgesReturnsList(self):
        edges = self.graph.getEdges(self.results)
        self.assertTrue(isinstance(edges, list))

    #Test that it is a list of dictionaries
    def test_getEdgesReturnsListOfDictionaries(self):
        edges = self.graph.getEdges(self.results)
        dicts = True
        for edge in edges:
            if not isinstance(edge, dict):
                dicts = False
        self.assertTrue(dicts)

    #Tests that it is greater than 1
    def test_EdgesGreaterThan1(self):
        edges = self.graph.getEdges(self.results)
        self.assertGreater(len(edges), 1)

    #Test that each edge has a from attribute
    def test_edgeHasFrom(self):
        edges = self.graph.getEdges(self.results)
        hasFrom = True
        for edge in edges:
            if 'from' not in edge:
                hasFrom = False
        self.assertTrue(hasFrom)

    #Test edge 'from' is int
    def test_edgeFromIsInt(self):
        edges = self.graph.getEdges(self.results)
        fromInt = True
        for edge in edges:
            if not isinstance(edge["from"], int):
                fromInt = False
        self.assertTrue(fromInt)

    #Test that each edge has a to attribute
    def test_edgeHasTo(self):
        edges = self.graph.getEdges(self.results)
        hasTo = True
        for edge in edges:
            if 'to' not in edge:
                hasTo = False
        self.assertTrue(hasTo)

    # Test edge 'to' is int
    def test_edgeToIsInt(self):
        edges = self.graph.getEdges(self.results)
        toInt = True
        for edge in edges:
            if not isinstance(edge["to"], int):
                toInt = False
        self.assertTrue(toInt)

    #Test that each edge has a value attribute
    def test_edgeHasValue(self):
        edges = self.graph.getEdges(self.results)
        hasValue = True
        for edge in edges:
            if 'value' not in edge:
                hasValue = False
        self.assertTrue(hasValue)

    # Test edge 'value' is int
    def test_edgeValueIsInt(self):
        edges = self.graph.getEdges(self.results)
        valueInt = True
        for edge in edges:
            if not isinstance(edge["value"], int):
                valueInt = False
        self.assertTrue(valueInt)


    # Test edge 'value' is positive
    def test_edgeValueIsPositive(self):
        edges = self.graph.getEdges(self.results)
        valueInt = True
        for edge in edges:
            if edge["value"] <= -1:
                valueInt = False
        self.assertTrue(valueInt)

    #Test that each edge has a title attribute
    def test_edgeHasTitle(self):
        edges = self.graph.getEdges(self.results)
        hasTitle = True
        for edge in edges:
            if 'value' not in edge:
                hasTitle = False
        self.assertTrue(hasTitle)

    # Test edge 'title' is string
    def test_edgeTitleIsString(self):
        edges = self.graph.getEdges(self.results)
        titleStr = True
        for edge in edges:
            if not isinstance(edge["title"], str):
                titleStr = False
        self.assertTrue(titleStr)

    #Test that each edge has a assignment attribute
    def test_edgeHasAssignmentNumber(self):
        edges = self.graph.getEdges(self.results)
        hasAsgNum = True
        for edge in edges:
            if 'assignment' not in edge:
                hasAsgNum = False
        self.assertTrue(hasAsgNum)

    # Test edge 'assignment' is string
    def test_edgeAsgNumIsString(self):
        edges = self.graph.getEdges(self.results)
        asgStr = True
        for edge in edges:
            if not isinstance(edge["assignment"], str):
                asgStr = False
        self.assertTrue(asgStr)

    #Test that each edge has a color attribute
    def test_edgeHasColor(self):
        edges = self.graph.getEdges(self.results)
        hasColor = True
        for edge in edges:
            if 'color' not in edge:
                hasColor = False
        self.assertTrue(hasColor)

    #Test there are multiple assignments
    def test_MultipleAssignments(self):
        results = self.results
        results.append(Result(2, "matt_Poker.java", "armen_Poker.java", self.validURL, 90, 70, 20))
        results.append(Result(2, "will_Poker.java", "stephen_Poker.java", self.validURL, 50, 40, 10))
        results.append(Result(2, "tori_Poker.java", "matt_Poker.java", self.validURL, 55, 65, 53))
        results.append(Result(2, "tori_Poker.java", "armen_Poker.java", self.validURL,65, 71, 100))
        nodes = self.graph.getNodes(results)
        edges = self.graph.getEdges(results)
        multipleAssignments = False
        for edge in edges:
            if edge["assignment"] != edges[0]["assignment"]:
                multipleAssignments = True
        self.assertTrue(multipleAssignments)




if __name__ == '__main__':
    unittest.main()

