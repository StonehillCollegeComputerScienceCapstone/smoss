import urllib
import urllib.request
import logging
class Config:

    #Assignments-------------------------------------->

    #1. Warmup.java
    warmup = "http://moss.stanford.edu/results/860369009"

    #2. TwentyOne.java
    twentyone = "http://moss.stanford.edu/results/28359173"

    #3. SquareRoot.java
    squareroot = "http://moss.stanford.edu/results/957841265"

    #4. Insipid.java
    insipid = "http://moss.stanford.edu/results/467757133"

    #5. Rodentia.java
    rodentia = "http://moss.stanford.edu/results/212658218"

    #Logger Setup------------------------------------->

    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
    logging.basicConfig(filename='output.log', format=FORMAT)

    #Constructor------------------------------------->

    def _init_(self):
        logger = logging.getLogger('root')
        logger.setLevel(logging.DEBUG)
        self.logger = logger


    #Methods-------------------------------------------->

    def getWarmup(self):
        return self.warmup

    def getTwentyone(self):
        return self.twentyone

    def getSquareroot(self):
        return self.squareroot

    def getInsipid(self):
        return self.insipid

    def getRodentia(self):
        return self.rodentia

