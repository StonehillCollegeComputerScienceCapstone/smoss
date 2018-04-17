import sys
from operator import attrgetter
from Result import Result
from Aggregation import Aggregation
from Config import Config
class DataAggregator:

    # Constructor for DataAggregator
    def __init__(self, results=None):
        self.results = results
        self.topPercents = []
        self.topLines = []
        self.config = Config()
        if results is not None:  # This adjustment made for using the example outside of this class
            self.aggregateData()

    # Validates data has been received to aggregate
    def validateResults(self, results):
        if results and isinstance(results, list):
            return True
        return False

    # Validates the array can be aggregated
    def validateArray(self, array):
        # Must be an array
        if (not array) or (not isinstance(array, list)):
            return False

        # Must only contain positive integers
        for value in array:
            if (not isinstance(value, int) or value <0):
                return False
        return True

    # Validates the percents array can be aggregated
    def validatePercents(self, percents):
        # Must contain ints <= 100
        for value in percents:
            if (value > 100):
                return False
        return True

    # Returns an array of names from Results
    def populateNames(self, results):
        names = []

        # For every row from MOSS

        for result in results:
            if result.fileOne not in names:
                names.append(result.fileOne)
            if result.fileTwo not in names:
                names.append(result.fileTwo)

        return names

    # Returns an array of assignment numbers in results
    def getAssignmentNumbers(self, results):
        numbers = []

        for result in results:
            if (result.assignmentNumber not in numbers):
                numbers.append(result.assignmentNumber)
        return numbers

    #
    # Returns an array of data based off of chosen data type
    #
    def parseData(self, results, name, dataType):
        parsedData = []
        assignmentNumbers = self.getAssignmentNumbers(results)
        for number in assignmentNumbers:
            data = []
            for result in results:
                if (result.assignmentNumber == number and dataType is "lines" and ((result.fileOne == name) or (result.fileTwo == name))):
                    data.append(int(result.linesMatched))
                elif (result.assignmentNumber == number and dataType is "percents" and result.fileOne == name):
                    data.append(int(result.fileOnePercent))
                elif (result.assignmentNumber == number and dataType is "percents" and result.fileTwo == name):
                    data.append(int(result.fileTwoPercent))
            if (data != []):
                parsedData.append(max(data))
        return parsedData

    # Calculates the average of a given array
    def average(self, array):
        return round(sum(array) / len(array))

    # Calculates the total sum of a given array
    def sum(self, array):
        return sum(array)

    # Sorts the Aggregation objects based on the data field
    def sort(self, array):
        return sorted(array, key=attrgetter('data'), reverse=True)

    # Aggregates the data and populates the two fields
    def aggregateData(self):
        if (not self.validateResults(self.results)):
            return False
        names = self.populateNames(self.results)

        aggregatePercents = []
        aggregateLines = []

        for name in names:
            # Parse the highest percents for a given name
            percents = self.parseData(self.results, name,"percents")
            if ((not self.validateArray(percents)) or (not self.validatePercents(percents))):
                return False
            # Parse the highest lines matched for a given name
            lines = self.parseData(self.results, name, "lines")

            # Append Aggregation object array
            aggregatePercents.append(Aggregation(name, self.average(percents)))
            aggregateLines.append(Aggregation(name, self.sum(lines)))

        # Sort data
        aggregatePercents = self.sort(aggregatePercents)
        aggregateLines = self.sort(aggregateLines)

        # We only want the top ten results
        self.topPercents = aggregatePercents[:10]
        self.topLines = aggregateLines[:10]

        return True
