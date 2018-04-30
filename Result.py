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

    def getNameOne(self):
        return self.getName(self.fileOne)

    def getNameTwo(self):
        return self.getName(self.fileTwo)

    def getName(self, file):
        fileName = file.split('_')
        if fileName[0] == "previous":
            return fileName[1]
        return fileName[0]

    def getAssignmentName(self):
        listOne = self.fileOne.split('_')
        listTwo = self.fileTwo.split('_')
        assignmentOne = listOne[-1]
        assignmentTwo = listTwo[-1]

        if assignmentOne != assignmentTwo:
            return "Error! Different file names!"

        return assignmentOne

    def nameOneIsPrevious(self):
        return self.isNamePrevious(self.fileOne)

    def nameTwoIsPrevious(self):
        return self.isNamePrevious(self.fileTwo)

    def isNamePrevious(self, name):
        prev = name.split('_')
        return prev[0] == "previous"

    def toString(self):
        return str(self.assignmentNumber) + "\t" + str(self.fileOne) + "\t" + str(self.fileTwo) + "\t" + str(self.url) \
               + "\t" + str(self.fileOnePercent) + "\t" + str(self.fileTwoPercent) + "\t" + str(self.linesMatched)

    def equals(self, result):
        return (self.assignmentNumber == result.assignmentNumber) and (self.fileOne == result.fileOne) and \
               (self.fileTwo == result.fileTwo) and (self.url == result.url) and \
               (self.fileOnePercent == result.fileOnePercent) and (self.fileTwoPercent == result.fileTwoPercent) and \
               (self.linesMatched == result.linesMatched)

    def isValid(self):
        return self.validateFiles() and self.validatePercents() and self.validateURL() and self.validateLinesMatched()

    def validateFiles(self):
        return isinstance(self.getFileOne(), str) and isinstance(self.getFileTwo(), str)

    def validatePercents(self):
        var1 = self.getPercentOne()
        var2 = self.getPercentTwo()
        return isinstance(var1, int) and isinstance(var2, int) and var1 > 0 and var2 > 0

    def validateURL(self):
        return isinstance(self.getUrl(), str)

    def validateLinesMatched(self):
        return isinstance(self.linesMatched, int) and self.linesMatched > 0