class Result:
    def __init__(self, assignment_num, f1, f2, url, f1_percent, f2_percent, lines_matched):
        self.assignment_number = assignment_num
        self.file_one = f1
        self.file_two = f2
        self.url = url
        self.file_one_percent = f1_percent
        self.file_two_percent = f2_percent
        self.lines_matched = lines_matched

    def get_assignment_number(self):
        return self.assignment_number()

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

    def get_lines_matched(self):
        return self.lines_matched
