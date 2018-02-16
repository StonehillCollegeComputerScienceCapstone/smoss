class AggregateData:

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
    def populateNames(self):
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

    def getAggregatePercents(self):
        return []

    def getAggregateLines(self):
        return []

def main():
    print('Hello world')

if __name__ == '__main__': main()