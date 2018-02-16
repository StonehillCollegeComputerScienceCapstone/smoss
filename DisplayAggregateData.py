

class DisplayAggregateData:
    def __init__(self):
        #initialize information
        self.html = ""
        self.address = "" #address to send to browser

    def set_Address(self, addr):
        if addr is not None: #not null
            self.address = addr
            return True
        else:
            return False

    def formHTML(self, object):
        #take 'result' objects / aggregate data, form html
        self.html = object
        return True

    def post(self):
        return True
        #take html and sent to browser


    def print_to_file(self, file_name):
        file = open(file_name, "w")
        file.write(self.html)
        file.close()
        return True
        #print to file the aggregate data