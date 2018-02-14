import json

class AggregateData:

    def isValid(self, object):
        return False

    def calculateAveragePercent(self, object):
        sum = 0
        average = -1
        count = 0
        for x in object:
            sum = sum + x.percent
            count = count + 1

        average = sum / count

        return average

    def calculateTotalLines(self, object):
        sum = 0
        for x in object:
            sum = sum + x.lines

        return sum

    def generateJSON(self, object):
        return {}

def main():
    object = {}
    json_object = json.dumps(object)

    print(type(json_object))

if __name__ == '__main__': main()