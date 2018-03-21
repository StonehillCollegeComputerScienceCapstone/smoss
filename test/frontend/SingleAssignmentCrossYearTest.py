#!/usr/bin/env python3.6

#
#   FILE:       SingleAssignmentCrossYearTest.py
#   AUTHOR:     mmiddleton
#   DATE:       16 MAR 2018
#
#   DESCRIPTION:   
#   This suite runs all of the UAT's from Story #154706492. 
#
import test.frontend.FrontEndConfig as FrontEndConfig
import Config

class SingleAssignmentCrossYearTest (FrontEndConfig.FrontEndTestSuite):    
    #  
    #   test_CurrentAndCurrentPairing:  SMOSS will return a list about cheating that compares from the current-current year  
    #  
    def test_CurrentAndCurrentPairing (self):  
        browser = self.InitializeBrowserStackConnection ('Single Assign. X-Year - Current & Current Pairing')  
        url = self.getUrl ()

        # Navigate to the homepage:
        browser.get ('http://localhost:5000/')

        # Target the textarea element and send it one of the Config file's pre-saved URL's
        textSubmission = browser.find_element_by_tag_name ('textarea')
        textSubmission.send_keys (url)
        textSubmission.submit ()

        # NEW PAGE      ->      http://localhost:5000/selectionpage
        
        # Click the expected radio button and click submit button:
        radioButton = browser.find_element_by_css_selector ("input[type='radio'][value='" + url + "']").click ()
        submitButton = browser.find_element_by_css_selector ("input[type='submit']").click ()

        # NEW PAGE      ->      http://localhost:5000/moss

        print ('FrontEndSuite:  This test is INCOMPLETE. It will currently pass if we get to /moss.')

        self.assertEqual (browser.current_url, 'http://localhost:5000/moss')        



    #
    #   getUrl ():      Creates a 
    #
    def getUrl (self):
        temp = Config.Config ()
        return temp.rodentia

'''
TODO:   These are the remaining UAT's for this file:
    SMOSS will return a list about cheating that compares from the current-previous year
    SMOSS will *NOT* return a list about cheating that compares from the previous-previous year.  
    SMOSS will display an error message with the wrong file's name.  
    SMOSS will have sort-able fields for the list of possible cheaters.  
'''