#!/usr/bin/env python3.6

#
#   FILE:   BackendServer.py
#   AUTHOR: mmiddleton
#   DATE:   19 FEB 2018
#
#   DESCRIPTION:
#   This file comprises the code that runs the Flask server for our MOSS solution.
#

from flask import *
from ResultsSorter import ResultsSorter
from DataAggregator import DataAggregator
from MossResultsRetriever import MossResultsRetriever
from Graph import Graph
import os
import logging
from Config import Config



# Global Variables
app = Flask(__name__, template_folder=os.path.dirname('./'))
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
logging.basicConfig(filename='output.log', format=FORMAT)
logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)

sorter = ResultsSorter()
aggregator = DataAggregator()
retriever = MossResultsRetriever()

#
#   _Index ():     Generates the landing page for SMOSS.
#
@app.route ('/', methods = ['GET', 'POST'])
def _Index ():
    logger.info('[BackendServer]\tIndex page displayed!')
    if request.method == "POST":
        inputURLs = request.form['text'] #input from the user
        retriever.urls = inputURLs.split("\n")

        valid, url = isValidUrlList(retriever.urls)
        if not valid:
            template = "templates/errorpage.html"
            error = ("Invalid URL: "+ url)
            return render_template(template, value=error)
        else:
            return redirect('selectionpage')

    template = "templates/index.html"
    return render_template (template)

@app.route('/selectionpage',  methods = ['GET', 'POST'])
def _MOSSselectpage():

    logger.info('[BackendServer]\tMOSS Selection page displayed!')
    template = "templates/SelectionPage.html"

    if request.method == "POST":
        selection = request.form['selection']

        if (selection == "allURLs"):
            for i in (0, len(retriever.urls)-1):
                retriever.urls[i] = retriever.urls[i].rstrip()
        else:
            retriever.reInit()  # Clear the retriever
            retriever.urls.append(selection)

        retriever.getResults()
        # If the results are empty
        if not retriever.results:
            template = "templates/errorpage.html"
            value = "Invalid File Name"
            return render_template(template, value=value)

        aggregator.reInit(retriever.results)
        return redirect('moss')
    duplicateValues, urlList = getDuplicateUrls(retriever.urls)
    return render_template(template, urlList=urlList, duplicateValues=duplicateValues)

#
#   _MOSSOutput (): Formerly held within ResultsSorter.py
# , this displays the MOSSoutput template at localhost:5000/moss
#
@app.route ('/moss')
def _MOSSOutput ():
    logger.info('[BackendServer]\tMOSS Output page displayed!')
    template, value = getMossTemplate()
    percentsValues = getAggregateLinesTemplate()
    linesValues = getAggregatePercentTemplate()
    results = retriever.results

    graph = Graph(results)
    graphJson = graph.getJsonObject(results)
    nodes = graphJson["nodes"]
    edges = graphJson["edges"]
    return render_template(template, value=value, percentsValues=percentsValues, linesValues=linesValues, nodes=nodes, edges=edges)


@app.route('/URLvalidation')
def _MOSSurlvalidation():
    logger.info('[BackendServer]\tMOSS URL validation page displayed!')
    template, value = getMossTemplate()
    return render_template(template, value=value)


def getDuplicateUrls(urlList):
    nonDuplicates = set()
    duplicates=set()
    for url in urlList:
        if url.rstrip() not in nonDuplicates:
            nonDuplicates.add(url.rstrip())
        else:
            duplicates.add(url.rstrip())

    return duplicates, nonDuplicates


def isValidUrlList(urlList):
    valid, url = retriever.getValidity(urlList)
    if not valid:
        return False, url
    else:
        return True, url


def getMossTemplate():
    if not(sorter.validateData()):
        template = "templates/errorpage.html"
        value = "Invalid File Data"
    else:
        template = "templates/MOSSoutput.html"
        value = sorter.get_csv()
    return template, value


def getAggregatePercentTemplate():
    percentsValues = aggregator.top_percents
    return percentsValues


def getAggregateLinesTemplate():
    linesValues = aggregator.top_lines
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
