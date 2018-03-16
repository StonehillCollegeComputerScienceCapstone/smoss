import unittest
import urllib
import ssl
from MossParser import MossParser
class MossParserUnitTest(unittest.TestCase):

    # 1. Test testValidURL() on an valid url
    # 2. Test testValidURL() on an invalid url
    # 3. Test getHtml() on a valid url
    # 4. Test processHtml() on valid output
    # 5. Test processHtml() on invalid output
    # 6. Test getName()
    # 7. Test for same year assignment
    # 8. Test for different year assignment

    def setUp(self):
        self.mp = MossParser("csv.csv")

#
# testUrl()
#
    # 1. Test for valid URL
    def test_validURL(self):
        self.assertTrue(self.mp.testUrl("http://moss.stanford.edu/results/558206563"))

    # 2. Test for inValid URL
    def test_invalidURL(self):
        self.assertFalse(self.mp.testUrl("http://mosdf23s.stanford.edu/resdawesults/3224570wdsd13"))

#
# getHtml()
#
    # 3. Test method which takes a url string and returns an html file
    def test_validHtml(self):
        html = urllib.request.urlopen("https://www.python.org")
        mybytes = html.read()
        mystr = mybytes.decode("utf8")
        html.close()
        self.assertTrue(self.mp.getHtml("https://www.python.org") == mystr)

#
# processHtml()
#
    # 4. Test the processing of a valid html file into a list of table element strings
    def test_validHtmlProcessing(self):
        self.assertTrue(["""<td><td><a href="http://moss.stanford.edu/results/11690537/match0.html">delrick_Palindrome.java (59%)</a>
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
                         </td></tr>"""], self.mp.processHtml(self.mp.getHtml("http://moss.stanford.edu/results/558206563")))

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
                             </td></tr>"""], self.mp.processHtml(self.mp.getHtml("http://moss.stanford.edu/results/558206563")))

#
# getName()
#
    # 6. Test getName()
    def test_getName(self):
        string = "2018_msmith_HomeValue.java (21%)"
        self.assertEqual(self.mp.getName(string), "msmith")

#
# yearMatch()
#
    # 7. Test for same year assignment
    def test_sameYears(self):
        FileList = (
            """ td a href http://moss.stanford.edu/results/558206563/match0.html 2018_lhbox_HomeValue.java (21%) a      td a href http://moss.stanford.edu/results/558206563/match0.html 2018_ssmith_HomeValue.java (30%) a  td align right 67 """,
            """ td a href http://moss.stanford.edu/results/558206563/match1.html 2018_eyo_HomeValue.java (15%) a      td a href http://moss.stanford.edu/results/558206563/match1.html 2018_jcary_HomeValue.java (16%) a  td align right 18 """)
        self.assertTrue(self.mp.yearMatch(FileList))

    # 8. Test for different year assignment
    def test_differentYears(self):
        FileList = (
            """ td a href http://moss.stanford.edu/results/558206563/match0.html 2017_lhbox_HomeValue.java (21%) a      td a href http://moss.stanford.edu/results/558206563/match0.html 2018_ssmith_HomeValue.java (30%) a  td align right 67 """,
            """ td a href http://moss.stanford.edu/results/558206563/match1.html 2018_eyo_HomeValue.java (15%) a      td a href http://moss.stanford.edu/results/558206563/match1.html 2018_jcary_HomeValue.java (16%) a  td align right 18 """)
        self.assertFalse(self.mp.yearMatch(FileList))

if __name__ == '__main__':
    unittest.main()