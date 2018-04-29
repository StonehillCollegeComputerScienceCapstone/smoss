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
from DataAggregator import DataAggregator
from MossResultsRetriever import MossResultsRetriever
from Graph import Graph
import os
from Config import Config
from MossDownloader import MossDownloader
from MossParser import MossParser

# Global Variables
app = Flask(__name__, template_folder=os.path.dirname('./'))
config = Config()
logger = config.logger
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"

# Try to retriever retriever session variable
def getRetrieverSession():
    try:
        retriever = decode(session['retriever'])
    except:
        logger.info("Session variable 'retriever' does not exist!")
        retriever = MossResultsRetriever()
    return retriever

# Try to retrieve urls session variable
def getUrlsSession():
    try:
        urls = decode(session['urls'])
    except:
        logger.info("Session variable 'urls' does not exist!")
        urls = []
    return urls

#
#   _Index (): Generates the landing page for SMOSS.
#
@app.route ('/', methods = ['GET', 'POST'])
def _Index ():
    logger.info('[BackendServer]\tIndex page displayed!')

    retriever = MossResultsRetriever()

    if request.method == "POST":
        inputURLs = request.form['text'] # Get input from the user
        urls = inputURLs.split("\n")
        for i in range(len(urls)):
            urls[i] = urls[i].rstrip()
        urls = list(filter(None, urls))

        valid, url = retriever.isValidUrlList(urls)

        if valid:
            if 'download' in request.form:
                parser = MossParser()
                downloader = MossDownloader()
                assignmentIds = downloader.getAssignmentIds(urls)
                downloader.downloadAllMatches(assignmentIds, parser.getSizeOfTables(urls))
                return send_from_directory(directory='./', filename='mossURLs.zip', as_attachment=True)
            else:
                session['urls'] = encode(urls)
                return redirect('selectionpage')
        else:
            template = "templates/errorpage.html"
            error = ("Invalid URL: "+ url)
            return render_template(template, value=error)

    template = "templates/index.html"
    return render_template (template)

#
#   _MOSSselectpage(): Generates the page to select which MOSS URL to analyze
#
@app.route('/selectionpage',  methods = ['GET', 'POST'])
def _MOSSselectpage():

    logger.info('[BackendServer]\tMOSS Selection page displayed!')
    template = "templates/SelectionPage.html"

    retriever = MossResultsRetriever()
    urls = getUrlsSession()

    MossDownloader.removeAllTempFiles()

    if request.method == "POST":
        selection = request.form['selection']

        if (selection == "allURLs"):
            for url in urls:
                retriever.appendUrl(url)
        else:
            retriever.appendUrl(selection)

        retriever.populateResults()

        # If the results are empty
        if not retriever.results:
            template = "templates/errorpage.html"
            value = "Invalid File Name"
            return render_template(template, value=value)

        session['retriever'] = encode(retriever)
        return redirect('moss')

    duplicateValues, urlList = retriever.getDuplicateUrls(urls)
    session['retriever'] = encode(retriever)

    return render_template(template, urlList=urlList, duplicateValues=duplicateValues)

#
#   _MOSSOutput (): Formerly held within ResultsSorter.py
# , this displays the MOSSoutput template at localhost:5000/moss
#
@app.route ('/moss', methods = ['GET', 'POST'])
def _MOSSOutput ():
    logger.info('[BackendServer]\tMOSS Output page displayed!')

    retriever = getRetrieverSession()
    template, value = getMossTemplate(retriever)
    aggregator = DataAggregator(retriever.results)
    graph = Graph(retriever.results)
    MossDownloader.removeAllTempFiles()

    if request.method == "POST":
        downloader = MossDownloader()
        assignmentIds = downloader.getAssignmentIds(retriever.urls)
        downloader.downloadAllMatches(assignmentIds, retriever.urlsTableRowsSize)
        return send_from_directory(directory='./', filename='mossURLs.zip', as_attachment=True)

    return render_template(template, value=value, percentsValues=aggregator.topPercents, linesValues=aggregator.topLines,
                           nodes=graph.graph["nodes"], edges=graph.graph["edges"])

#
#   _MOSSurlvalidation(): Validates the URLs
#
@app.route('/URLvalidation')
def _MOSSurlvalidation():
    try:
        retriever = decode(session['retriever'])
    except:
        logger.info('Session variable does not exist!')
        retriever = MossResultsRetriever()

    logger.info('[BackendServer]\tMOSS URL validation page displayed!')
    template, value = getMossTemplate(retriever)
    return render_template(template, value=value)

#
#  getMossTemplate(): Returns the MOSS template if valid
#
def getMossTemplate(retriever):
    if retriever.resultsAreValid():
        template = "templates/MOSSoutput.html"
        value = retriever.results
    else:
        template = "templates/errorpage.html"
        value = "Invalid File Data"
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
