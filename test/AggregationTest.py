import unittest
from Aggregation import Aggregation

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.aggregation = Aggregation("name", 0) #(Name, Data)

    def test_getName(self):
        self.assertEqual(self.aggregation.getName(), "name")

    def test_setName(self):
        self.aggregation.setName("newName")
        self.assertEqual(self.aggregation.getName(), "newName")

    def test_getData(self):
        self.assertEqual(self.aggregation.getData(), 0)

    def test_setData(self):
        self.aggregation.setData(100)
        self.assertEqual(self.aggregation.getData(), 100)

    def test_toString(self):
        self.assertEqual(self.aggregation.toString(), "name" + " \t" + str(0))


if __name__ == '__main__':
    unittest.main()
