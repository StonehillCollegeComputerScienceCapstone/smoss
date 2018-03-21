import urllib
import urllib.request
import logging
class Config:

    #These should be valid URL's for each assignment in the 'current_year_data' folder
    homevalue = "http://moss.stanford.edu/results/558206563"
    golbach = "http://moss.stanford.edu/results/886377605"
    palindrome = "http://moss.stanford.edu/results/674631558"
    carnivalgame = "http://moss.stanford.edu/results/411107744"
    warmup = "http://moss.stanford.edu/results/628475676"

    #Logger Setup
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
    logging.basicConfig(filename='output.log', format=FORMAT)

    def _init_(self):
        self.homevalue = homevalue
        self.golbach = golbach
        self.palindrome = palindrome
        self.carnivalgame = carnivalgame
        self.warmup = warmup
        logger = logging.getLogger('root')
        logger.setLevel(logging.DEBUG)
        self.logger = logger


    def getHomevalue(self):
        return self.homevalue
    def getGolbach(self):
        return self.golbach
    def getPalindrome(self):
        return self.palindrome
    def getCarnivalgame(self):
        return self.carnivalgame
    def getWarmup(self):
        return self.warmup

