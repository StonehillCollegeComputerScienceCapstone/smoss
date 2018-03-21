import urllib
import urllib.request
import logging
class Config:

    #Assignments-------------------------------------->

    #1. Warmup.java
    warmup = "http://moss.stanford.edu/results/934408726"

    #2. TwentyOne.java
    twentyone = "http://moss.stanford.edu/results/752446360"

    #3. SquareRoot.java
    squareroot = "http://moss.stanford.edu/results/686270206"

    #4. Insipid.java
    insipid = "http://moss.stanford.edu/results/348481084"

    #5. Rodentia.java
    rodentia = "http://moss.stanford.edu/results/80427955"

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

