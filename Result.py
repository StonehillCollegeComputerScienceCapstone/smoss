class Result:
    def __init__(self, f1, f2, url, f1_percent, f2_percent):
        self.file_one = f1
        self.file_two = f2
        self.url = url
        self.file_one_percent = f1_percent
        self.file_two_percent = f2_percent

    def get_file_one(self):
        return self.file_one

    def get_file_two(self):
        return self.file_two

    def get_url(self):
        return self.url

    def get_percent_one(self):
        return self.file_one_percent

    def get_percent_two(self):
        return self.file_two_percent
