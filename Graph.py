from AggregateData import AggregateData

class Graph:

    def __init__(self):
        self.x = 2

    def print(self):
        print('print')

    def cmp(self, a, b):
        return (a > b) - (a < b)

    def getNames(self):
        return False

    def pairNames(self, names):
        return False


def main():
    names = ['Matt', 'Tori', 'Will']
    #g = nx.DiGraph()
    #g.add_edge(names[1], names[2], weight=80)

if __name__ == '__main__': main()