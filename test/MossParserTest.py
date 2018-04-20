import unittest
import urllib
from Config import Config
from MossParser import MossParser

class MossParserUnitTest(unittest.TestCase):

    # - testValidURL() Test for valid URL
    # - testValidURL() Test for inValid URL
    # - testValidURL() Test for invalid URL that will return a 200 ok response
    # - testValidURL() Test testUrl on empty string
    # - testValidURL() Test testUrl on string "moss"
    # - testValidURL() Test testUrl on valid URL + extra chars
    # - testValidURL() Test testURL on carriage return
    # - testValidURL() Test testUrl on numeric value
    # - testValidURL() Test testUrl on list
    # - testValidURL() Test testUrl on a list of MOSS URL's
    # - testValidURL() Test testUrl on None
    # - testValidURL() Test testUrl on Valid IP
    # - getHtml() Test method on invalid MOSS URL
    # - getHtml() Test method on valid MOSS URL
    # - processHtml() Test on valid output
    # - processHtml() Test on invalid output
    # - getName() Test with previous file
    # - getName() Test with current file
    # - previousYearMatch() Test for current years (current, current)
    # - previousYearMatch() Test for different years (current, previous)
    # - previousYearMatch() Test for previous years (previous, previous)
    # - parseMultiple() Test for
    # - processTableStrings() Test for
    # - formatTableString() Test for
    # - testFileNaming() Test for
    # Tests for inner class "myHTMLParser"
    # - handle_starttag() Test for
    # - handle_endtag() Test for
    # - handle_data() Test for
    # - parse() Test for


    def setUp(self):
        self.mp = MossParser("csv.csv")
        self.config = Config()
        self.validUrl = self.config.getPalindrome()

#
# parse()
#

    def test_parse(self):
        url = Config.palindrome
        self.assertTrue(self.mp.parse(url))

    def test_parseInvalidURL(self):
        url = "fake url"
        self.assertFalse(self.mp.parse(url))

#
# testUrl()
#
    # Test for valid URL
    def test_validURL(self):
        self.assertTrue(self.mp.testUrl(self.validUrl))

    # Test for inValid URL
    def test_invalidURL(self):
        self.assertFalse(self.mp.testUrl("http://mosdf23s.stanford.edu/resdawesults/3224570wdsd13"))

    # Test for invalid URL that will return a 200 ok response
    def test_invalidURLOnResponseCode200OK(self):
        self.assertFalse(self.mp.testUrl("http://google.com"))

    # Test testUrl on empty string
    def test_invalidURLOnEmptyString(self):
        self.assertFalse(self.mp.testUrl(""))

    # Test testUrl on string "moss"
    def test_invalidURLOnMOSSString(self):
        self.assertFalse(self.mp.testUrl("http://moss.stanford.edu"))

    # Test testUrl on valid URL + extra chars
    def test_invalidURLOnValidPlusExtra(self):
        appendChars = ['a', '\?', ':', '+', 'z', ' ', '\n']
        for char in appendChars:
            self.assertFalse(self.mp.testUrl(self.validUrl + char))

    # Test testURL on carriage return
    def test_invalidURLOnCarriageReturn(self):
        self.assertFalse(self.mp.testUrl("\n"))

    # Test testUrl on numeric value
    def test_invalidURLOnNumericValue(self):
        self.assertFalse(self.mp.testUrl(12345))

    # Test testUrl on list
    def test_invalidURLOnList(self):
        l = ['a', 1, '$']
        self.assertFalse(self.mp.testUrl(l))

    # Test testUrl on a list of MOSS URL's
    def test_invalidURLOnListOfMOSSURLs(self):
        l = [self.config.getPalindrome(), self.config.getTwentyone(), self.config.getMagicsquare()]
        self.assertFalse(self.mp.testUrl(l))

    # Test testUrl on None
    def test_invalidURLOnNone(self):
        self.assertFalse(self.mp.testUrl(None))

    # Test testUrl on Valid IP
    def test_validURLOnIP(self):
        IP = self.validUrl.replace("moss.stanford.edu", "171.64.78.49")
        self.assertTrue(self.mp.testUrl(str(IP)))


#
# getHtml()
#
    # Test method on a non utf8 webpage
    # def test_validHtmlOnNonUTF8Webpage(self):
    #     html = urllib.request.urlopen("https://www.google.com")
    #     mybytes = html.read()
    #     mystr = mybytes.decode("utf16")
    #     html.close()
    #     self.assertFalse(self.mp.getHtml("https://www.google.com") == mystr)

    # Test method on invalid MOSS URL
    def test_validHTMLOnInvalidURL(self):
        self.assertIsNone(self.mp.getHtml(self.validUrl + "a"))

    # Test method on valid MOSS URL
    def test_validHTMLOnValidMOSSURL(self):
        html = urllib.request.urlopen(self.validUrl)
        mybytes = html.read()
        mystr = mybytes.decode("utf8")
        html.close()
        self.assertTrue(self.mp.getHtml(self.validUrl) == mystr)


#
# processHtml()
#
    # 4. Test the processing of a valid html file into a list of table element strings
    #def test_validHtmlProcessing(self):
    #    mossUrlNumber = self.config.getPalindrome()[33:]
    #    testList=[""" <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match0.html clannister_Warmup.java (82%) a      <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match0.html jbaxter5_Warmup.java (72%) a  <td> align right 17 """,
#""" <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match1.html jbaxter5_Warmup.java (65%) a      <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match1.html stentacles_Warmup.java (86%) a  <td> align right 16 """,
#""" <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match2.html clannister_Warmup.java (74%) a      <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match2.html stentacles_Warmup.java (86%) a  <td> align right 16 """,
#""" <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match3.html hlloyd_Warmup.java (70%) a      <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match3.html hpataki_Warmup.java (70%) a  <td> align right 9 """,
#""" <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match4.html fbordeau_Warmup.java (94%) a      <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match4.html rlupin_Warmup.java (68%) a  <td> align right 13 """,
#""" <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match5.html previous_asillz_Warmup.java (86%) a      <td> a href http://moss.stanford.edu/results/""" + mossUrlNumber + """/match5.html previous_scarter_Warmup.java (86%) a  <td> align right 13 """,
#]
        #testList2=self.mp.processHtml(self.mp.getHtml(self.config.getPalindrome()))
        #self.assertTrue(len(testList) == len(testList2) and sorted(testList) == sorted(testList2))

    # 5. Test the processing of an invalid html file into a list of table elements strings
    def test_invalidHtmlProcessing(self):
        self.assertNotEqual(["""<tr><td><a href="http://moss.stanford.edu/results/11690537/match0.html">delrick_Palindrome.java (59%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match0.html">jcary_Palindrome.java (69%)</a>
                            </td><td align="right">28
                            </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match1.html">jcary_Palindrome.java (55%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match1.html">lhbox_Palindrome.java (39%)</a>
                             </td><td align="right">18
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match2.html">relliot_Palindrome.java (42%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match2.html">tbassett_Palindrome.java (52%)</a>
                             </td><td align="right">16
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match3.html">delrick_Palindrome.java (40%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match3.html">lhbox_Palindrome.java (33%)</a>
                             </td><td align="right">15
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match4.html">mmarquez2_Palindrome.java (31%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match4.html">relliot_Palindrome.java (34%)</a>
                             </td><td align="right">14
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match5.html">cchase_Palindrome.java (16%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match5.html">ssmith_Palindrome.java (21%)</a>
                             </td><td align="right">12
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match6.html">ssmith_Palindrome.java (21%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match6.html">tbassett_Palindrome.java (33%)</a>
                             </td><td align="right">6
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match7.html">lhbox_Palindrome.java (22%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match7.html">tbassett_Palindrome.java (33%)</a>
                             </td><td align="right">10
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match8.html">jcary_Palindrome.java (31%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match8.html">tbassett_Palindrome.java (33%)</a>
                             </td><td align="right">9
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match9.html">qbinkin4_Palindrome.java (33%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match9.html">sfath1_Palindrome.java (21%)</a>
                             </td><td align="right">8
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match10.html">qbinkin4_Palindrome.java (33%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match10.html">relliot_Palindrome.java (25%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match11.html">mmarquez2_Palindrome.java (22%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match11.html">qbinkin4_Palindrome.java (33%)</a>
                             </td><td align="right">6
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match12.html">delrick_Palindrome.java (25%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match12.html">whark_Palindrome.java (27%)</a>
                             </td><td align="right">9
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match13.html">cchase_Palindrome.java (12%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match13.html">delrick_Palindrome.java (21%)</a>
                             </td><td align="right">8
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match14.html">lhbox_Palindrome.java (17%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match14.html">whark_Palindrome.java (22%)</a>
                             </td><td align="right">8
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match15.html">jcary_Palindrome.java (24%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match15.html">whark_Palindrome.java (22%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match16.html">dmell_Palindrome.java (30%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match16.html">zhillier_Palindrome.java (20%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match17.html">delrick_Palindrome.java (20%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match17.html">zhillier_Palindrome.java (20%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match18.html">delrick_Palindrome.java (20%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match18.html">dmell_Palindrome.java (30%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match19.html">tbassett_Palindrome.java (24%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match19.html">zhillier_Palindrome.java (20%)</a>
                             </td><td align="right">6
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match20.html">lhbox_Palindrome.java (16%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match20.html">zhillier_Palindrome.java (20%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match21.html">jcary_Palindrome.java (23%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match21.html">zhillier_Palindrome.java (20%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match22.html">dmell_Palindrome.java (28%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match22.html">tbassett_Palindrome.java (24%)</a>
                             </td><td align="right">6
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match23.html">dmell_Palindrome.java (28%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match23.html">relliot_Palindrome.java (19%)</a>
                             </td><td align="right">10
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match24.html">dmell_Palindrome.java (28%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match24.html">lhbox_Palindrome.java (16%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match25.html">dmell_Palindrome.java (28%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match25.html">jcary_Palindrome.java (23%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match26.html">delrick_Palindrome.java (19%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match26.html">tbassett_Palindrome.java (24%)</a>
                             </td><td align="right">6
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match27.html">cchase_Palindrome.java (11%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match27.html">zhillier_Palindrome.java (20%)</a>
                             </td><td align="right">8
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match28.html">cchase_Palindrome.java (11%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match28.html">dmell_Palindrome.java (28%)</a>
                             </td><td align="right">8
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match29.html">sfath1_Palindrome.java (16%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match29.html">tbassett_Palindrome.java (23%)</a>
                             </td><td align="right">6
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match30.html">relliot_Palindrome.java (18%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match30.html">ssmith_Palindrome.java (15%)</a>
                             </td><td align="right">8
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match31.html">qbinkin4_Palindrome.java (25%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match31.html">tbassett_Palindrome.java (23%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match32.html">mmarquez2_Palindrome.java (17%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match32.html">tbassett_Palindrome.java (23%)</a>
                             </td><td align="right">4
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match33.html">mmarquez2_Palindrome.java (17%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match33.html">ssmith_Palindrome.java (15%)</a>
                             </td><td align="right">4
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match34.html">lhbox_Palindrome.java (15%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match34.html">sfath1_Palindrome.java (16%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match35.html">lhbox_Palindrome.java (15%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match35.html">qbinkin4_Palindrome.java (25%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match36.html">jcary_Palindrome.java (22%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match36.html">sfath1_Palindrome.java (16%)</a>
                             </td><td align="right">6
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match37.html">jcary_Palindrome.java (22%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match37.html">qbinkin4_Palindrome.java (25%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match38.html">eyo_Palindrome.java (19%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match38.html">ssmith_Palindrome.java (15%)</a>
                             </td><td align="right">8
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match39.html">cchase_Palindrome.java (11%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match39.html">tbassett_Palindrome.java (23%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match40.html">cchase_Palindrome.java (11%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match40.html">lhbox_Palindrome.java (15%)</a>
                             </td><td align="right">7
                             </td></tr>""",

                             """<tr><td><a href="http://moss.stanford.edu/results/11690537/match41.html">cchase_Palindrome.java (11%)</a>
                                 </td><td><a href="http://moss.stanford.edu/results/11690537/match41.html">jcary_Palindrome.java (22%)</a>
                             </td><td align="right">7
                             </td></tr>"""], self.mp.processHtml(self.mp.getHtml(self.config.getPalindrome())))

#
# getName()
#
    # 6. Test getName with previous file
    def test_getName_previuos(self):
        string = "previous_msmith_HomeValue.java (21%)"
        self.assertEqual(self.mp.getName(string), "msmith")

    #7.  Test get name with current file
    def test_getName_current (self):
        string = "msmith_HomeValue.java (21%)"
        self.assertEqual(self.mp.getName(string), "msmith")


#
# previousyearMatch()
#
    # 8. Test for same year assignment
    def test_currentYears(self):
        file1="lhbox_HomeValue.java"
        file2="eyo_HomeValue.java"
        self.assertFalse(self.mp.previousYearMatch(file1,file2))

    # 9. Test for different year assignment
    def test_differentYears(self):
        file1 = "previous_lhbox_HomeValue.java"
        file2 = "eyo_HomeValue.java"
        self.assertFalse(self.mp.previousYearMatch(file1, file2))


    # 10. Test for past assignments
    def test_previousYears(self):
        file1 = "previous_lhbox_HomeValue.java"
        file2 = "previous_eyo_HomeValue.java"
        self.assertTrue(self.mp.previousYearMatch(file1,file2))

    #difference in capitalization
    def test_previousYears(self):
        file1 = "previous_test.java"
        file2 = "PREVIOUS_test2.java"
        self.assertTrue(self.mp.previousYearMatch(file1, file2))

    #difference in capitalization in both files
    def test_previousYears(self):
        file1 = "pReviOus_test.java"
        file2 = "PReVIOUS_test2.java"
        self.assertTrue(self.mp.previousYearMatch(file1, file2))

    #incorrect spelling of previous
    def test_previousYears(self):
        file1 = "pr3vious_test.java"
        file2 = "previous_test2.java"
        self.assertFalse(self.mp.previousYearMatch(file1, file2))

    #incorrect use of special characters
    def test_previousYears(self):
        file1 = "previ0us_test.java"
        file2 = "previou$_test2.java"
        self.assertFalse(self.mp.previousYearMatch(file1, file2))

    # missing '_' in name
    def test_previousYears(self):
        file1 = "previoustest.java"
        file2 = "previous_test2.java"
        self.assertFalse(self.mp.previousYearMatch(file1, file2))

    # dash does not count as underscore
    def test_previousYears(self):
        file1 = "previous-test.java"
        file2 = "previous_test2.java"
        self.assertFalse(self.mp.previousYearMatch(file1, file2))
#
# processTableStrings()
#

    #Testing on no output
    def test_processTableStrings1(self):
        f = open('testurls.txt')
        testlines = f.readlines()
        url = testlines[0]
        url=url.replace('\n','')
        html = self.mp.getHtml(url)
        tableStrings = self.mp.processHtml(html)
        result = self.mp.processTableStrings(tableStrings)
        self.assertTrue(result, "")

    #Testing on expected output
    #def test_processTableStrings2(self):
    #    f = open('testurls.txt')
    #    testlines = f.readlines()
    #    url = testlines[1]
    #    url=url.replace('\n','')
    #    mossNumber = url[33:]
    #    html = self.mp.getHtml(url)
    #    tableStrings = self.mp.processHtml(html)
    #    result = self.mp.processTableStrings(tableStrings)
    #    expected = ([["jbaxter5","jbaxter5_Warmup.java","65","stentacles","stentacles_Warmup.java","86","16","http://moss.stanford.edu/results/"+mossNumber+"/match0.html"],
    #                ["jbaxter5","jbaxter5_Insipid.java","17","stentacles","stentacles_Insipid.java","17","11","http://moss.stanford.edu/results/"+mossNumber+"/match1.html"]], True)
    #    self.assertEqual(result, expected)

    #Testing on expected output
    #def test_processTableStrings3(self):
    #    f = open('testurls.txt')
    #    testlines = f.readlines()
    #    url = testlines[2]
    #    url=url.replace('\n','')
    #    mossNumber = url[33:]
    #    html = self.mp.getHtml(url)
    #    tableStrings = self.mp.processHtml(html)
    #    result = self.mp.processTableStrings(tableStrings)
    #    expected = ([["jbaxter5","jbaxter5_Warmup.java","91","jbaxter5","jbaxter5_Warmup.java","91","12","http://moss.stanford.edu/results/"+mossNumber+"/match0.html"]], True)
    #    self.assertEqual(result, expected)

    #Testing on unexpected output
    #def test_processTableStrings4(self):
     #   f = open('testurls.txt')
      #  testlines = f.readlines()
       # url = testlines[4]
       # url=url.replace('\n','')
       # html = self.mp.getHtml(url)
       # tableStrings = self.mp.processHtml(html)
       # result = self.mp.processTableStrings(tableStrings)
       # expected = ([[ "jter_Warmup.java,91,jbaxter_Warmup.java,91,12,http://moss.stanford.edu/results/20984829/match0.html"]],True)
       # self.assertNotEqual(result, expected)
#
# testFileNaming()
#
    #-.Test that filename is string
    def test_fileIsString(self):
        file1 = "eyo_HomeValue.java"
        self.assertTrue(self.mp.testFileNaming(file1))

 # -.Test that filename is a digit
    def test_fileIsDigit(self):
        file1 = "558924359787"
        self.assertFalse(self.mp.testFileNaming(file1))

    # no '_' which would need a username appended to the front
    def test_testFileNaming(self):
        file = "invalidfile.java"
        self.assertFalse(self.mp.testFileNaming(file))

    # this naming is valid because it
    def test_testFileNaming2(self):
        file = "bsmith_validfile.java"
        self.assertTrue(self.mp.testFileNaming(file))

    # no extension needed
    def test_testFileNaming3(self):
        file = "bsmith_validfile"
        self.assertTrue(self.mp.testFileNaming(file))

    # underscore precedes the filename
    def test_testFileNaming4(self):
        file = "_bsmithinvalidfile.java"
        self.assertFalse(self.mp.testFileNaming(file))

    # valid filename but underscore precedes the filename, making it invalid
    def test_testFileNaming5(self):
        file = "_bsmith_invalidfile.java"
        self.assertFalse(self.mp.testFileNaming(file))

    #get table string values test, make sure the split functionality works
    def test_getTableStringValues(self):
        response = self.mp.getTableStringValues("jbxter_Warmup.java,91,jbaxter_Warmup.java,91,12,http://moss.stanford.edu/results/20984829/match0.html")
        expected = ["jbxter_Warmup.java","91","jbaxter_Warmup.java","91","12","http://moss.stanford.edu/results/20984829/match0.html"]
        self.assertEqual(response,expected)

    #tests for invalid strings
    def test_getTableStringValues1(self):
        #self.assertFalse(self.mp.getTableStringValues("this is not a valid string"))
        self.assertTrue(self.mp.getTableStringValues("this,is,a,valid,string"))

    # assert the length is valid
    def test_getTableStringValues2(self):
        response = self.mp.getTableStringValues("jbxter_Warmup.java,91,jbaxter_Warmup.java,91,12,http://moss.stanford.edu/results/20984829/match0.html")
        self.assertTrue((len(response)==6))

    def test_formatTableString(self):
        data = "<td> a href http://moss.stanford.edu/results/490959839/match249.html jlacey_Rodentia.java (9%) a      <td> a href http://moss.stanford.edu/results/490959839/match249.html pbaelish_Rodentia.java (10%) a  <td> align right 16 "
        result = self.mp.formatTableString(data)
        expected = ",http://moss.stanford.edu/results/490959839/match249.html,jlacey_Rodentia.java,9,http://moss.stanford.edu/results/490959839/match249.html,pbaelish_Rodentia.java,10,16,"
        self.assertEqual(result, expected)

#
# parse()
#
    # Break method if getHtml(url) returns None
    def test_InvalidMossUrl(self):
        self.assertFalse(self.mp.parse("invalid.com"))

#
# toCsv()
#
    # Correct write with 'w'
    def test_validWriteCsvStrings(self):
        csvStrings = [['clannister', 'clannister_Warmup.java', '82', 'jbaxter5', 'jbaxter5_Warmup.java', '72', '17', 'http://moss.stanford.edu/results/373890203/match0.html']]
        self.assertTrue(self.mp.toCsv(csvStrings, 'w'))

    # Correct write with 'a'
    def test_validAppendCsvStrings(self):
        csvStrings = [['clannister', 'clannister_Warmup.java', '82', 'jbaxter5', 'jbaxter5_Warmup.java', '72', '17', 'http://moss.stanford.edu/results/373890203/match0.html']]
        self.assertTrue(self.mp.toCsv(csvStrings, 'a'))

    # Invalid type to write/append
    def test_invalidTypeForWriteOrAppend(self):
        csvStrings = [['clannister', 'clannister_Warmup.java', '82', 'jbaxter5', 'jbaxter5_Warmup.java', '72', '17', 'http://moss.stanford.edu/results/373890203/match0.html']]
        self.assertFalse(self.mp.toCsv(csvStrings, 'z'))

    # Invalid CsvStrings type
    def test_invalidCsvStringsTypeInt(self):
        self.assertFalse(self.mp.toCsv(5, 'a'))

    # CsvStrings needs to be a list
    def test_invalidCsvStringsTypeString(self):
        self.assertFalse(self.mp.toCsv('string', 'a'))

    # Invalid type of write/append argument
    def test_invalidTypeInt(self):
        csvStrings = [['clannister', 'clannister_Warmup.java', '82', 'jbaxter5', 'jbaxter5_Warmup.java', '72', '17', 'http://moss.stanford.edu/results/373890203/match0.html']]
        self.assertFalse(self.mp.toCsv(csvStrings, 5))



if __name__ == '__main__':
    unittest.main()