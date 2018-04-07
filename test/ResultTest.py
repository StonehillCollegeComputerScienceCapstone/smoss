import unittest
from Result import Result


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.result = Result(1, "f1", "f2", "url", 40, 50, 60)

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

    def test_toString(self):
        self.assertEqual(self.result.toString(), "1" + "\t" + "f1" + "\t" + "f2" +
                         "\t" + "url" + "\t" + "40" + "\t" + "50" + "\t" + "60")

    def test_equalsTrue(self):
        self.assertTrue(self.result.equals(Result(1, "f1", "f2", "url", 40, 50, 60)))

    def test_equalsFalse(self):
        self.assertFalse(self.result.equals(Result(0, "", "", "", 0, 0, 0)))


if __name__ == '__main__':
    unittest.main()
