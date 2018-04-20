# Class MossParser
# This class is designed to take a url as input and creates a csv file of results from MOSS in the same directory
# as this program
import urllib
import urllib.request
import lxml.html
from html.parser import HTMLParser
from Config import Config


class MossParser ():
    def __init__(self, csvFileName):
        self.csvFileName = csvFileName
        self.config = Config()

    # Parse a single URL
    def parse(self, url):
        # Get the html text from the URL
        html = self.getHtml(url)

        if html is None:
            return False

        # Process the html into table strings
        tableStrings = self.processHtml(html)

        # Process the table strings into csv strings
        csvStrings, validFileName = self.processTableStrings(tableStrings)

        if(validFileName):
            return self.toCsv(csvStrings, 'w')

    def toCsv(self, csvStrings, type):
        if(type == 'w'):
            f = open(self.csvFileName, 'w')
            f.write("User1,FileName1,Match1,User2,FileName2,Match2,Lines_Matched,URL" + '\n')
        elif (type == 'a'):
            f = open(self.csvFileName, 'a')
        else:
            return False
        if (isinstance(csvStrings, list)):
            for item in csvStrings:
                for value in item[:-1]:
                    f.write(value+",")
                f.write(item[-1])
                f.write('\n')
            f.close()
            return True
        f.close()
        return False

    # Gets the name of the student for a given file name
    def getName(self, fileName):
        values=fileName.split("_")
        if values[0] == "previous":
            return values[1]
        else:
            return values[0]

    # Returns True if the URL is valid, else returns False
    def testUrl(self, url):
        if (not (isinstance(url, str)) or (("moss.stanford.edu/results" not in url) and ("171.64.78.49" not in url))):
            return False
        try:
            text=lxml.html.parse(url)
            html=text.find(".//title").text
            if(html != "Moss Results"):
                return False
            else:
                return True
        # Create an exception and return False if the URL is not valid
        except:
            return False

    def processHtml(self, html):
        # Parse until table
        htmlParser=myHtmlParser()
        htmlParser.feed(html)

        # Here we have all of the rows in one long string
        # now we parse through the string and split them up into individual strings
        stripped=htmlParser.tableString.strip('\n')
        stripped = stripped.replace('\n', '')
        splitStrings=stripped.split("<tr>")

        # Have list of strings split up
        # first two indexes are a blank space and the header, so remove them
        del(splitStrings[0])
        del(splitStrings[0])
        return splitStrings

    def getHtml(self, url):
        if(self.testUrl(url) is True):
            html = urllib.request.urlopen(url)
            mybytes = html.read()
            mystr = mybytes.decode("utf8")
            html.close()
            return mystr
        else:
            return None

    def getTableStringValues(self, tableString):
        if not isinstance(tableString, str):
            return False
        tableString=self.formatTableString(tableString)

        # if we didn't get a csv format string, that's an error
        if(not ("," in tableString)):
            return False

        tableStringValues = tableString.split(",")
        return tableStringValues


    def processTableStrings(self, tableStrings):
        # Go through list and turn them into Result object
        csvStrings = []
        csvPreviousStrings = []
        previousSet = set()
        for tableString in tableStrings:
            tableStringValues=self.getTableStringValues(tableString)
            fileName1=tableStringValues[1].strip()
            fileName2=tableStringValues[4].strip()

            if self.testFileNaming(fileName1) and self.testFileNaming(fileName2):
                csvString=[self.getName(fileName1), fileName1, tableStringValues[2], self.getName(fileName2), fileName2, tableStringValues[5],tableStringValues[6], tableStringValues[0]];
                if self.previousYearMatch(fileName1,fileName2):
                    previousSet.add(fileName1)
                    csvPreviousStrings.append(csvString)
                else:
                    csvStrings.append(csvString)

        # Returns
        if len(csvStrings)>0:
            return csvStrings, True
        elif len(csvPreviousStrings)>0:
            return csvPreviousStrings, True
        else:
            return None, True


    def testFileNaming(self, fileName):
        if fileName[0].isdigit():
            return False

        # we need an underscore to seperate username and the assignment name,
        #  _ is suppose to seperate, not precede the name
        if "_" in fileName and ("_" is not fileName[0]):
            return True

        return False

    def previousYearMatch(self, filename1, filename2):
        #  make sure that potential difference in casing does not cause a problem with the 'previous' tag
        filename1.lower()
        filename2.lower()

        return ("previous_" in filename1) and ("previous_" in filename2)

    def formatTableString(self,tableString):
        tableString.lstrip()
        tableString = tableString.replace("<td> a href", '')
        tableString = tableString.replace("a  <td> align right", '')
        tableString = tableString.replace("a       ", '')
        tableString=tableString.replace("  http://",'http://')
        tableString=tableString.replace("  ",",")
        tableString=tableString.replace(" ",", ")
        tableString=tableString.replace(" (","(")
        tableString=tableString.replace("(","")
        tableString=tableString.replace(")","")
        tableString=tableString.replace("%","")
        tableString = tableString.replace(" ","")
        return tableString

#
# Inner class myHtmlParser extends HTMLParser
#
class myHtmlParser (HTMLParser):
    tableString=""
    seenTable=False
    seenEndOfTable=False

    def handle_starttag(self, tag, attrs):
        if(self.seenTable and (not self.seenEndOfTable)):
            if(tag=="tr" or tag=="td"):
                self.tableString = self.tableString + "<"+tag+">" + " "
            else:
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
