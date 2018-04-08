import csv
import webbrowser
import os
import json


class ResultsSorter:

    def __init__(self):
        # CSV input file name
        self.inputFileName = "csv.csv"
        # Lists that hold the csv information
        self.user1 = []
        self.user2 = []
        self.fileName1 = []
        self.fileName2 = []
        self.match1 = []
        self.match2 = []
        self.linesMatched = []
        self.URL = []
        # Main list that holds dictionaries in the format
        # ("CSV column title", value)
        self.MOSSresults = []

    # Checks to make sure there is a csv file
    def isValidFilename(self):
        if len(self.inputFileName) <= 5:
            return False
        self.inputFileName = self.inputFileName.lower()
        if self.inputFileName.endswith('.csv'):
            return True
        return False

    # Creates a list from the csv file
    def createMainList(self):
        with open(self.inputFileName) as f:
            inputFile = csv.DictReader(f)
            for row in inputFile:
                self.MOSSresults.append(row)
        f.close()

        if len(self.MOSSresults) > 0:
            return True
        else:
            return False

    # Parses the main list into individual category lists
    def createCategoryLists(self):
        for dict in self.MOSSresults:
            self.user1.append(dict['User1'].rstrip())
            self.user2.append(dict['User2'].rstrip())
            self.fileName1.append(dict['FileName1'].rstrip())
            self.fileName2.append(dict['FileName2'].rstrip())
            self.match1.append(dict['Match1'].rstrip())
            self.match2.append(dict['Match2'].rstrip())
            self.linesMatched.append(dict['Lines_Matched'].rstrip())
            self.URL.append(dict['URL'].rstrip())

    def isValidStringList(self, listName):
        for key in listName:
            if key.isdigit():
                return False
        return True

    def isValidMatchedList(self, listName):
        for key in listName:
            if not key.isdigit() or int(key) <= 0:
                return False
        return True

    def isValidLength(self):
        if len(self.user1) == len(self.user2) == len(self.fileName1) == len(self.fileName2) == len(self.match1) == len(self.match2) == len(self.URL) == len(self.linesMatched):
            return True
        else:
            return False

    def getFilePath(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "csv.csv")
        return filename
        # webbrowser.open("file://" + filename, new=0)

    def get_csv(self):
        csv_path = self.getFilePath()
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        csv_file.close()
        return csv_list

    def validateData(self):
        if not(self.isValidLength() or self.isValidStringList(self.fileName1) or self.isValidStringList(self.fileName2) or
               self.isValidStringList(self.URL)or self.isValidMatchedList(self.match1) or self.isValidMatchedList(self.match2) or
               self.isValidMatchedList(self.linesMatched) or self.isValidFilename()):
            return False
        return True
