import sys
from operator import attrgetter
from Result import Result
from Aggregation import Aggregation

class AggregateData:

    # Constructor for AggregateData
    def __init__(self, results):
        self.results = results
        self.top_percents = []
        self.top_lines = []
        if (not (results is None)):  # This adjustment made for using the example outside of this class
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
            if (result.file_one != "User1"):
                if result.file_one not in names:
                    names.append(result.file_one)
                if result.file_two not in names:
                    names.append(result.file_two)

        return names

    # Returns an array of assignment numbers in results
    def getAssignmentNumbers(self, results):
        numbers = []

        for result in results:
            if (result.file_one != "User1"):
                if (result.assignment_number not in numbers):
                    numbers.append(result.assignment_number)
        return numbers

    # Returns an array of highest percents based on a given name
    def parsePercents(self, results, name):
        maxPercents = []
        assignmentNumbers = self.getAssignmentNumbers(results)

        for number in assignmentNumbers:
            percents = []

            for result in results:
                if (result.file_one != "User1"):
                    if (result.assignment_number == number) and (result.file_one == name):
                        percents.append(int(result.file_one_percent))
                    elif (result.assignment_number == number) and (result.file_two == name):
                        percents.append(int(result.file_two_percent))
            if (percents != []):
                maxPercents.append(max(percents))
        return maxPercents

    # Returns an array of lines matched based on a given name
    def parseLines(self, results, name):
        maxLines = []
        assignmentNumbers = self.getAssignmentNumbers(results)

        for number in assignmentNumbers:
            lines = []

            for result in results:
                if (result.file_one != "User1"):
                    if (result.assignment_number == number) and (result.file_one == name):
                        lines.append(int(result.lines_matched))
                    elif (result.assignment_number == number) and (result.file_two == name):
                        lines.append(int(result.lines_matched))
            if (lines != []):
                maxLines.append(max(lines))
        return maxLines

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
            print(object.to_string())

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
            percents = self.parsePercents(self.results, name)
            if ((not self.validateArray(percents)) or (not self.validatePercents(percents))):
                print("Percents array not valid!")
                sys.exit()

            # Parse the highest lines matched for a given name
            lines = self.parseLines(self.results, name)
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
        validURL = "http://moss.stanford.edu/results/11690537/" # Change this when URL expires
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

#    results = example()  # Obtained from Sam and Nikolay
#   ag = AggregateData(results)

    ag = AggregateData(None)  #adjusted to get this main's example to work with example() being part of the class
    ag.results = ag.example()
    ag.aggregateData()

    # Display data
    #print("Highest Average Percent")
    #ag.display(ag.top_percents)
    #print()
    #print("Highest Lines Matched")
    #ag.display(ag.top_lines)



if __name__ == '__main__': main()