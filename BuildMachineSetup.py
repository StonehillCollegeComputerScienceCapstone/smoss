#!/usr/bin/env python3.6

#
#   FILE:       BuildMachineSetup.py
#   AUTHOR:     mmiddleton
#   DATE:       25 MAR 2018
#
#   DESCRIPTION:
#   This file was created to run set-up for the build machine. It is NOT meant to be a component
#   of SMOSS' source-code.

import requests
import json
import getpass
import os

# Make the request to the BrowserStack API to get our builds
username = ''
password = ''

if getpass.getuser () == 'mmiddleton'
    username = 'mmiddleton'
    password = 'sjFs7kUux7jvjxbk6Vss'

else:
    username = os.environ['BROWSERSTACK_USER']
    password = os.environ['BROWSERSTACK_ACCESS_KEY']


browserStackBuilds = requests.get ('https://api.browserstack.com/automate/builds.json', auth = (username, password))

if browserStackBuilds.status_code is 200:
    # If the request returns data:
    if browserStackBuilds.json ():
        for build in browserStackBuilds.json ():
            # Grab the build hash
            buildHash = build['automation_build']['hashed_id']

            # Form DELETE URL based on the build hash we just received
            url = 'https://api.browserstack.com/automate/builds/' + buildHash + '.json'

            # Make the request
            deletePreviousData = requests.delete (url, auth = (username, password))


            # Print the output for logging purposes
            print (deletePreviousData.text)

    # We only get here if there is nothing in the returned request data:
    else:
        print ('INFO:\tThere are no builds currently listed online')

else:
    print ('ERROR:\tThere was a problem with the request to the BrowserStack API. Response code is NOT 200!!!')

