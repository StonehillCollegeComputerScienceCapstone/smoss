import unittest
import urllib
import urllib.request
from config import config

#-----Methods being tested
#1. config.getHomeValue()
#2. config.getPalindrome()
#3. config.getWarmup()
#4. config.getCarnivalgame()
#5. config.getHomevalue()

class MyTestCase(unittest.TestCase):

    #1. config.getHomeValue()
    def test_homevalueURLValidity(self):
        c = config()
        url = c.getHomevalue()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False

    #2. config.getPalindrome()
    def test_palindromeURLValidity(self):
        c = config()
        url = c.getPalindrome()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False

    #3. config.getWarmup()
    def test_warmupURLValidity(self):
        c = config()
        url = c.getWarmup()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False

    #4. config.getCarnivalgame()
    def test_carnivalgameURLValidity(self):
        c = config()
        url = c.getCarnivalgame()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False

    #5. config.getHomevalue()
    def test_golbachURLValidity(self):
        c = config()
        url = c.getGolbach()
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False