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
from flask_session import Session
from jsonpickle import encode, decode
from ResultsSorter import ResultsSorter
from DataAggregator import DataAggregator
from MossResultsRetriever import MossResultsRetriever
from Graph import Graph
import os
from Config import Config

# Global Variables
app = Flask(__name__, template_folder=os.path.dirname('./'))
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
config = Config()
logger = config.logger

#
#   _Index (): Generates the landing page for SMOSS.
#
@app.route ('/', methods = ['GET', 'POST'])
def _Index ():
    logger.info('[BackendServer]\tIndex page displayed!')

    retriever = MossResultsRetriever()

    if request.method == "POST":
        inputURLs = request.form['text'] #input from the user
        retriever.urls = inputURLs.split("\n")
        session['retriever'] = encode(retriever)

        valid, url = isValidUrlList(retriever)
        if not valid:
            template = "templates/errorpage.html"
            error = ("Invalid URL: "+ url)
            return render_template(template, value=error)
        else:
            return redirect('selectionpage')

    template = "templates/index.html"
    return render_template (template)

#
#   _MOSSselectpage(): Generates the page to select which MOSS URL to analyze
#
@app.route('/selectionpage',  methods = ['GET', 'POST'])
def _MOSSselectpage():

    logger.info('[BackendServer]\tMOSS Selection page displayed!')
    template = "templates/SelectionPage.html"

    retriever = decode(session['retriever'])

    if request.method == "POST":
        selection = request.form['selection']

        if (selection == "allURLs"):
            for i in (0, len(retriever.urls)-1):
                retriever.urls[i] = retriever.urls[i].rstrip()
        else:
            retriever = MossResultsRetriever() # Clear the retriever
            retriever.urls.append(selection)

        retriever.getResults()
        # If the results are empty
        if not retriever.results:
            template = "templates/errorpage.html"
            value = "Invalid File Name"
            return render_template(template, value=value)

        aggregator = DataAggregator(retriever.results)
        session['retriever'] = encode(retriever)
        session['aggregator'] = encode(aggregator)

        return redirect('moss')

    duplicateValues, urlList = getDuplicateUrls(retriever.urls)
    session['retriever'] = encode(retriever)

    return render_template(template, urlList=urlList, duplicateValues=duplicateValues)

#
#   _MOSSOutput (): Formerly held within ResultsSorter.py
# , this displays the MOSSoutput template at localhost:5000/moss
#
@app.route ('/moss')
def _MOSSOutput ():
    logger.info('[BackendServer]\tMOSS Output page displayed!')

    retriever = decode(session['retriever'])
    aggregator = decode(session['aggregator'])

    template, value = getMossTemplate()
    percentsValues = aggregator.topPercents
    linesValues = aggregator.topLines
    results = retriever.results

    graph = Graph(results)
    graphJson = graph.getJsonObject(results)
    nodes = graphJson["nodes"]
    edges = graphJson["edges"]
    return render_template(template, value=value, percentsValues=percentsValues, linesValues=linesValues, nodes=nodes, edges=edges)

#
#   _MOSSurlvalidation(): Validates the URLs
#
@app.route('/URLvalidation')
def _MOSSurlvalidation():
    logger.info('[BackendServer]\tMOSS URL validation page displayed!')
    template, value = getMossTemplate()
    return render_template(template, value=value)

#
#  getDuplicateUrls(urlList): Returns the duplicate and nonduplicate URLs
#
def getDuplicateUrls(urlList):
    nonDuplicates = set()
    duplicates=set()
    for url in urlList:
        if url.rstrip() not in nonDuplicates:
            nonDuplicates.add(url.rstrip())
        else:
            duplicates.add(url.rstrip())

    return duplicates, nonDuplicates

#
#  isValidUrlList(retriever): Returns true if the URLs are valid, else false
#
def isValidUrlList(retriever):
    valid, url = retriever.getValidity(retriever.urls)
    if not valid:
        return False, url
    else:
        return True, url

#
#  getMossTemplate(): Returns the MOSS template if valid
#
def getMossTemplate():
    sorter = ResultsSorter()
    if not(sorter.validateData()):
        template = "templates/errorpage.html"
        value = "Invalid File Data"
    else:
        template = "templates/MOSSoutput.html"
        value = sorter.get_csv()
    return template, value

#
#   _ErrorHandler ():   Displays the generic error page with output on the error type
#
@app.errorhandler (403)
@app.errorhandler (404)
def _ErrorHandler (errorCode):
    template = "templates/errorpage.html"
    return render_template (template, value = errorCode)

#
#   Main
#
if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)
    app.run(debug = True, use_reloader=True)
