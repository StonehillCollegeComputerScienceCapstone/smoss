#!/usr/bin/python

#
#   FILE:   BackendServer.py
#   AUTHOR: mmiddleton
#   DATE:   19 FEB 2018
#
#   DESCRIPTION:
#   This file comprises the code that runs the Flask server for our MOSS solution.
#

from flask import *
from SortResults import SortResults
from AggregateData import AggregateData
from MossURLsRetrieval import MossURLsRetrieval
from FileRetrieval import FileRetrieval
import os
import cgi, cgitb



# Global Variables
app = Flask(__name__, template_folder=os.path.dirname('./'))
sorter = SortResults ()
mossURLSetrieval = MossURLsRetrieval()
mossURLSetrieval.get_file_urls("FileInput.txt")
mossURLSetrieval.get_results()
aggregate = AggregateData(mossURLSetrieval.results)
urlRetrieval = MossURLsRetrieval()

#
#   _Index ():     Generates the landing page for SMOSS.
#
@app.route ('/')
def _Index ():
    print('[BackendServer]\tIndex page displayed!')
    template = "templates/index.html"
    return render_template (template)


#
#   _MOSSOutput (): Formerly held within SortResults.py, this displays the MOSSoutput template at localhost:5000/moss
#
@app.route ('/moss')
def _MOSSOutput ():
    print('[BackendServer]\tMOSS Output page displayed!')
    template, value = getValidorInvalidMossTemplate()
    percentsValues = getValidorInvalidAggregateLinesTemplate()
    linesValues = getValidorInvalidAggregatePercentTemplate()
    return render_template(template, value = value,percentsValues=percentsValues, linesValues=linesValues),

@app.route('/URLvalidation')
def _MOSSurlvalidation():
    print('[BackendServer]\tMOSS URL validation page displayed!')
    template, value = getValidorInvalidURL()
    return render_template(template, value=value)

def getValidorInvalidURL():
    valid, url = urlRetrieval.getValidity("FileInput.txt")
    if not(valid):
        template = "templates/errorpage.html"
        value = ("Invalid URL: " + url)
    else:
        template = 'templates/invalidURL.html'
        value = "URL is Valid"
    return template, value



def getValidorInvalidMossTemplate():
    if not(sorter.validateData()):
        template = "templates/errorpage.html"
        value = "Invalid File Data"
    else:
        template = "templates/MOSSoutput.html"
        value = sorter.get_csv()
    return template, value

def getValidorInvalidAggregatePercentTemplate():
    percentsValues = aggregate.top_percents
    return percentsValues

def getValidorInvalidAggregateLinesTemplate():
    linesValues = aggregate.top_lines
    return linesValues

#
#   _ErrorHandler ():   Displays the generic error page with output on the error type
#
@app.errorhandler (403)
@app.errorhandler (404)
def _ErrorHandler (errorCode):
    template = "templates/errorpage.html"
    return render_template (template, value = errorCode)



if __name__ == '__main__':
    app.run(debug = True, use_reloader=True)