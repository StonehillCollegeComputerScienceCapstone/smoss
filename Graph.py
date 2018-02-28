from AggregateData import AggregateData

class Graph:

    def __init__(self, results):
        self.createNodes()
        self.createEdges(results)
        self.names = []

    def print(self):
        print('print')

    def validResults(self, results):
        if results and isinstance(results, list):
            assignmentNumber = results[0].assignment_number
            for result in results:
                if not (result.assignment_number == assignmentNumber):
                    return False
        else:
            return False
        return True

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

if __name__ == '__main__': main()