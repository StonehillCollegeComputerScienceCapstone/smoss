import sys
from Result import Result
from Aggregation import Aggregation

class AggregateData:

    # Example data
    def example(self):
        results = []
        result1 = Result(1, "Matt", "Armen", "http://moss.stanford.edu/results/299782671/", 90, 70, 20)
        result2 = Result(1, "Matt", "Sam", "http://moss.stanford.edu/results/299782671/", 80, 43, 77)
        result3 = Result(1, "Armen", "Sam", "http://moss.stanford.edu/results/299782670/", 12, 10, 8)
        result4 = Result(2, "Matt", "Armen", "http://moss.stanford.edu/results/299782671/", 33, 70, 45)
        result5 = Result(2, "Matt", "Sam", "http://moss.stanford.edu/results/299782671/", 16, 17, 15)
        result6 = Result(2, "Armen", "Sam", "http://moss.stanford.edu/results/299782670/", 50, 34, 5)
        result7 = Result(3, "Matt", "Armen", "http://moss.stanford.edu/results/299782671/", 76, 79, 20)
        result8 = Result(3, "Matt", "Sam", "http://moss.stanford.edu/results/299782671/", 90, 88, 100)
        result9 = Result(3, "Armen", "Sam", "http://moss.stanford.edu/results/299782670/", 10, 6, 2)
        results.append(result1)
        results.append(result2)
        results.append(result3)
        results.append(result4)
        results.append(result5)
        results.append(result6)
        results.append(result7)
        results.append(result8)
        results.append(result9)
        return results

    # Validates data has been received to aggregate
    def validResults(self, results):
        if results and isinstance(results, list):
            return True
        return False

    # Validates the array can be aggregated
    def validArray(self, array):
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
    def validPercents(self, percents):
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
            if result.file_one not in names:
                names.append(result.file_one)
            if result.file_two not in names:
                names.append(result.file_two)

        return names

    def getAssignmentNumbers(self, results):
        numbers = []
        for result in results:
            if (result.assignment_number not in numbers):
                numbers.append(result.assignment_number)
        return numbers


    # Returns an array of highest percents based on a given name
    def parsePercents(self, results, name):
        percents = []
        num = 1
        assignmentNumbers = self.getAssignmentNumbers()

        for result in results:
            if result.assignment_number == num:
                percents

        return percents

    # Returns an array of lines matched based on a given name
    def parseLines(self, results, name):
        return []

    # Calculates the average of a given array
    def average(self, array):
        sum = 0
        count = 0
        for value in array:
            sum = sum + value
            count = count + 1
        average = sum / count
        return round(average)

    # Calculates the total sum of a given array
    def total(self, array):
        sum = 0
        for value in array:
            sum = sum + value
        return sum

    # Sorts the passed in array
    def sort(self, array):
        return

    # Displays the passed in array
    def display(self, array):
        for object in array:
            print(object.to_string())

def main():
    ag = AggregateData()

    # Get results and ensure they are valid
    results = ag.example() # Obtained from Sam and Nikolay
    if (not ag.validResults):
        print("Results not valid!")
        sys.exit()

    names = ag.populateNames(results)

    aggregatePercents = []
    aggregateLines = []

    for name in names:
        # Parse the highest percents for a given name
        percents = ag.parsePercents(results, name)
        if ((not ag.validArray(percents)) or (not ag.validPercents(percents))):
            print("Percents array not valid!")
            sys.exit()

        # Parse the highest lines matched for a given name
        lines = ag.parseLines(results, name)
        if (not ag.validArray(percents)):
            print("Lines array not valid!")
            sys.exit()

        # Calculate average percent and total lines
        avgPercent = ag.average(percents)
        totalLines = ag.total(lines)

        # Create an Aggregation object with the data
        aggPercents = Aggregation(name, avgPercent)
        aggLines = Aggregation(name, totalLines)

        # Append Aggregation object array
        aggregatePercents.append(aggPercents)
        aggregateLines.append(aggLines)

    # Sort data
    ag.sort(aggregatePercents)
    ag.sort(aggregateLines)

    # Display data
    print("Highest Average Percent")
    ag.display(aggregatePercents)
    print("Highest Lines Matched")
    ag.display(aggregateLines)


if __name__ == '__main__': main()