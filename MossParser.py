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
        print("need to work on class")
        # If this is not a valid URL display error and exit
        # using http://moss.stanford.edu/results/299782671/ to test
        validUrl=self.testUrl(urlInput)
        if(not validUrl):
            self.displayInvalidUrl()
        else:
            # get the html text from the URL
            html = self.getHtml(urlInput)
            #print('Have HTML, now going to process')
            # Process the html into table strings
            tableStrings = self.processHtml(html)

            # Process the table strings into csv strings
            csvStrings = self.processTableStrings(tableStrings)
            self.writeToCsv(csvStrings)

    def writeToCsv(self,csvStrings):
        f = open(self.csvFileName, 'a')
        for item in csvStrings:
            for value in item[:-1]:
                f.write(value+",")
            f.write(item[-1])
            f.write('\n')
        f.close()

    def displayInvalidUrl(self):
        #when there is web functionality, redirect to page displaying error.
        #for now just display error message
        print('Invalid URL was entered')

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
        #print("Table String: ", htmlParser.tableString)
        #here we have all of the rows in one long string
        #now we parse through the string and split them up into individual strings
        #first take out \n
        stripped=htmlParser.tableString.strip('\n')
        stripped = stripped.replace('\n', '')
        splitStrings=stripped.split("tr")
        #have list of strings split up
        #first two indexes are a blank space and the header, so remove them
        del(splitStrings[0])
        del(splitStrings[0])
        return splitStrings



    def processTableString(self):
        return """"<tr><td><a href="http://moss.stanford.edu/results/322457013/match0.html">warmup36.java (94%)</a>
                         </td><td><a href="http://moss.stanford.edu/results/322457013/match0.html">warmup435.java (94%)</a>
                            </td><td align="right">12
                            </td></tr>"""
    def getHtml(self, urlArg):
        html = urllib.request.urlopen(urlArg)
        mybytes = html.read()
        mystr = mybytes.decode("utf8")
        html.close()
        return mystr
    def processTableStrings(self,tableStrings):
        #go through list and turn them into Result object
        #FileName1, Match1, FileName2, Match2, Lines
        #Matched, URL
        csvStrings=[]

        for tableString in tableStrings:
            tableString=self.formatTableString(tableString)
            #print(tableString)
            tableStringValues=tableString.split(",")
            #print(tableStringValues)
            csvString=[tableStringValues[1].strip(),tableStringValues[2],tableStringValues[4].strip(),tableStringValues[5],tableStringValues[6],tableStringValues[0]]
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
#mp.parse("http://moss.stanford.edu/results/299782671/")