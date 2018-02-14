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
            mybytes = html.read()
            mystr = mybytes.decode("utf8")
            html.close()

            self.assertTrue(mp.getHtml("http://www.python.org") == mystr)


    #Test the processing of a valid html file into a list of table element strings
        def testValidHtmlProcessing(self):
            mp=MossParser()

            self.assertTrue(["""<tr><td><a href="http://moss.stanford.edu/results/299782671/match0.html">squareroot29.java (93%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match0.html">squareroot36.java (80%)</a>
</td><td align="right">38
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match1.html">squareroot10.java (24%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match1.html">squareroot33.java (43%)</a>
</td><td align="right">18
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match2.html">squareroot1.java (51%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match2.html">squareroot29.java (49%)</a>
</td><td align="right">15
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match3.html">squareroot26.java (37%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match3.html">squareroot8.java (45%)</a>
</td><td align="right">12
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match4.html">squareroot1.java (35%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match4.html">squareroot36.java (29%)</a>
</td><td align="right">10
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match5.html">squareroot24.java (37%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match5.html">squareroot8.java (32%)</a>
</td><td align="right">9
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match6.html">squareroot24.java (37%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match6.html">squareroot26.java (27%)</a>
</td><td align="right">9
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match7.html">squareroot34.java (47%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match7.html">squareroot5.java (37%)</a>
</td><td align="right">9
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match8.html">squareroot35.java (30%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match8.html">squareroot8.java (30%)</a>
</td><td align="right">9
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match9.html">squareroot34.java (45%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match9.html">squareroot8.java (30%)</a>
</td><td align="right">9
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match10.html">squareroot26.java (25%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match10.html">squareroot35.java (30%)</a>
</td><td align="right">9
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match11.html">squareroot26.java (25%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match11.html">squareroot34.java (45%)</a>
</td><td align="right">9
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match12.html">squareroot24.java (33%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match12.html">squareroot34.java (43%)</a>
</td><td align="right">8
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match13.html">squareroot1.java (30%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match13.html">squareroot24.java (33%)</a>
</td><td align="right">9
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match14.html">squareroot3.java (43%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match14.html">squareroot8.java (27%)</a>
</td><td align="right">10
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match15.html">squareroot26.java (22%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match15.html">squareroot3.java (43%)</a>
</td><td align="right">10
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match16.html">squareroot1.java (29%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match16.html">squareroot8.java (27%)</a>
</td><td align="right">8
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match17.html">squareroot1.java (29%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match17.html">squareroot26.java (22%)</a>
</td><td align="right">8
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match18.html">squareroot3.java (40%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match18.html">squareroot35.java (26%)</a>
</td><td align="right">10
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match19.html">squareroot1.java (25%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match19.html">squareroot34.java (36%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match20.html">squareroot5.java (25%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match20.html">squareroot8.java (21%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match21.html">squareroot35.java (21%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match21.html">squareroot5.java (25%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match22.html">squareroot34.java (31%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match22.html">squareroot35.java (21%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match23.html">squareroot26.java (17%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match23.html">squareroot5.java (25%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match24.html">squareroot11.java (15%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match24.html">squareroot35.java (21%)</a>
</td><td align="right">6
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match25.html">squareroot24.java (23%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match25.html">squareroot5.java (23%)</a>
</td><td align="right">6
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match26.html">squareroot24.java (23%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match26.html">squareroot35.java (20%)</a>
</td><td align="right">6
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match27.html">squareroot33.java (17%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match27.html">squareroot8.java (19%)</a>
</td><td align="right">5
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match28.html">squareroot33.java (17%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match28.html">squareroot34.java (28%)</a>
</td><td align="right">5
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match29.html">squareroot26.java (16%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match29.html">squareroot33.java (17%)</a>
</td><td align="right">5
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match30.html">squareroot24.java (22%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match30.html">squareroot33.java (17%)</a>
</td><td align="right">5
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match31.html">squareroot22.java (22%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match31.html">squareroot33.java (17%)</a>
</td><td align="right">10
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match32.html">squareroot1.java (20%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match32.html">squareroot33.java (17%)</a>
</td><td align="right">5
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match33.html">squareroot31.java (16%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match33.html">squareroot36.java (15%)</a>
</td><td align="right">6
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match34.html">squareroot29.java (18%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match34.html">squareroot31.java (16%)</a>
</td><td align="right">11
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match35.html">squareroot36.java (15%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match35.html">squareroot5.java (20%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match36.html">squareroot34.java (25%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match36.html">squareroot36.java (15%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match37.html">squareroot33.java (15%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match37.html">squareroot5.java (20%)</a>
</td><td align="right">5
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match38.html">squareroot33.java (15%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match38.html">squareroot35.java (17%)</a>
</td><td align="right">5
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match39.html">squareroot3.java (26%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match39.html">squareroot5.java (20%)</a>
</td><td align="right">8
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match40.html">squareroot3.java (26%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match40.html">squareroot34.java (25%)</a>
</td><td align="right">8
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match41.html">squareroot29.java (17%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match41.html">squareroot5.java (20%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match42.html">squareroot29.java (17%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match42.html">squareroot34.java (25%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match43.html">squareroot22.java (19%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match43.html">squareroot5.java (20%)</a>
</td><td align="right">12
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match44.html">squareroot22.java (19%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match44.html">squareroot35.java (17%)</a>
</td><td align="right">7
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match45.html">squareroot22.java (19%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match45.html">squareroot3.java (26%)</a>
</td><td align="right">6
</td></tr>""",
"""<tr><td><a href="http://moss.stanford.edu/results/299782671/match46.html">squareroot2.java (29%)</a>
    </td><td><a href="http://moss.stanford.edu/results/299782671/match46.html">squareroot22.java (19%)</a>
</td><td align="right">
</td></tr>"""],mp.processHtml())



        #Test the processing of an invalid html file into a list of table elements strings
        def testInvalidHtmlProcessing(self):
            mp = MossParser()

            self.assertFalse(["""<td><td><a href="http://moss.stanford.edu/results/299782671/match0.html">squareroot29.java (93%)</a>
        </td><td><a href="http://moss.stanford.edu/results/299782671/match0.html">squareroot36.java (80%)</a>
    </td><td align="right">38
    </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match1.html">squareroot10.java (24%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match1.html">squareroot33.java (43%)</a>
                         </td><td align="right">18
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match2.html">squareroot1.java (51%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match2.html">squareroot29.java (49%)</a>
                         </td><td align="right">15
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match3.html">squareroot26.java (37%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match3.html">squareroot8.java (45%)</a>
                         </td><td align="right">12
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match4.html">squareroot1.java (35%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match4.html">squareroot36.java (29%)</a>
                         </td><td align="right">10
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match5.html">squareroot24.java (37%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match5.html">squareroot8.java (32%)</a>
                         </td><td align="right">9
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match6.html">squareroot24.java (37%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match6.html">squareroot26.java (27%)</a>
                         </td><td align="right">9
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match7.html">squareroot34.java (47%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match7.html">squareroot5.java (37%)</a>
                         </td><td align="right">9
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match8.html">squareroot35.java (30%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match8.html">squareroot8.java (30%)</a>
                         </td><td align="right">9
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match9.html">squareroot34.java (45%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match9.html">squareroot8.java (30%)</a>
                         </td><td align="right">9
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match10.html">squareroot26.java (25%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match10.html">squareroot35.java (30%)</a>
                         </td><td align="right">9
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match11.html">squareroot26.java (25%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match11.html">squareroot34.java (45%)</a>
                         </td><td align="right">9
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match12.html">squareroot24.java (33%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match12.html">squareroot34.java (43%)</a>
                         </td><td align="right">8
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match13.html">squareroot1.java (30%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match13.html">squareroot24.java (33%)</a>
                         </td><td align="right">9
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match14.html">squareroot3.java (43%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match14.html">squareroot8.java (27%)</a>
                         </td><td align="right">10
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match15.html">squareroot26.java (22%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match15.html">squareroot3.java (43%)</a>
                         </td><td align="right">10
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match16.html">squareroot1.java (29%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match16.html">squareroot8.java (27%)</a>
                         </td><td align="right">8
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match17.html">squareroot1.java (29%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match17.html">squareroot26.java (22%)</a>
                         </td><td align="right">8
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match18.html">squareroot3.java (40%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match18.html">squareroot35.java (26%)</a>
                         </td><td align="right">10
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match19.html">squareroot1.java (25%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match19.html">squareroot34.java (36%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match20.html">squareroot5.java (25%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match20.html">squareroot8.java (21%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match21.html">squareroot35.java (21%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match21.html">squareroot5.java (25%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match22.html">squareroot34.java (31%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match22.html">squareroot35.java (21%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match23.html">squareroot26.java (17%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match23.html">squareroot5.java (25%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match24.html">squareroot11.java (15%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match24.html">squareroot35.java (21%)</a>
                         </td><td align="right">6
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match25.html">squareroot24.java (23%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match25.html">squareroot5.java (23%)</a>
                         </td><td align="right">6
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match26.html">squareroot24.java (23%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match26.html">squareroot35.java (20%)</a>
                         </td><td align="right">6
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match27.html">squareroot33.java (17%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match27.html">squareroot8.java (19%)</a>
                         </td><td align="right">5
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match28.html">squareroot33.java (17%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match28.html">squareroot34.java (28%)</a>
                         </td><td align="right">5
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match29.html">squareroot26.java (16%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match29.html">squareroot33.java (17%)</a>
                         </td><td align="right">5
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match30.html">squareroot24.java (22%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match30.html">squareroot33.java (17%)</a>
                         </td><td align="right">5
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match31.html">squareroot22.java (22%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match31.html">squareroot33.java (17%)</a>
                         </td><td align="right">10
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match32.html">squareroot1.java (20%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match32.html">squareroot33.java (17%)</a>
                         </td><td align="right">5
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match33.html">squareroot31.java (16%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match33.html">squareroot36.java (15%)</a>
                         </td><td align="right">6
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match34.html">squareroot29.java (18%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match34.html">squareroot31.java (16%)</a>
                         </td><td align="right">11
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match35.html">squareroot36.java (15%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match35.html">squareroot5.java (20%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match36.html">squareroot34.java (25%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match36.html">squareroot36.java (15%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match37.html">squareroot33.java (15%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match37.html">squareroot5.java (20%)</a>
                         </td><td align="right">5
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match38.html">squareroot33.java (15%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match38.html">squareroot35.java (17%)</a>
                         </td><td align="right">5
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match39.html">squareroot3.java (26%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match39.html">squareroot5.java (20%)</a>
                         </td><td align="right">8
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match40.html">squareroot3.java (26%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match40.html">squareroot34.java (25%)</a>
                         </td><td align="right">8
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match41.html">squareroot29.java (17%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match41.html">squareroot5.java (20%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match42.html">squareroot29.java (17%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match42.html">squareroot34.java (25%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match43.html">squareroot22.java (19%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match43.html">squareroot5.java (20%)</a>
                         </td><td align="right">12
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match44.html">squareroot22.java (19%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match44.html">squareroot35.java (17%)</a>
                         </td><td align="right">7
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match45.html">squareroot22.java (19%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match45.html">squareroot3.java (26%)</a>
                         </td><td align="right">6
                         </td></tr>""",
                         """<tr><td><a href="http://moss.stanford.edu/results/299782671/match46.html">squareroot2.java (29%)</a>
                             </td><td><a href="http://moss.stanford.edu/results/299782671/match46.html">squareroot22.java (19%)</a>
                         </td><td align="right">
                         </td></tr>"""], mp.processHtml())

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

if __name__ == '__main__':
    unittest.main()