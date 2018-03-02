from flask import *
from AggregateData import AggregateData

class Graph:

    def __init__(self, results):
        self.graph = self.getJsonObject(results)

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
    def getNames(self, results):
        names = []
        ag = AggregateData(results)
        nameList = ag.populateNames(results)

        for n in nameList:
            dict = {'name': n}
            names.append(dict)
        return names

    # Return an array of dictionary objects
    def getEdges(self, results):
        return False

    def chooseGreaterPercent(self, result):
        if result.file_one_percent > result.file_two_percent:
            return result.file_one_percent
        return result.file_two_percent

    def getJsonObject(self, results):
        graph = {}
        graph['nodes'] = self.getNames(results)
        graph['edges'] = self.getEdges(results)
        return jsonify(graph)

    def printGraph(self):
        return False


def main():
    names = ['Matt', 'Tori', 'Will']

if __name__ == '__main__': main()