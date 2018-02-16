from Result import Result
from Aggregation import Aggregation

class AggregateData:

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
        return False

    # Validates the array can be aggregated
    def validArray(self, array):
        return False

    # Validates the percents array can be aggregated
    def validPercents(self, percents):
        return False

    # Returns an array of names from Results
    def populateNames(self, results):
        return []

    # Returns an array of highest percents based on a given name
    def parsePercents(self, results, name):
        return []

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

    d

def main():
    ag = AggregateData()
    results = ag.example() # Obtained from Sam and Nikolay
    names = ag.populateNames(results)

    aggregatePercents = []
    aggregateLines = []

    for name in names:
        percents = ag.parsePercents(results, name)
        avgPercent = ag.average(percents)
        lines = ag.parseLines(results, name)
        totalLines = ag.total(lines)

        aggPercents = Aggregation(name, avgPercent)
        aggLines = Aggregation(name, totalLines)

        aggregatePercents.append(aggPercents)
        aggregateLines.append(aggLines)

    ag.sort(aggregatePercents)
    ag.sort(aggregateLines)
    ag.display(aggregatePercents, aggregateLines)







if __name__ == '__main__': main()