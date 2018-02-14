from Result import Result

class MossURLsRetrieval:
    def __init__(self):
        self.urls = []
        self.Results = []
        #potentially a data variable?

    def getURL(self, url):
        #check to see if it has "moss.stanford.edu"
        #check that it exists (http response of 200?)
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