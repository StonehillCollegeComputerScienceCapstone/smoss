import unittest
from Result import Result


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.result = Result(1, "f1", "f2", "url", 40, 50, 60)

#
# getters
#
    def test_getAssignmentNumber(self):
        self.assertEqual(1, self.result.getAssignmentNumber())

    def test_getFileOne(self):
        self.assertEqual("f1", self.result.getFileOne())

    def test_getFileTwo(self):
        self.assertEqual("f2", self.result.getFileTwo())

    def test_getUrl(self):
        self.assertEqual("url", self.result.getUrl())

    def test_getPercentOne(self):
        self.assertEqual(40, self.result.getPercentOne())

    def test_getPercentTwo(self):
        self.assertEqual(50, self.result.getPercentTwo())

    def test_getLinesMatched(self):
        self.assertEqual(60, self.result.getLinesMatched())

#
# getNameOne()
#
    def test_getNameOne(self):
        self.result = Result(1, "hpotter_Insipid.java", "nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertEqual(self.result.getNameOne(), "hpotter")
        self.assertNotEqual(self.result.getNameOne(), "Insipid.java")

    def test_getNameOnePrevious(self):
        self.result = Result(1, "previous_hpotter_Insipid.java", "previous_nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertEqual(self.result.getNameOne(), "hpotter")
        self.assertNotEqual(self.result.getNameOne(), "previous")

    def test_getNameOneNotTwo(self):
        self.result = Result(1, "previous_hpotter_Insipid.java", "previous_nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertNotEqual(self.result.getNameOne(), "nmarth")

#
# getNameTwo()
#
    def test_getNameTwo(self):
        self.result = Result(1, "hpotter_Insipid.java", "nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertEqual(self.result.getNameTwo(), "nmarth")
        self.assertNotEqual(self.result.getNameTwo(), "Warmup.java")

    def test_getNameTwoPrevious(self):
        self.result = Result(1, "previous_hpotter_Insipid.java", "previous_nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertEqual(self.result.getNameTwo(), "nmarth")
        self.assertNotEqual(self.result.getNameTwo(), "previous")

    def test_getNameTwoNotOne(self):
        self.result = Result(1, "previous_hpotter_Insipid.java", "previous_nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertNotEqual(self.result.getNameTwo(), "hpotter")

#
# getName()
#
    def test_getName(self):
        self.result = Result(1, "hpotter_Insipid.java", "nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertEqual(self.result.getName(self.result.fileTwo), "nmarth")
        self.assertNotEqual(self.result.getName(self.result.fileTwo), "Warmup.java")

    def test_getNameNotPrevious(self):
        self.result = Result(1, "previous_hpotter_Insipid.java", "previous_nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertEqual(self.result.getName(self.result.fileTwo), "nmarth")
        self.assertNotEqual(self.result.getName(self.result.fileTwo), "previous")

#
# getAssignmentName()
#
    # Test two current files
    def test_getAssignmentName(self):
        self.result.fileOne = "hpotter_Insipid.java"
        self.result.fileTwo = "nmarth_Insipid.java"
        self.assertEqual("Insipid.java", self.result.getAssignmentName())

    # Test previous and current files
    def test_getAssignmentNameOnePrevious(self):
        self.result.fileOne = "previous_hpotter_Insipid.java"
        self.result.fileTwo = "nmarth_Insipid.java"
        self.assertEqual("Insipid.java", self.result.getAssignmentName())

    # Test previous and current files reverse
    def test_getAssignmentNameTwoPrevious(self):
        self.result.fileOne = "previous_hpotter_Insipid.java"
        self.result.fileTwo = "nmarth_Insipid.java"
        self.assertEqual("Insipid.java", self.result.getAssignmentName())

    # Test two previous files
    def test_getAssignmentNameBothPrevious(self):
        self.result.fileOne = "previous_hpotter_Insipid.java"
        self.result.fileTwo = "previous_nmarth_Insipid.java"
        self.assertEqual("Insipid.java", self.result.getAssignmentName())

    def test_getAssignmentNameDifferentAssignments(self):
        self.result.fileOne = "hpotter_Warmup.java"
        self.result.fileTwo = "previous_nmarth_Insipid.java"
        self.assertNotEqual("Warmup.java", self.result.getAssignmentName())
        self.assertNotEqual("Insipid.java", self.result.getAssignmentName())

#
# nameOneIsPrevious()
#
    def test_nameOneIsPreviousTrue(self):
        self.result = Result(1, "previous_hpotter_Insipid.java", "nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertTrue(self.result.nameOneIsPrevious())

    def test_nameOneIsPreviousFalse(self):
        self.result = Result(1, "hpotter_Insipid.java", "previous_nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertFalse(self.result.nameOneIsPrevious())

#
# nameTwoIsPrevious()
#
    def test_nameTwoIsPreviousTrue(self):
        self.result = Result(1, "hpotter_Insipid.java", "previous_nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertTrue(self.result.nameTwoIsPrevious())

    def test_nameTwoIsPreviousFalse(self):
        self.result = Result(1, "previous_hpotter_Insipid.java", "nmarth_Warmup.java", "url", 40, 50, 60)
        self.assertFalse(self.result.nameTwoIsPrevious())

#
# isNamePrevious()
#
    # Test previous file name
    def test_isNamePreviousTrue(self):
        self.assertTrue(self.result.isNamePrevious("previous_hpotter_Insipid.java"))

    # Test current file name
    def test_isNamePreviousFalse(self):
        self.assertFalse(self.result.isNamePrevious("hpotter_Insipid.java"))

    # Test incorrect spelling of previous
    def test_isNamePreviousFalseWrongSpelling(self):
        self.assertFalse(self.result.isNamePrevious("pr3vious_test.java"))

    # Test incorrect use of special characters
    def test_isNamePreviousSpecialChars(self):
        self.assertFalse(self.result.isNamePrevious("previ0us_test.java"))
        self.assertFalse(self.result.isNamePrevious("previou$_test2.java"))

    # Test missing '_' in name
    def test_isNamePreviousMissingUnderscore(self):
        self.assertFalse(self.result.isNamePrevious("previoustest.java"))

    # Test dash (does not count as underscore)
    def test_isNamePrevious(self):
        self.result.fileOne = "previous-test.java"
        self.assertFalse(self.result.isNamePrevious("previous-test.java"))

#
# toString()
#
    def test_toString(self):
        self.assertEqual(self.result.toString(), "1" + "\t" + "f1" + "\t" + "f2" +
                         "\t" + "url" + "\t" + "40" + "\t" + "50" + "\t" + "60")

#
# equals()
#

    def test_equalsTrue(self):
        self.assertTrue(self.result.equals(Result(1, "f1", "f2", "url", 40, 50, 60)))

    def test_equalsFalse(self):
        self.assertFalse(self.result.equals(Result(0, "", "", "", 0, 0, 0)))

#
# isValid()
#
    # Test for invalid type of fileOne
    def test_invalidTypeOfFileOne(self):
        self.result.fileOne = 1
        self.assertFalse(self.result.isValid())

    # Test for invalid type of fileTwo
    def test_invalidFileTwo(self):
        self.result.fileTwo = 2
        self.assertFalse(self.result.isValid())

    # Test for invalid type of URL
    def test_invalidTypeOfURL(self):
        self.result.url = 3
        self.assertFalse(self.result.isValid())

    # Test for invalid type of fileOnePercent
    def test_invalidTypeOfFileOnePercent(self):
        self.result.fileOnePercent = "56"
        self.assertFalse(self.result.isValid())

    # Test for invalid type of fileTwoPercent
    def test_invalidTypeOfFileTwoPercent(self):
        self.result.fileTwoPercent = "22"
        self.assertFalse(self.result.isValid())

    # Test for invalid negative for fileOnePercent
    def test_invalidNegativeOnFileOnePercent(self):
        self.result.fileOnePercent = -50
        self.assertFalse(self.result.isValid())

    # Test for invalid negative for fileTwoPercent
    def test_invalidNegativeOnFileTwoPercent(self):
        self.result.fileTwoPercent = -60
        self.assertFalse(self.result.isValid())

    # Test for invalid lines matched string
    def test_invalidTypeOfLinesMatched(self):
        self.result.linesMatched = "17"
        self.assertFalse(self.result.isValid())

    # Test for invalid lines matched int
    def test_invalidNegativeOnLinesMatched(self):
        self.result.linesMatched = -70
        self.assertFalse(self.result.isValid())

    # Test for all is valid
    def test_validTrue(self):
        self.assertTrue(self.result.isValid())

    def test_validateFiles1(self):
        self.assertTrue(self.result.validateFiles())

    def test_validateFiles2(self):
        self.result.fileOne = 23
        self.assertFalse(self.result.validateFiles())

    def test_validateFiles3(self):
        self.result.fileTwo = 201.3
        self.assertFalse(self.result.validateFiles())

    def test_validateFiles4(self):
        self.result.fileOne = True
        self.assertFalse(self.result.validateFiles())

    def test_validatePercents1(self):
        self.assertTrue(self.result.validatePercents())

    def test_validatePercents2(self):
        self.result.fileOnePercent = "not an int"
        self.assertFalse(self.result.validatePercents())

    def test_validatePercents3(self):
        self.result.fileTwoPercent = "not an int"
        self.assertFalse(self.result.validatePercents())

    def test_validatePercents4(self):
        self.result.fileOnePercent = -10
        self.assertFalse(self.result.validatePercents())

    def test_validatePercents5(self):
        self.result.fileTwoPercent = -32
        self.assertFalse(self.result.validatePercents())

    def test_validatePercents6(self):
        self.result.fileOnePercent = 0
        self.assertFalse(self.result.validatePercents())

    def test_validatePercents7(self):
        self.result.fileTwoPercent = 0
        self.assertFalse(self.result.validatePercents())

    def test_validateURL1(self):
        self.assertTrue(self.result.validateURL())

    def test_validateURL2(self):
        self.result.url = 10329
        self.assertFalse(self.result.validateURL())

    def test_validateURL3(self):
        self.result.url = True
        self.assertFalse(self.result.validateURL())

    def test_validateLinesMatched1(self):
        self.assertTrue(self.result.validateLinesMatched())

    def test_validateLinesMatched2(self):
        self.result.linesMatched = "not an int"
        self.assertFalse(self.result.validateLinesMatched())

    def test_validateLinesMatched3(self):
        self.result.linesMatched = -10
        self.assertFalse(self.result.validateLinesMatched())

    def test_validateLinesMatched4(self):
        self.result.linesMatched = 0
        self.assertFalse(self.result.validateLinesMatched())

    def test_validateLinesMatched5(self):
        self.result.linesMatched = False
        self.assertFalse(self.result.validateLinesMatched())

if __name__ == '__main__':
    unittest.main()
