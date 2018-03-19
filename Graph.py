import json
from flask import *
from Config import Config
from Result import Result
from DataAggregator import DataAggregator

class Graph:

    def __init__(self, results=None):
        if isinstance(results, list):
            self.graph = self.getJsonObject(results)
        else:
            pass

    def validResults(self, results):
        if results and isinstance(results, list):
            assignmentNumber = results[0].assignment_number
            for result in results:
                if not (result.assignment_number == assignmentNumber):
                    return False
        else:
            return False
        return True

    # Return an array of dictionary objects containing the names of every student
    def getNodes(self, results):
        names = []
        ag = DataAggregator(results)
        nameList = ag.populateNames(results)

        count = 1
        for n in nameList:
            names.append({"id": count, "value": 5, "label": n})
            count = count + 1
        return names

    def getNodeIndex(self, name, results):
        ag = DataAggregator(results)
        nameList = ag.populateNames(results)
        id = 1
        for n in nameList:
            if n == name:
                return id
            id = id + 1
        return -1

    # Return an array of dictionary objects
    def getEdges(self, results):
        edges = []
        edgeFrom = -1
        edgeTo = -1
        nodes = self.getNodes(results)
        for result in results:
            edgeFrom = self.getNodeIndex(result.file_one, results)
            edgeTo = self.getNodeIndex(result.file_two, results)
            value = self.chooseGreaterPercent(result)
            valueString = str(value) + "% matched"
            edges.append({"from": edgeFrom, "to": edgeTo, "value": value, "title": valueString})
        return edges

    def chooseGreaterPercent(self, result):
        if result.file_one_percent > result.file_two_percent:
            return result.file_one_percent
        return result.file_two_percent

    def getJsonObject(self, results):
        graph = {}
        graph['nodes'] = self.getNodes(results)
        graph['edges'] = self.getEdges(results)

        jsonString = json.dumps(graph)
        return json.loads(jsonString)

    def print(self):
        print('Nodes:')
        for node in self.graph['nodes']:
            print(node)
        print('\nEdges:')
        for edge in self.graph['edges']:
            print(edge)

# Example data
def example():
    results = []
    config = Config()
    validURL = config.getHomevalue()
    results.append(Result(1, "Matt", "Armen", validURL, 90, 70, 20))
    results.append(Result(1, "Stephen", "Sam", validURL, 80, 43, 77))
    results.append(Result(1, "Matt", "Tori", validURL, 33, 70, 45))
    results.append(Result(1, "Armen", "Tori", validURL, 50, 34, 5))
    results.append(Result(1, "Matt", "Stephen", validURL, 76, 79, 20))
    results.append(Result(1, "Matt", "Will", validURL, 90, 88, 100))
    results.append(Result(1, "Armen", "Sam", validURL, 10, 6, 2))

    return results


def main():
    graph = Graph(example())
    #graph.print()

if __name__ == '__main__': main()