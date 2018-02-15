class AggregateData:

    def validResults(self, results):
        return False

    def validArray(self, array):
        return False

    def validPercents(self, percents):
        return False

    def averagePercent(self, percents):
        sum = 0
        average = -1
        count = 0
        for percent in percents:
            sum = sum + percent
            count = count + 1

        average = sum / count

        return average

    def totalLines(self, lines):
        sum = 0
        for line in lines:
            sum = sum + line

        return sum

def main():
    array = [3, 2]
    if array:
        print("Array exists")

if __name__ == '__main__': main()