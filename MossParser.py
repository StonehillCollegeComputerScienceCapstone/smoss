# Class MossParser
# This class is designed to take a url as input and creates a csv file of results from MOSS in the same directory
# as this program
import urllib
import urllib.request
from html.parser import HTMLParser


class MossParser ():
    def __init__(self,csvFileName):
        self.csvFileName = csvFileName

    def parse(self,urlInput):
        # get the html text from the URL
        html = self.getHtml(urlInput)
        # Process the html into table strings
        tableStrings = self.processHtml(html)
        # Process the table strings into csv strings
        csvStrings = self.processTableStrings(tableStrings)
        self.writeToCsv(csvStrings)

    def parseMultiple(self, urlInputs):
        counter = 0
        for url in urlInputs:
            html = self.getHtml(url)
            tableStrings = self.processHtml(html)
            csvStrings = self.processTableStrings(tableStrings)
            if (counter != 0):
                self.appendToCsv(csvStrings)
            else:
                self.writeToCsv(csvStrings)
                counter = 1

    def appendToCsv(self, csvStrings):
        f = open(self.csvFileName, 'a')
        for item in csvStrings:
            for value in item[:-1]:
                f.write(value + ",")
            f.write(item[-1])
            f.write('\n')
        f.close()

    def writeToCsv(self,csvStrings):
        f = open(self.csvFileName, 'w')
        f.write("User1,FileName1,Match1,User2,FileName2,Match2,Lines_Matched,URL")
        f.write('\n')
        for item in csvStrings:
            for value in item[:-1]:
                f.write(value+",")
            f.write(item[-1])
            f.write('\n')
        f.close()

    def getName(self,s):
        s=s.replace("_",",")
        values=s.split(",")
        return values[0]

    def testUrl(self,urlArg):
        request = urllib.request.Request(urlArg)
        try:
            response = urllib.request.urlopen(request)
            # response is now a string you can search through containing the page's html
            return True
        except:
            #The url wasn't valid
            return False

    def processHtml(self,html):
        #parse until table
        htmlParser=myHtmlParser()
        htmlParser.feed(html)
        #here we have all of the rows in one long string
        #now we parse through the string and split them up into individual strings
        stripped=htmlParser.tableString.strip('\n')
        stripped = stripped.replace('\n', '')
        splitStrings=stripped.split("tr")
        #have list of strings split up
        #first two indexes are a blank space and the header, so remove them
        del(splitStrings[0])
        del(splitStrings[0])
        return splitStrings

    def getHtml(self, urlArg):
        html = urllib.request.urlopen(urlArg)
        mybytes = html.read()
        mystr = mybytes.decode("utf8")
        html.close()
        return mystr
    def processTableStrings(self,tableStrings):
        #go through list and turn them into Result object
        csvStrings=[]

        for tableString in tableStrings:
            tableString=self.formatTableString(tableString)
            tableStringValues=tableString.split(",")
            name1=self.getName(tableStringValues[1].strip())
            name2 = self.getName(tableStringValues[4].strip())
            csvString=[name1,tableStringValues[1].strip(),tableStringValues[2],name2,tableStringValues[4].strip(),tableStringValues[5],tableStringValues[6],tableStringValues[0]]
            csvStrings.append(csvString)
        return csvStrings
    def formatTableString(self,tableString):
        tableString.lstrip()
        tableString = tableString.replace("td a href", '')
        tableString = tableString.replace("a  td align right", '')
        tableString = tableString.replace("a       ", '')
        tableString=tableString.replace("  http://",'http://')
        tableString=tableString.replace("  ",",")
        tableString=tableString.replace(" ",", ")
        tableString=tableString.replace(" (","(")
        tableString=tableString.replace("(","")
        tableString=tableString.replace(")","")
        tableString=tableString.replace("%","")
        return tableString
class myHtmlParser (HTMLParser):
    tableString=""
    seenTable=False
    seenEndOfTable=False
    def handle_starttag(self, tag, attrs):
        if(self.seenTable and (not self.seenEndOfTable)):
            self.tableString=self.tableString+tag+" "
            for attr in attrs:
                tupleList=list(attr)
                for item in tupleList:
                    self.tableString=self.tableString+item+" "
        if(tag=="table"):
            self.seenTable=True

    def handle_endtag(self, tag):
        if(self.seenTable and (not self.seenEndOfTable)):
            if(tag=="table"):
                self.seenEndOfTable=True
            else:
               self.tableString=self.tableString+tag+" "
    def handle_data(self, data):
        if(self.seenTable and (not self.seenEndOfTable)):
            self.tableString = self.tableString + data + " "

#use these for testing/running locally
#mp=MossParser("csv.csv")
#mp.parse("http://moss.stanford.edu/results/582293048/")