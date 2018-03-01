import os.path
# from tkinter.filedialog import askopenfile


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

#    def pop_up_open_file(self):  # built-in pop up for python that we can consider using in the future of this project
#        name = askopenfile()
#        if name is None:
#            return False
#        return True
