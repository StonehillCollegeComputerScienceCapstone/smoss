import urllib
import urllib.request
import urllib.error
from FileRetrieval import FileRetrieval
from Result import Result
from MossParser import MossParser
from Config import Config

class MossResultsRetriever:
    def __init__(self):
        self.urls = []
        self.file = FileRetrieval()
        self.results = []
        self.config = Config()

    # If url is valid, append to list of urls. Else, returns false
    def getUrl(self, url):
        if (not isinstance(url, str)) or ("moss.stanford.edu/results" not in url):
            return False

        # Catch 404 Not Found or connection not accepted
        try:
            urllib.request.urlopen(url)
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            return False

        if url not in self.urls:
            self.urls.append(url)

        return True

    # Retrieves the URLs from a specified file
    def getFileUrls(self, file):
        if not self.file.readFile(file):  # FileRetrieval returns if the file is valid
            return False
        for url in self.file.urlList:
            self.getUrl(url)# checks the validity of the URLs given from file
        return True

    # Returns true if every URL in the list is valid, else returns false
    def getValidity(self, urlList):
        for item in urlList:
            if not(self.getUrl(item)):# checks the validity of the URLs given from file
                return False, item #returns the url that is invalid
        success = "success"
        return True, success

    # Populate the results object with the lines from the csv
    def getResults(self):
        csv = "csv.csv"
        m = MossParser(csv)
        assignmentNum = 0
        validFileName = True

        for url in self.urls:
            validFileName = m.parse(url)
            file = open(csv)
            lines = file.readlines()
            lines.pop(0) # Remove header from csv

            for line in lines:
                data = line.split(',')
                r = Result(assignmentNum, data[0], data[3], data[7].strip(), data[2], data[5], data[6])
                self.results.append(r)

            file.close()
            assignmentNum = assignmentNum + 1

        if (len(self.urls) > 1):
            m.parseMultiple(self.urls)  #added this to get a csv file for all the assignments so the sortResults method can add all assignments to one table in html /moss
                                        #will need to be adjusted because of time consumption
        return validFileName

    # Checks the results object for any duplicate data
    def areDuplicateResults(self):
        seen = []
        for result in self.results:
            for seenResult in seen:
                if result.equals(seenResult):
                    return True
            seen.append(result)
        return False

def main():
    murl = MossResultsRetriever()
    murl.getResults()

if __name__ == '__main__': main()