from Result import Result
import urllib
import urllib.request, urllib.error

class MossURLsRetrieval:
    def __init__(self):
        self.urls = []
        self.Results = []
        #potentially a data variable?

    def getURL(self, url):
        #check to see if it has "moss.stanford.edu"
        #check that it exists (http response of 200?)
        if (not isinstance(url, str)):
            return False
        if ("moss.stanford.edu/results" not in url): #this can be changed by Stanford at any time
            return False
        if (url in self.urls): #URL already exists in list
            return False
        try:
            connection = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e: #case of 404 Not Found
            print(e)
            return False
        except urllib.error.URLError as e: #case connection refused
            print(e)
            return False
        self.urls.append(url)
        return True

    def gatherData(self):
        for url in self.urls:
            self.parseHTML(url)

    def parseHTML(self, url):
        #take url, send request for html
        #take html, parse that it is correctly formated
        #maybe break up the data?
        #otherwise, append to html string
        return True