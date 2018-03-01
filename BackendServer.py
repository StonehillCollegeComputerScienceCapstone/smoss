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
from MossParser import MossParser
import os


class BackendServer ():
    # Public Variables
    app = Flask(__name__, template_folder=os.path.dirname('./'))
    sorter = SortResults ()
    mossURLSetrieval = MossURLsRetrieval()
    mossURLSetrieval.get_file_urls("FileInput.txt")
    mossURLSetrieval.get_results()
    aggregate = AggregateData(mossURLSetrieval.results)
    urlRetrieval = MossURLsRetrieval()
    parser = MossParser("csv.csv")
    
    #
    #   _Index ():     Generates the landing page for SMOSS.
    #
    @app.route ('/', methods = ['GET', 'POST'])
    def _Index ():
        BackendServer.urlRetrieval.urls=[]

        if request.method == "POST":
            url = request.form['text'] #input from the user
            if not(getValidorInvalidURL(url)):
                template = "templates/errorpage.html"
                error = ("Invalid URL: "+url)
                return render_template(template, value=error)
            else:
                parser.parse(url)
                return redirect('/moss')

        template = "templates/index.html"
        return render_template (template)


    #
    #   _MOSSOutput (): Formerly held within SortResults.py, this displays the MOSSoutput template at localhost:5000/moss
    #
    @app.route ('/moss')
    def _MOSSOutput ():
        template, value = BackendServer.getValidorInvalidMossTemplate()
        percentsValues = BackendServer.getValidorInvalidAggregateLinesTemplate()
        linesValues = BackendServer.getValidorInvalidAggregatePercentTemplate()
        return render_template(template, value = value,percentsValues=percentsValues, linesValues=linesValues),

    @app.route('/URLvalidation')
    def _MOSSurlvalidation():
        template, value = BackendServer.getValidorInvalidURL()
        return render_template(template, value=value)

    def getValidorInvalidURL(urlName):
        valid = BackendServer.urlRetrieval.get_url(urlName)
        if not(valid):
            return False
        else:
            return True

    def getValidorInvalidMossTemplate():
        if not(BackendServer.sorter.validateData()):
            template = "templates/errorpage.html"
            value = "Invalid File Data"
        else:
            template = "templates/MOSSoutput.html"
            value = BackendServer.sorter.get_csv()
        return template, value

    def getValidorInvalidAggregatePercentTemplate():
        percentsValues = BackendServer.aggregate.top_percents
        return percentsValues

    def getValidorInvalidAggregateLinesTemplate():
        linesValues = BackendServer.aggregate.top_lines
        return linesValues

    #
    #   _ErrorHandler ():   Displays the generic error page with output on the error type
    #
    @app.errorhandler (403)
    @app.errorhandler (404)
    @app.errorhandler (500)
    def _ErrorHandler (errorCode):
        template = "templates/errorpage.html"
        return render_template (template, value = errorCode)


if __name__ == '__main__':
    BackendServer.app.run(debug = True, use_reloader=True)