import json

class AggregateData:

    def display(self):
        print ("Method example")

    def isValid(self, object):
        return False

    def calculateAveragePercent(self, object):
        return -1

    def calculateTotalLines(self, object):
        return -1

    def generateJSON(self, object):
        return {}

def main():
    print('Main method')
    object = {}
    json_object = json.dumps(object)

    print(type(json_object))

if __name__ == '__main__': main()