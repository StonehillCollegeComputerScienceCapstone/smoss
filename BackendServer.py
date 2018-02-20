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



@app.route ('/')
def _Index ():
    print ('[BackendServer]\tIndex page displayed!')
    template = 'templates/index.html'
    return render_template (template)




#
#   _MOSSOutput (): Formerly held within SortResults.py, this displays the MOSSoutput template at localhost:5000/moss
#
@app.route ('/moss')
def _MOSSOutput():
    print ('[BackendServer]\tMOSS Output page displayed!')
    template = "templates/MOSSoutput.html"
    object_list = sorter.get_csv()
    return render_template(template, object_list=object_list)



if __name__ == '__main__':
    app.run(debug = True, use_reloader=True)