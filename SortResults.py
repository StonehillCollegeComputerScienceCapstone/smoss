import csv
import webbrowser
import os
import json
from flask import Flask, render_template

app = Flask(__name__)


class SortResults:

    def __init__(self):
        # CSV input file name
        self.inputFileName = "MOSSinput.csv"
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

        print(self.MOSSresults)

        if len(self.MOSSresults) > 0:
            return True
        else:
            return False

    # Parses the main list into individual category lists
    def createCategoryLists(self):
        for dict in self.MOSSresults:
            for key, value in dict.items():
                if key == "User1":
                    self.user1.append(value.rstrip())
                if key == "User2":
                    self.user2.append(value.rstrip())
                if key == "FileName1":
                    self.fileName1.append(value.rstrip())
                if key == "FileName2":
                    self.fileName2.append(value.rstrip())
                if key == "Match1":
                    self.match1.append(value.rstrip())
                if key == "Match2":
                    self.match2.append(value.rstrip())
                if key == "Lines Matched":
                    self.linesMatched.append(value.rstrip())
                if key == "URL":
                    self.URL.append(value)

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
        if len(self.user1) == len(self.user2) == len(self.match1) == len(self.match2) == len(self.URL) == len(self.linesMatched):
            return True
        else:
            return False

    def renderWebpage(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "MOSSoutput.html")
        webbrowser.open("file://" + filename, new=0)

    def getUser1(self):
        return self.user1[:]

    @app.route('/')
    def userList():
        test = ['Hello', 'World']
        test = json.dumps(test)
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "/templates/MOSSoutput.html")
        filename = "/MOSSoutput.html"
        return render_template(filename, test=test)

if __name__ == '__main__':
    sr = SortResults()
    sr.createMainList()
    sr.createCategoryLists()
    app.run(debug = True)
