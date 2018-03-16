#!/usr/bin/env python3.6

#
#   FILE:       FrontEndConfig.py
#   AUTHOR:     mmiddleton
#   DATE:       16 MAR. 2018
#
#   DESCRIPTION:
#   This file will be included in all FrontEnd test classes.
#

#
#   Returns a static dictionary with the proper BrowserStack syntax 
#
def InitializeBrowserStackConnection (self, testName):
    return {
        'os' : 'Windows',
        'os_version' : '10',
        'browserstack.timezone' : 'UTC-05:00',
        'browserstack.selenium_version' : '3.5.2',  
        'browser' : 'Chrome',
        'browser_version' : '64.0',
        'project' : 'SMOSS',
        'browserstack.local' : 'true',
        'name' : testName,
    }