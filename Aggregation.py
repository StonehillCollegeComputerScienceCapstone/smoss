from Config import Config

class Aggregation:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.Config = Config()

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def toString(self):
        return self.name + " \t" + str(self.data)
