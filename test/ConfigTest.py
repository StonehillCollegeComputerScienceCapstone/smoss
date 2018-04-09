import unittest
import urllib
import urllib.request
from Config import Config

#-----Methods being tested
#1. config.getWarmup()
#2. config.getTwentyone()
#3. config.getSquareroot()
#4. config.getInsipid()
#5. config.getRodentia()

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.c = Config()
        self.valid = False

    #1. config.getWarmup()
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

    #2. config.getTwentyone()
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

    #3. config.getWarmup()
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

    #4. config.getInsipid()
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

    #5. config.getRodentia()
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