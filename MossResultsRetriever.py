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
        # potentially a data variable?

    def reInit(self):
        self.urls = []
        self.file = FileRetrieval()
        self.results = []

    def getUrl(self, url):
        # check to see if it has "moss.stanford.edu"
        # check that it exists (http response of 200?)

        if not isinstance(url, str):
            #print(url, "is invalid")
            return False
        if "moss.stanford.edu/results" not in url:  # this can be changed by Stanford at any time
            #print(url, "is invalid")
            return False
        #if url in self.urls:  # URL already exists in list
         #   print(url, "is duplicate")
          #  return False
        try:
            urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:  # case of 404 Not Found
            #print(url, e)
            return False
        except urllib.error.URLError as e:  # case connection refused
            #print(url, ": ", e)
            return False
        if url not in self.urls:
            self.urls.append(url)
        return True

    def get_file_urls(self, file):
        if not self.file.open_and_read_file(file):  # FileRetrieval returns if the file is valid
            return False
        for url in self.file.url_list:
            self.getUrl(url)# checks the validity of the URLs given from file
        return True

    def getValidity(self, urlList):
        for item in urlList:
            if not(self.getUrl(item)):# checks the validity of the URLs given from file
                return False, item #returns the url that is invalid
        success = "success"
        return True, success

    def get_results(self):
        file_data_name = "csv.csv"
        m = MossParser(file_data_name)
        assignment_num = 0
        validFileName = True
        for url in self.urls:
            validFileName = m.parse(url)
            file_data = open(file_data_name)
            lines = file_data.readlines()
            for line in lines:
                data = line.split(',')
                r = Result(assignment_num, data[0], data[3], data[7].strip(), data[2], data[5], data[6])
                self.results.append(r)

            file_data.close()
            assignment_num = assignment_num + 1
        if (len(self.urls) > 1):
            m.parseMultiple(self.urls)  #added this to get a csv file for all the assignments so the sortResults method can add all assignments to one table in html /moss
                                        #will need to be adjusted because of time consumption
        return validFileName

def main():
    murl = MossResultsRetriever()
    #murl.get_file_urls("FileInput.txt")
    murl.get_results()
    #for r in murl.results:
        #print("------------------- assignment number: ")
        #print(r.assignmentNumber)
        #print(r.fileOne )
        #print(r.fileTwo )
        #print(r.url )
        #print(r.fileOnePercent)
        #print(r.fileTwoPercent )
        #print(r.linesMatched)

if __name__ == '__main__': main()