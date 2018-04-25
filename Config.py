import logging
class Config:

    mossUrlsFile = './test/mossUrls.txt'
    file = open(mossUrlsFile, 'r').read()
    lines = file.split('\n')

    #Assignments-------------------------------------->
    magicsquare = lines[0]
    palindrome = lines[1]
    twentyone = lines[2]
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

    def getMagicsquare(self):
        return self.magicsquare

    def getTwentyone(self):
        return self.twentyone

    def getPalindrome(self):
        return self.palindrome

