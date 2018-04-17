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
        for result in results:
            if result.nameOneIsPrevious() and [result.getNameOne(), 'p'] not in cpNames:
                cpNames.append([result.getNameOne(), 'p'])
            elif not result.nameOneIsPrevious() and [result.getNameOne(), 'c'] not in cpNames:
                cpNames.append([result.getNameOne(), 'c'])
            if result.nameTwoIsPrevious() and [result.getNameTwo(), 'p'] not in cpNames:
                cpNames.append([result.getNameTwo(), 'p'])
            elif not result.nameTwoIsPrevious() and [result.getNameTwo(), 'c'] not in cpNames:
                cpNames.append([result.getNameTwo(), 'c'])

        names = []
        index = 1
        for name in cpNames:
            if name[1] is 'c':
                names.append({"id": self.nameList.index(name[0]), "value": 5, "label": name[0], "group": 'currentYear'})
            elif name[1] is 'p':
                names.append({"id": self.nameList.index(name[0]), "value": 5, "label": name[0], "group": 'previousYear'})
            index = index + 1
        return names

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

