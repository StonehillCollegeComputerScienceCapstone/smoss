class config:
    mossURL = "http://moss.stanford.edu/results/558206563"
    def _init_(self):
        self.mossURL = mossURL

    def testURLValidity(self):
        request = urllib.request.Request(self.mossURL)
        try:
            response = urllib.request.urlopen(request)
            return True
        except:
            return False