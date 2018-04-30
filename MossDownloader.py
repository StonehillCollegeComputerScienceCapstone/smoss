#!/usr/bin/env python3.6
#
#   FILE:       MossDownloader.py
#   AUTHOR:     mmiddleton, nlisichenok
#   DATE:       25 APR. 2018
#

import wget
import os
import shutil
from MossResultsRetriever import MossResultsRetriever

class MossDownloader ():

    # Given the base URL, download all 4 HTML files that come with an assignment analysis
    def downloadMatch(self, urlBase, mossID):
        wget.download(urlBase + '.html', './archive/' + mossID)
        wget.download(urlBase + '-top.html', './archive/' + mossID)
        wget.download(urlBase + '-0.html', './archive/' + mossID)
        wget.download(urlBase + '-1.html', './archive/' + mossID)

    # Given a MOSS ID and the number of matches in the ID, call downloadMatch() on all matches in the submission
    def downloadAllMatchesForAssignment (self, mossID, numberOfMatches):
        for match in range(0, numberOfMatches):
            self.downloadMatch('http://moss.stanford.edu/results/' + mossID + '/' + 'match' + str(match), mossID)

    # Given a 2D array of MOSS ID's and number of matches for the ID, run
    def downloadAllMatches(self, mossIDs, numberOfMatches):
        self.removeAllTempFiles()
        mossRetriever = MossResultsRetriever()
        for id in mossIDs:
            if not mossRetriever.isValidUrl('http://moss.stanford.edu/results/' + id):
                return False
        for assignment in range(0, len(mossIDs)):
            self.downloadSummaryPage(mossIDs[assignment])
            self.downloadAllMatchesForAssignment(mossIDs[assignment], numberOfMatches[assignment])
        self.zipFile()

    # Given MOSS's ID number, it downloads MOSS's index page of all assignment rankings
    def downloadSummaryPage(self, mossID):
        if os.path.isdir('archive/' + mossID):
            shutil.rmtree('archive/' + mossID)
        os.makedirs('archive/' + mossID)
        wget.download('http://moss.stanford.edu/results/' + mossID, './archive/' + mossID)
        os.rename('./archive/' + mossID + '/' + mossID, './archive/' + mossID + '/' + mossID + '.html')
        with open('./archive/' + mossID + '/' + mossID + '.html', 'r') as file:
            original = file.read()
        original = original.replace('http://moss.stanford.edu/results/' + mossID + '/', '')
        with open('./archive/' + mossID + '/' + mossID + '.html', 'w') as file:
            file.write(original)

    # Takes away the http:..../results/
    def getAssignmentIds(self, urls):
        adjustedList = []
        for url in urls:
            adjustedList.append(url.replace('http://moss.stanford.edu/results/', ''))
        return adjustedList

    # Creates a .zip of the archive directory
    def zipFile(self):
        zipName = 'mossURLs'
        directoryName = './archive'
        shutil.make_archive(zipName, 'zip', directoryName)

    # Removes mossURLs.zip and the archive directory if either exist
    @staticmethod
    def removeAllTempFiles():
        if os.path.exists('./mossURLs.zip'):
            os.remove('./mossURLs.zip')
        if os.path.isdir('./archive'):
            shutil.rmtree('./archive')