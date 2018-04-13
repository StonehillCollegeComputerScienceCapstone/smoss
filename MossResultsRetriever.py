import urllib
import urllib.request
import urllib.error
from Result import Result
from MossParser import MossParser
from Config import Config
import os
import csv

class MossResultsRetriever:
    def __init__(self):
        self.config = Config()
        self.urls = []
        self.results = []

    # If url is valid, return true. Else, return false
    def isValidUrl(self, url):
        # If the url is not a string, does not contain moss url, ot contains new line or space, return false
        if (not isinstance(url, str)) or ("moss.stanford.edu/results/" not in url) or ('\n' in url) or (' ' in url):
            return False

        # Catch 404 Not Found or connection not accepted
        try:
            urllib.request.urlopen(url)
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            return False

        return True

    # Returns true if every URL in the list is valid, else returns false
    def isValidUrlList(self, urls):
        if not isinstance(urls, list) or (len(urls) == 0):
            return False, "argument " + str(urls) + " is not a valid list"
        for url in urls:
            if not self.isValidUrl(url):  # If the url is invalid
                return False, url  # Return the url that is invalid
        success = "success"
        return True, success

    # If url is valid, append to list of urls
    def appendUrl(self, url):
        if (url not in self.urls) and (self.isValidUrl(url)):
            self.urls.append(url)

    # Populate the results object with the lines from the csv
    def populateResults(self):
        csv = "csv.csv"
        m = MossParser(csv)
        assignmentNum = 0

        for url in self.urls:
            m.parse(url)
            file = open(csv)
            lines = file.readlines()
            lines.pop(0) # Remove header from csv

            for line in lines:
                data = line.split(',')
                r = Result(assignmentNum, data[0], data[3], data[7].strip(), int(data[2]), int(data[5]), int(data[6]))
                self.results.append(r)

            file.close()
            assignmentNum = assignmentNum + 1

        if len(self.urls) > 1:
            m.parseMultiple(self.urls)

    # Returns a set of duplicate urls and a set of urls to be processed
    def getDuplicateUrls(self, urls):
        duplicates = []
        nonDuplicates = []
        isValidUrlList, message = self.isValidUrlList(urls)

        if not isValidUrlList:
            return [], []

        for url in urls:
            if url not in nonDuplicates:
                nonDuplicates.append(url)
            else:
                duplicates.append(url)
                nonDuplicates.remove(url)
        return duplicates, nonDuplicates

    def validateData(self):
        for result in self.results:
            if not result.isValid():
                return False
        return True

def main():
    retriever = MossResultsRetriever()
    retriever.populateResults()

if __name__ == '__main__': main()