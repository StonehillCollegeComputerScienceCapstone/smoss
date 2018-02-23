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
import os



# Global Variables
app = Flask(__name__, template_folder=os.path.dirname('./'))
sorter = SortResults ()


#
#   _Index ():     Generates the landing page for SMOSS.
#
@app.route ('/')
def _Index ():
    print ('[BackendServer]\tIndex page displayed!')
    template = 'templates/index.html'
    return render_template (template)




#
#   _MOSSOutput (): Formerly held within SortResults.py, this displays the MOSSoutput template at localhost:5000/moss
#
@app.route ('/moss')
def _MOSSOutput ():
    print ('[BackendServer]\tMOSS Output page displayed!')
    template = "templates/MOSSoutput.html"
    objectList = sorter.get_csv()
    sorter.validateData (objectList)
    return render_template (template, object_list = objectList)


#
#   _ErrorHandler ():   Displays the generic error page with output on the error type
#
@app.errorhandler (403)
@app.errorhandler (404)
def _ErrorHandler (errorCode):
    template = "templates/errorpage.html"
    return render_template (template, errorCode = errorCode)



if __name__ == '__main__':
    app.run(debug = True, use_reloader=True)