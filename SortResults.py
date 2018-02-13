class SortResults:

    def __init__(self):
        self.fileName = "MOSSinput.csv"

    def isValidFilename(self):
        self.fileName = self.fileName.lower()
        if self.fileName.endswith('.csv'):
            return True
        return False
