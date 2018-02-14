import unittest
from MossParser import MossParser
class MossParserUnitTest(unittest.TestCase):

    #Test for valid URL
        def testValidURL(self):
            mp = MossParser()
            self.assertTrue(mp.testUrl("http://moss.stanford.edu/results/322457013"))

    #Test for inValid URL
        def testInvalidURL(self):
            mp = MossParser()
            self.assertFalse(mp.testUrl("http://mosdf23s.stanford.edu/resdawesults/3224570wdsd13"))

    #Test method which takes a url string and returns an html file
        def testValidURL(self):
            mp = MossParser()
            html = urllib.request.urlopen("http://www.python.org")
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            fp.close()

            self.assertTrue(mp.getHtml("http://www.python.org") == mystr)


    #Test the processing of a valid html file into a list of table element strings

    #Test the processing of an invalid html file into a list of table elements strings

    #Test for valid csvstrings being made from the processTableStrings method
        def testValidProcessTableStrings(self):
            mp = MossParser()
            tableString = """"<tr><td><a href="http://moss.stanford.edu/results/322457013/match0.html">warmup36.java (94%)</a>
                         </td><td><a href="http://moss.stanford.edu/results/322457013/match0.html">warmup435.java (94%)</a>
                            </td><td align="right">12
                            </td></tr>"""

            testString = processTableString()
            assertTrue(tableString == testString)

    #Test for invalid csvstrings being made from the processTableStrings method
        def testInvalidProcessTableString(self):
            tableString = """"<tr><td><a href="http://moss.stanford.edu/results/322457013/match0.html">warmup36.java (94%)</a>
                            </td><td><a href="http://moss.stanford.edu/results/322457013/match0.html">warmup435.java (94%)</a>
                            </td></tr>"""
            testString = processTableString()
            assertFalse(tableString == testString)


    #test for valid Moss Result Object

            def testValidMossResult():
                mp=MossParser()
                self.assertTrue(mp.isValidMossResult("Sally","squareroot26.java","22","Sally","squareroot3.java",
                                                     "43","10","http://moss.stanford.edu/results/299782671/match15.html"))
    #test for invalid MOSS result object- no user 1

            def testInvalidMossResultUser1():
                mp = MossParser()
                self.assertFalse(mp.isValidMossResult("", "squareroot26.java", "22", "Sally", "squareroot3.java",
                                                     "43", "10", "http://moss.stanford.edu/results/299782671/match15.html"))

            def testInvalidMossResultUser2():
                mp = MossParser()
                self.assertFalse(mp.isValidMossResult("Sally", "squareroot26.java", "22", "", "squareroot3.java",
                                                     "43", "10", "http://moss.stanford.edu/results/299782671/match15.html"))
            def testInvalidMossResultFile1():
                mp = MossParser()
                self.assertFalse(mp.isValidMossResult("Sally", "", "22", "Sally", "squareroot3.java",
                                                     "43", "10", "http://moss.stanford.edu/results/299782671/match15.html"))
            def testInvalidMossResultFile2():
                mp = MossParser()
                self.assertFalse(mp.isValidMossResult("Sally", "squareroot26.java", "22", "Sally", "",
                                                     "43", "10", "http://moss.stanford.edu/results/299782671/match15.html"))
            def testInvalidMossResultLines1():
                MP=MossParser()
                mp = MossParser()
                self.assertFalse(mp.isValidMossResult("Sally", "squareroot26.java", "", "Sally", "squareroot3.java",
                                                     "43", "10", "http://moss.stanford.edu/results/299782671/match15.html"))
            def testInvalidMossResultLines2():
                MP=MossParser()
                mp = MossParser()
                self.assertFalse(mp.isValidMossResult("Sally", "squareroot26.java", "22", "Sally", "squareroot3.java",
                                                     "", "10", "http://moss.stanford.edu/results/299782671/match15.html"))
            def testInvalidMossResultLinesMatched():
                MP=MossParser()
                mp = MossParser()
                self.assertFalse(mp.isValidMossResult("Sally", "squareroot26.java", "22", "Sally", "squareroot3.java",
                                                     "43", "", "http://moss.stanford.edu/results/299782671/match15.html"))
            def testInvalidMossResultUrl():
                MP=MossParser()
                mp = MossParser()
                self.assertFalse(mp.isValidMossResult("Sally", "squareroot26.java", "22", "Sally", "squareroot3.java",
                                                     "43", "10", "http://moss.stanford.edu/results/299782671/match15.html"))

