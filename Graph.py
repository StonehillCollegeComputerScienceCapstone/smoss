import json
import random
from flask import *
from Result import Result
from DataAggregator import DataAggregator
from Config import Config
from ResultsSorter import ResultsSorter


class Graph:

    def __init__(self, results):
        self.config = Config()
        if isinstance(results, list):
            self.graph = self.getJsonObject(results)
        else:
            pass
    #
    # method will return false if list contains results with different assignment numbers
    #
    def getValidResults(self, results):
        if results and isinstance(results, list):
            for result in results:
                if not (result.assignmentNumber == results[0].assignmentNumber):
                    return False
        else:
            return False
        return True
    #
    # Return an array of dictionary objects containing the names of every student
    #
    def getNodes(self, results):
        sorter = ResultsSorter()
        values = sorter.get_csv()
        cpNames = []
        for value in values:
            if "previous" in value["FileName1"]:
                if ([value["User1"], 'p']) not in cpNames:
                    cpNames.append([value["User1"], 'p'])
            else:
                if ([value["User1"], 'c']) not in cpNames:
                    cpNames.append([value["User1"], 'c'])
            if "previous" in value["FileName2"]:
                if ([value["User2"], 'p']) not in cpNames:
                    cpNames.append([value["User2"], 'p'])
            else:
                if ([value["User2"], 'c']) not in cpNames:
                    cpNames.append([value["User2"], 'c'])
        names = []
        index = 1
        for name in cpNames:
            if name[1] is 'c':
                names.append({"id": index, "value": 5, "label": name[0], "group": 'currentYear'})
            elif name[1] is 'p':
                names.append({"id": index, "value": 5, "label": name[0], "group": 'previousYear'})
            index = index + 1
        return names

    #
    # return index of passed variable name in list of DataAggregator
    #
    def getNodeIndex(self, name, results):
        nameList = DataAggregator().populateNames(results)
        index = 1
        for n in nameList:
            if n == name:
                return index
            index = index + 1
        return -1
    #
    # Return an array of dictionary objects representing edges in the graph
    #
    def getEdges(self, results):
        edges = []
        assignments = []
        for result in results:
            if result.assignmentNumber not in assignments:
                assignments.append(result.assignmentNumber)
            edgeFrom = self.getNodeIndex(result.fileOne, results)
            edgeTo = self.getNodeIndex(result.fileTwo, results)
            value = self.getGreaterPercentage(result)
            valueString = str(value) + "% matched"
            edges.append({"from": edgeFrom, "to": edgeTo, "value": value, "title": valueString, "assignment": result.assignmentNumber, "color": 0})
        return edges
    #
    # Return the greater value between two percentages
    #
    def getGreaterPercentage(self, result):
        return max(result.fileOnePercent, result.fileTwoPercent)
    #
    # return a JsonObject based off of list of moss results
    #
    def getJsonObject(self, results):
        graph = ({"nodes": self.getNodes(results), "edges": self.getEdges(results) })
        return json.loads(json.dumps(graph))


if __name__ == '__main__': main()