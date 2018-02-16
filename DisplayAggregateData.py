

class DisplayAggregateData:
    def __init__(self):
        #initialize information
        self.html = ""
        self.address = "" #address to send to browser

    def set_Address(self, addr):
        if addr is not None: #not null
            self.address = addr

    def formHTML(self):
        #take 'result' objects / aggregate data, form html

        return self.html

    def post(self):
        return True
        #take html and sent to browser


    def print(self):
        return True
        #print to file the aggregate data