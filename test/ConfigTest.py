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

    #1. config.getWarmup()
    def test_warmupURLValidity(self):
        c = Config()
        url = c.getWarmup()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False

    #2. config.getTwentyone()
    def test_twentyoneRLValidity(self):
        c = Config()
        url = c.getTwentyone()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False

    #3. config.getWarmup()
    def test_squarerootURLValidity(self):
        c = Config()
        url = c.getSquareroot()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False

    #4. config.getInsipid()
    def test_inspidURLValidity(self):
        c = Config()
        url = c.getInsipid()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False

    #5. config.getRodentia()
    def test_rodentiaURLValidity(self):
        c = Config()
        url = c.getRodentia()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False