import unittest
import urllib
from Config import Config
from MossParser import MossParser

class MossParserUnitTest(unittest.TestCase):

    # - Test testValidURL() on an valid url
    # - Test testValidURL() on an invalid url
    # - Test getHtml() on a valid url
    # - Test processHtml() on valid output
    # - Test processHtml() on invalid output
    # - Test getName() with previous file
    # - Test getName() with current file
    # - Test for previousYearMatch() for current years (current, current)
    # - Test for previousYearMatch() for different years (current, previous)
    # - Test for previousYearMatch() for previous years (previous, previous)
    # New tests March 26th
    # - Test for parseMultiple()
    # - Test for processTableStrings()
    # - Test for parse()
    # - Test for formatTableString()
    # - Test for testFileNaming()
    # Tests for inner class "myHTMLParser"
    # - Test for handle_starttag()
    # - Test for handle_endtag()
    # - Test for handle_data()


    def setUp(self):
        self.mp = MossParser("csv.csv")
        self.config = Config()
        self.validUrl = self.config.getWarmup()

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
        appendChars = ['a', '?', ':', '#', '+', 'z', ' ', '\n']
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
        l = [self.config.getWarmup(), self.config.getInsipid(), self.config.getRodentia()]
        self.assertFalse(self.mp.testUrl(l))

    # Test testUrl on None
    def test_invalidURLOnNone(self):
        self.assertFalse(self.mp.testUrl(None))

    # Test testUrl on Valid IP
    def test_invalidURLOnIP(self):
        IP = self.validUrl.replace("moss.stanford.edu", "171.64.78.49")
        self.assertTrue(self.mp.testUrl(IP))


#
# getHtml()
#
    # Test method on a non utf8 webpage
    def test_validHtmlOnNonUTF8Webpage(self):
        html = urllib.request.urlopen("https://www.google.com")
        mybytes = html.read()
        mystr = mybytes.decode("utf16")
        html.close()
        self.assertFalse(self.mp.getHtml("https://www.google.com") == mystr)

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
    def test_validHtmlProcessing(self):
        self.assertEqual(["""<td><td><a href="http://moss.stanford.edu/results/11690537/match0.html">delrick_Palindrome.java (59%)</a>
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
                         </td></tr>"""], self.mp.processHtml(self.mp.getHtml(self.config.getWarmup())))

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
                             </td></tr>"""], self.mp.processHtml(self.mp.getHtml(self.config.getWarmup())))

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



   
#
# processTableStrings()
#

if __name__ == '__main__':
    unittest.main()