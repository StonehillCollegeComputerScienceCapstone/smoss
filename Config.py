import logging
class Config:

    #Assignments-------------------------------------->
    warmup = "http://moss.stanford.edu/results/860369009"
    twentyone = "http://moss.stanford.edu/results/28359173"
    squareroot = "http://moss.stanford.edu/results/957841265"
    insipid = "http://moss.stanford.edu/results/467757133"
    rodentia = "http://moss.stanford.edu/results/212658218"

    #Logger Setup------------------------------------->
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
    logging.basicConfig(filename='output.log', format=FORMAT)

    #Constructor------------------------------------->
    def __init__(self):
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

