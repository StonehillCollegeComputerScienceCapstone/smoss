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
        if not(self.isValidLength() and self.isValidStringList(self.fileName1) and self.isValidStringList(self.fileName2)
               and self.isValidStringList(self.URL) and self.isValidMatchedList(self.match1) and
               self.isValidMatchedList(self.match2) and self.isValidMatchedList(self.linesMatched)
               and self.isValidFilename()):
            return False
        return True
rs=ResultsSorter()