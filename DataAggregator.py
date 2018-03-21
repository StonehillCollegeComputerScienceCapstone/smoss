import sys
from operator import attrgetter
from Result import Result
from Aggregation import Aggregation
from Config import Config
class DataAggregator:

    # Constructor for DataAggregator
    def __init__(self, results=None):
        self.results = results
        self.top_percents = []
        self.top_lines = []
        self.config = Config()
        if (not (results is None)):  # This adjustment made for using the example outside of this class
            results.pop(0)  # this removes the header line from array of csv data
            self.aggregateData()

    def reInit(self, results):
        self.results = results
        self.top_percents = []
        self.top_lines = []
        if (not (results is None)):
            self.aggregateData()

    def setResults(self, results):
        self.results = results
        if (not (results is None)):
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
            if (not isinstance(value, int)):
                return False
            if (value < 0):
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
                if (result.assignmentNumber == number):
                    if (dataType is "lines"):
                        if ((result.fileOne == name) or (result.fileTwo == name)):
                            data.append(int(result.linesMatched))
                    elif (dataType is "percents"):
                        if (result.fileOne == name):
                            data.append(int(result.fileOnePercent))
                        elif (result.fileTwo == name):
                            data.append(int(result.fileTwoPercent))
            if (data != []):
                parsedData.append(max(data))
        return parsedData

    # Calculates the average of a given array
    def calculateAverage(self, array):
        sum = 0
        count = 0
        for value in array:
            sum = sum + value
            count = count + 1
        average = sum / count
        return round(average)

    # Calculates the total sum of a given array
    def calculateSum(self, array):
        return sum(array)

    # Displays the passed in array
    def displayArray(self, array):
        for object in array:
            print(object.toString())

    # Sorts the Aggregation objects based on the data field
    def sort(self, array):
        return sorted(array, key=attrgetter('data'), reverse=True)

    # Aggregates the data and populates the two fields
    def aggregateData(self):
        if (not self.validateResults):
            print("Results not valid!")
            sys.exit()

        names = self.populateNames(self.results)

        aggregatePercents = []
        aggregateLines = []

        for name in names:
            # Parse the highest percents for a given name
            percents = self.parseData(self.results, name,"percents")
            if ((not self.validateArray(percents)) or (not self.validatePercents(percents))):
                print("Percents array not valid!")
                sys.exit()

            # Parse the highest lines matched for a given name
            lines = self.parseData(self.results, name, "lines")
            if (not self.validateArray(percents)):
                print("Lines array not valid!")
                sys.exit()

            # Calculate average percent and total lines
            avgPercent = self.calculateAverage(percents)
            totalLines = self.calculateSum(lines)

            # Create an Aggregation object with the data
            aggPercents = Aggregation(name, avgPercent)
            aggLines = Aggregation(name, totalLines)

            # Append Aggregation object array
            aggregatePercents.append(aggPercents)
            aggregateLines.append(aggLines)

        # Sort data
        aggregatePercents = self.sort(aggregatePercents)
        aggregateLines = self.sort(aggregateLines)

        # We only want the top ten results
        self.top_percents = aggregatePercents[:10]
        self.top_lines = aggregateLines[:10]

    # Example data
    def example(self):  # Put this in the class to have the example
        validURL = Config.getGolbach() # URL for 'Golbach' assignment
        results = []
        results.append(Result(1, "Matt", "Armen", validURL, 90, 70, 20))
        results.append(Result(1, "Matt", "Sam", validURL, 80, 43, 77))
        results.append(Result(1, "Armen", "Sam", validURL, 12, 10, 8))
        results.append(Result(2, "Matt", "Armen", validURL, 33, 70, 45))
        results.append(Result(2, "Matt", "Sam", validURL, 16, 17, 15))
        results.append(Result(2, "Armen", "Sam", validURL, 50, 34, 5))
        results.append(Result(3, "Matt", "Armen", validURL, 76, 79, 20))
        results.append(Result(3, "Matt", "Sam", validURL, 90, 88, 100))
        results.append(Result(3, "Armen", "Sam", validURL, 10, 6, 2))

        return results

def main():

    ag = DataAggregator()  #adjusted to get this main's example to work with example() being part of the class
    ag.results = ag.example()
    ag.aggregateData()



if __name__ == '__main__': main()