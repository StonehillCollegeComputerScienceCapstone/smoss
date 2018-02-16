class Aggregation:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def to_string(self):
        return self.name + " \t" + str(self.data)
