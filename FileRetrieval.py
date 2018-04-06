import os.path
from Config import Config

class FileRetrieval:
    def __init__(self):
        self.fileName = None
        self.urlList = []

    def readFile(self, file):
        if not isinstance(file, str):
            return False

        path = os.path.dirname(os.path.realpath(__file__))  # get the systems path when running this code
        lines = os.path.join(path, file)

        try:
            openingFile = open(lines, "r")
        except FileNotFoundError as e:
            print(e)
            return False

        for url in openingFile:
            self.urlList.extend(url.splitlines())

        openingFile.close()
        self.fileName = file
        return True

