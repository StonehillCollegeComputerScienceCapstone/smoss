import json
from flask import *
from DataAggregator import DataAggregator
from Config import Config

class Graph:

    def __init__(self, results):
        self.config = Config()
        if isinstance(results, list):
            self.nameList = DataAggregator().populateNames(results)
            self.graph = self.getJsonObject(results)
        else:
            pass

    # Return false if list contains results with different assignment numbers
    def getValidResults(self, results):
        if results and isinstance(results, list):
            for result in results:
                if not (result.assignmentNumber == results[0].assignmentNumber):
                    return False
        else:
            return False
        return True

    # Return an array of dictionary objects containing the names of every student
    def getNodes(self, results):
        cpNames = []
        currentYear = "currentYear"
        previousYear = "previousYear"
        nameOne = ""
        nameTwo = ""
        nameOnePrevious = False
        nameTwoPrevious = False
        for result in results:
            nameOne = result.getNameOne()
            nameTwo = result.getNameTwo()
            nameOnePrevious = result.nameOneIsPrevious()
            nameTwoPrevious = result.nameTwoIsPrevious()

            if nameOnePrevious and [nameOne, previousYear] not in cpNames:
                cpNames.append([nameOne, previousYear])
            elif not nameOnePrevious and [nameOne, currentYear] not in cpNames:
                cpNames.append([result.getNameOne(), currentYear])

            if nameTwoPrevious and [nameTwo, previousYear] not in cpNames:
                cpNames.append([nameTwo, previousYear])
            elif not nameTwoPrevious and [nameTwo, currentYear] not in cpNames:
                cpNames.append([nameTwo, currentYear])

        nodes = []
        index = 1
        for name in cpNames:
            nodes.append({"id": self.nameList.index(name[0]), "value": 5, "label": name[0], "group": name[1]})
            index = index + 1
        return nodes

    # Return an array of dictionary objects representing edges in the graph
    def getEdges(self, results):
        edges = []

        for result in results:
            edgeFrom = self.nameList.index(result.getNameOne())
            edgeTo = self.nameList.index(result.getNameTwo())
            value = self.getGreaterPercentage(result)
            valueString = str(value) + "% matched"
            edges.append({"from": edgeFrom, "to": edgeTo, "value": value, "title": valueString, "assignment": result.assignmentNumber, "color": 0})
        return edges

    # Return the greater value between two percentages
    def getGreaterPercentage(self, result):
        return max(result.fileOnePercent, result.fileTwoPercent)

    # return a JsonObject based off of list of moss results
    def getJsonObject(self, results):
        graph = ({"nodes": self.getNodes(results), "edges": self.getEdges(results) })
        return json.loads(json.dumps(graph))

