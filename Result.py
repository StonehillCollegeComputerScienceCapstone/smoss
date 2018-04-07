class Result:
    def __init__(self, assignmentNum, f1, f2, url, f1Percent, f2Percent, linesMatched):
        self.assignmentNumber = assignmentNum
        self.fileOne = f1
        self.fileTwo = f2
        self.url = url
        self.fileOnePercent = f1Percent
        self.fileTwoPercent = f2Percent
        self.linesMatched = linesMatched

    def getAssignmentNumber(self):
        return self.assignmentNumber

    def getFileOne(self):
        return self.fileOne

    def getFileTwo(self):
        return self.fileTwo

    def getUrl(self):
        return self.url

    def getPercentOne(self):
        return self.fileOnePercent

    def getPercentTwo(self):
        return self.fileTwoPercent

    def getLinesMatched(self):
        return self.linesMatched

    def toString(self):
        return str(self.assignmentNumber) + "\t" + str(self.fileOne) + "\t" + str(self.fileTwo) + "\t" + str(self.url) \
               + "\t" + str(self.fileOnePercent) + "\t" + str(self.fileTwoPercent) + "\t" + str(self.linesMatched)

    def equals(self, result):
        return (self.assignmentNumber == result.assignmentNumber) and (self.fileOne == result.fileOne) and \
               (self.fileTwo == result.fileTwo) and (self.url == result.url) and \
               (self.fileOnePercent == result.fileOnePercent) and (self.fileTwoPercent == result.fileTwoPercent) and \
               (self.linesMatched == result.linesMatched)
