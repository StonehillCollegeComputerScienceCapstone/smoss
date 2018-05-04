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

    # Constructor
    def __init__(self, sessionId):
        self.sessionId = sessionId

    # Sometimes there is an error accessing a valid url. This enables the program to try to access the url multiple
    # times before throwing an error
    def tryDownload(self, url, directory):
        if not isinstance(url, str) or not isinstance(directory, str):
            return False
        i = 0
        urlSuccess = False

        # Try to access the url 5 times
        while i < 5 and (not urlSuccess):
            try:
                wget.download(url, directory)
                urlSuccess = True
            except:
                i = i + 1

        # If the URL was not successful, try one more time and let the exception get thrown automatically
        if not urlSuccess:
            wget.download(url, directory)

    # Given the base URL, download all 4 HTML files that come with an assignment analysis
    def downloadMatch(self, urlBase, mossID):
        if not isinstance(urlBase, str) or not isinstance(mossID, str):
            return False
        dirName = './' + self.sessionId + 'archive/' + mossID
        self.tryDownload(urlBase + '.html', dirName)
        self.tryDownload(urlBase + '-top.html', dirName)
        self.tryDownload(urlBase + '-0.html', dirName)
        self.tryDownload(urlBase + '-1.html', dirName)

    # Given a MOSS ID and the number of matches in the ID, call downloadMatch() on all matches in the submission
    def downloadAllMatchesForAssignment (self, mossID, numberOfMatches):
        if not isinstance(mossID, str) or not isinstance(numberOfMatches, int):
            return False
        for match in range(0, numberOfMatches):
            self.downloadMatch('http://moss.stanford.edu/results/' + mossID + '/' + 'match' + str(match), mossID)

    # Given a 2D array of MOSS ID's and number of matches for the ID, run
    def downloadAllMatches(self, mossIDs, numberOfMatches):
        if not isinstance(mossIDs, list) or not isinstance(numberOfMatches, list):
            return False
        else:
            for assignment in range(0, len(mossIDs)):
                if not isinstance(mossIDs[assignment], str) or not isinstance(numberOfMatches[assignment], int):
                    return False
        self.removeAllTempFiles()
        for assignment in range(0, len(mossIDs)):
            self.downloadSummaryPage(mossIDs[assignment])
            self.downloadAllMatchesForAssignment(mossIDs[assignment], numberOfMatches[assignment])
        self.zipFile()

    # Given MOSS's ID number, it downloads MOSS's index page of all assignment rankings
    def downloadSummaryPage(self, mossID):
        if not isinstance(mossID, str):
            return False
        directory = self.sessionId + 'archive/'
        if os.path.isdir(directory + mossID):
            shutil.rmtree(directory + mossID)
        os.makedirs(directory + mossID)
        self.tryDownload('http://moss.stanford.edu/results/' + mossID, './' + directory + mossID)

        oldName = './' + directory + mossID + '/' + mossID
        newName = oldName + '.html'

        os.rename(oldName, newName)
        with open(newName, 'r') as file:
            original = file.read()
        original = original.replace('http://moss.stanford.edu/results/' + mossID + '/', '')
        with open(newName, 'w') as file:
            file.write(original)

    # Takes away the http:..../results/
    def getAssignmentIds(self, urls):
        if not isinstance(urls, list):
            return False
        else:
            for url in urls:
                if not isinstance(url, str):
                    return False
        adjustedList = []
        for url in urls:
            adjustedList.append(url.replace('http://moss.stanford.edu/results/', ''))
        return adjustedList

    # Creates a .zip of the archive directory
    def zipFile(self):
        zipName = self.sessionId + 'mossURLs'
        directoryName = './' + self.sessionId + 'archive'
        shutil.make_archive(zipName, 'zip', directoryName)

    # Removes mossURLs.zip and the archive directory if either exist
    def removeAllTempFiles(self):
        zipFileName = './' +  self.sessionId + 'mossURLs.zip'
        archiveFileName = './' + self.sessionId + 'archive'
        if os.path.exists(zipFileName):
            os.remove(zipFileName)
        if os.path.isdir(archiveFileName):
            shutil.rmtree(archiveFileName)