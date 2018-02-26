from networkx import nx
from AggregateData import AggregateData

class Graph:

    def print(self):
        print('print')

    def getNames(self):
        return False


def main():
    names = ['Matt', 'Tori', 'Will']
    g = nx.DiGraph()
    g.add_edge(names[1], names[2], weight=80)

if __name__ == '__main__': main()