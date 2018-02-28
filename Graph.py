from networkx import nx
from AggregateData import AggregateData


class Graph:

    def __init__(self, results):
        self.graph = nx.Graph()
        self.createNodes()
        self.createEdges(results)
        self.names = []

    def print(self):
        print('print')

    def validResults(self, results):
        currAssignmentNum = -1
        assignments = {}
        if results and isinstance(results, list):
            for result in results:
                currAssignmentNum = result.assignment_number
                if currAssignmentNum in assignments:
                    assignments[currAssignmentNum] += 1
                else:
                    assignments[currAssignmentNum] = 1
            listKeys = [*assignments]
            if len(assignments) == 1:
                return listKeys[0]
            else:
                currMajority = -1
                assignmentNum = -1
                for key,value in assignments.items():
                    if value > currMajority:
                        currMajority = value
                        assignmentNum = key
                return assignmentNum
        return -1

    def getNames(self, results):
        ag = AggregateData(results)
        self.names = ag.populateNames(results)
        return self.names

    def createNodes(self):
        return False

    def chooseGreaterPercent(self, result):
        return False

    def createEdges(self, results):
        return False



def main():
    names = ['Matt', 'Tori', 'Will']
    #g = nx.DiGraph()
    #g.add_edge(names[1], names[2], weight=80)

if __name__ == '__main__': main()