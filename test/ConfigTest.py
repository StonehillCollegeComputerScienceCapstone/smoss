import unittest
import urllib
import urllib.request
from Config import Config

#-----Methods being tested
# getMoss
# getWarmup()
# getTwentyone()
# getSquareroot()
# getInsipid()
# getRodentia()

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.c = Config()
        self.valid = False

    # getMossUrlsFile()
    def test_getMossUrlsFile(self):
        name = "new file name"
        self.c.mossUrlsFile = name
        self.assertEqual(self.c.getMossUrlsFile(), name)

    # getWarmup()
    def test_warmupURLValidity(self):
        self.valid = False
        url = self.c.getWarmup()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            self.valid = True
        except:
            self.valid = False
        self.assertTrue(self.valid)

    # getTwentyone()
    def test_twentyoneURLValidity(self):
        self.valid = False
        url = self.c.getTwentyone()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            self.valid = True
        except:
            self.valid = False
        self.assertTrue(self.valid)

    # getWarmup()
    def test_squarerootURLValidity(self):
        self.valid = False
        url = self.c.getSquareroot()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            self.valid = True
        except:
            self.valid = False
        self.assertTrue(self.valid)

    # getInsipid()
    def test_inspidURLValidity(self):
        self.valid = False
        url = self.c.getInsipid()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            self.valid = True
        except:
            self.valid = False
        self.assertTrue(self.valid)

    # getRodentia()
    def test_rodentiaURLValidity(self):
        self.valid = False
        url = self.c.getRodentia()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            self.valid = True
        except:
            self.valid = False
        self.assertTrue(self.valid)