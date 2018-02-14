#Class MossParser
#This class is designed to take a url as input and creates a csv file of results from MOSS in the same directory
#as this program
import urllib

class MossParser:

    def main(self):
        print ("need to work on class")
        #If this is not a valid URL display error and exit

        #get the html text from the URL
        #-> html = getHtml(some_url)

        #Process the html into table strings
        #-> tableStrings = processHtml(html)

        #Process the table strings into csv strings
        #-> csvStrings = processTableStrings(tableStrings)

        #Create, save, and close the csv file
    def testUrl(self,urlArg):
        request = urllib.request.Request(urlArg)
        try:
            response = urllib.request.urlopen(request)
            # response is now a string you can search through containing the page's html
            return True
        except:
            #The url wasn't valid
            return False
    def processHtml(self):
        return ""
    def processTableString(self):
        return """"<tr><td><a href="http://moss.stanford.edu/results/322457013/match0.html">warmup36.java (94%)</a>
                         </td><td><a href="http://moss.stanford.edu/results/322457013/match0.html">warmup435.java (94%)</a>
                            </td><td align="right">12
                            </td></tr>"""
    def getHtml(self, urlArg):
        html = urllib.request.urlopen("http://www.python.org")
        mybytes = html.read()
        mystr = mybytes.decode("utf8")
        html.close()
        return mystr

