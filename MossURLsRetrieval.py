import urllib
import urllib.request
import urllib.error
from FileRetrieval import FileRetrieval


class MossURLsRetrieval:
    def __init__(self):
        self.urls = []
        self.file = FileRetrieval()
        # potentially a data variable?

    def get_url(self, url):
        # check to see if it has "moss.stanford.edu"
        # check that it exists (http response of 200?)
        if not isinstance(url, str):
            print(url, "is invalid")
            return False
        if "moss.stanford.edu/results" not in url:  # this can be changed by Stanford at any time
            print(url, "is invalid")
            return False
        if url in self.urls:  # URL already exists in list
            print(url, "is duplicate")
            return False
        try:
            urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:  # case of 404 Not Found
            print(url, e)
            return False
        except urllib.error.URLError as e:  # case connection refused
            print(url, ": ", e)
            return False
        self.urls.append(url)
        return True

    def get_file_urls(self, file):
        if not self.file.open_and_read_file(file):  # FileRetrieval returns if the file is valid
            return False
        for url in self.file.url_list:
            self.get_url(url)  # checks the validity of the URLs given from file
        return True
