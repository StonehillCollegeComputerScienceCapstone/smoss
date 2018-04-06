import os.path
from Config import Config

class FileRetrieval:
    def __init__(self):
        self.file_name = None
        self.url_list = []

    def open_and_read_file(self, file):
        if not isinstance(file, str):
            return False
        dir_path = os.path.dirname(os.path.realpath(__file__))  # get the systems path when running this code
        lines = os.path.join(dir_path, file)
        try:
            opening_file = open(lines, "r")
        except FileNotFoundError as e:
            print(e)
            return False
        for url in opening_file:
            self.url_list.extend(url.splitlines())
        opening_file.close()
        self.file_name = file
        return True

