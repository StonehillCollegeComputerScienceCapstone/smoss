import urllib
import urllib.request
import urllib.error
from Result import Result
from MossParser import MossParser
from Config import Config

class MossResultsRetriever:
    def __init__(self):
        self.config = Config()
        self.urls = []
        self.results = []

    # Populate the results object with the lines from the csv
    def populateResults(self):
        m = MossParser()
        assignmentNum = 0

        for url in self.urls:
            data = m.parse(url)

            for result in data:
                r = Result(assignmentNum, result[0], result[2], result[5].strip(), int(result[1]), int(result[3]), int(result[4]))
                self.results.append(r)

            assignmentNum = assignmentNum + 1

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

    # Returns a set of duplicate urls and a set of urls to be processed
    def getDuplicateUrls(self, urls):
        duplicates = []
        urlList = []
        isValidUrlList, message = self.isValidUrlList(urls)

        if not isValidUrlList:
            return [], []

        for url in urls:
            if url not in urlList:
                urlList.append(url)
            elif url not in duplicates:
                duplicates.append(url)
        return duplicates, urlList

    def validateData(self):
        for result in self.results:
            if not result.isValid():
                return False
        return True

