#!/usr/bin/env python3.6
#
#   FILE:       MossDownloader.py
#   AUTHOR:     mmiddleton, nlisichenok
#   DATE:       25 APR. 2018
#

import wget

class MossDownloader ():
    #
    #   downloadMatch:   Given the base URL, download all 4 HTML files that come with an assignment analysis
    #
    def downloadMatch (self, urlBase):
        wget.download (urlBase + '.html')
        wget.download (urlBase + '-top.html')
        wget.download (urlBase + '-0.html')
        wget.download (urlBase + '-1.html')



    #
    #   downloadAllMatchesForAssignment:    Given a MOSS ID and the number of matches in the ID, call downloadMatch() on all matches in the submission
    #
    def downloadAllMatchesForAssignment (self, assignmentID, numberOfMatches):
        for match in range (0, numberOfMatches):
            downloadMatch ('http://moss.stanford.edu/results/' + assignmentID + '/' + str (match))



    #
    # downloadAllMatches ():    Given a 2D array of MOSS ID's and number of matches for the ID, run 
    #
    def downloadAllMatches (self, submissions):
        for assignment in submissions:
            downloadAllMatchesForAssignment (assignment[0], assignment[1])



# NOTE: We are currently missing the following functionalities/components to the story:
'''
    - We need an INDEX.HTML page that will show all of the results that we have.
      (Maybe we can modify MOSSoutput.html in /templates?)
    
    - We need to compress all of these to a single, downloadable file.
        > Make subdirectory
        > 'CD' into subdirectory
        > Create INDEX.HTML
        > Create a 'submissions' array using the MOSSretriever data
        > downloadAllMatches (submissions_array)
        > 'CD' ..
        > zip/tar the subdirectory

    - We need to add a download button to the MOSSoutput template that will call the BackendServer connection to this.

    - We need to make a BackendServer connection to all of this
'''