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
        return self.assignmentNumber()

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
