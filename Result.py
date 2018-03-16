class Result:
    def __init__(self, assignmentNum, f1, f2, url, f1Percent, f2Percent, linesMatched):
        self.assignment_number = assignmentNum
        self.file_one = f1
        self.file_two = f2
        self.url = url
        self.file_one_percent = f1Percent
        self.file_two_percent = f2Percent
        self.lines_matched = linesMatched

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
