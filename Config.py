import logging
class Config:

    mossUrlsFile = 'mossUrls.txt'
    file = open(mossUrlsFile, 'r').read()
    lines = file.split('\n')

    #Assignments-------------------------------------->
    warmup = lines[0]
    twentyone = lines[1]
    squareroot = lines[2]
    insipid = lines[3]
    rodentia = lines[4]

    #Logger Setup------------------------------------->
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
    logging.basicConfig(filename='output.log', format=FORMAT)

    #Constructor------------------------------------->
    def __init__(self):
        logger = logging.getLogger('root')
        logger.setLevel(logging.DEBUG)
        self.logger = logger


    #Methods-------------------------------------------->

    def getMossUrlsFile(self):
        return self.mossUrlsFile

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

