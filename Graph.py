from networkx import nx
from AggregateData import AggregateData


class Graph:

    def __init__(self, results):
        self.graph = nx.Graph()
        self.createNodes()
        self.createEdges(results)

    def print(self):
        print('print')

    def validResults(self, results):
        if results and isinstance(results, list):
            #
            #Make sure all results have the same assignment number
            #
            return True
        return False

    def getNames(self, results):
        return False

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