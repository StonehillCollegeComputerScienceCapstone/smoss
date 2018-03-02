import json
from flask import *
from Result import Result
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
    def getNodes(self, results):
        names = []
        ag = AggregateData(results)
        nameList = ag.populateNames(results)

        for n in nameList:
            names.append({'name': n})
        return names

    # Return an array of dictionary objects
    def getEdges(self, results):
        edges = []
        for result in results:
            edges.append({'name1': result.file_one, 'name2': result.file_two, 'weight': self.chooseGreaterPercent(result)})
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
    validURL = "http://moss.stanford.edu/results/11690537/"  # Change this when URL expires
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
    graph.print()

if __name__ == '__main__': main()