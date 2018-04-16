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
# getNameOne()
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


if __name__ == '__main__':
    unittest.main()
