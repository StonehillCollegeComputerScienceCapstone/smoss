#!/usr/bin/env python3.6

#
#   FILE:       TopTenStudentsTest.py
#   AUTHOR:     wgreelish
#   DATE:       9 APR 2018
#
#   DESCRIPTION:   
#   This suite runs all of the UAT's from Story #154706475. 
#

import test.frontend.FrontEndConfig as FrontEndConfig
import Config

class TopTenStudentsTest (FrontEndConfig.FrontEndTestSuite):
    #
    #   setUp ():       Specifies the build name for the test suite
    #
    def setUp (self):
        FrontEndConfig.FrontEndTestSuite.setUp (self)
        self.buildName = "154706475 - Top Ten Students"



    #
    #   ExpiredURLSubmission ():    Enters in an expired URL into the text ara and submits it
    #
    def test_ExpiredURLSubmission (self):
        driver = self.InitializeBrowserStackConnection ("Test an Expired URL")
        
        # Navigate to page
        driver.get ("http://127.0.0.1:5000/")

        # Find textarea and input expired URL
        driver.find_element_by_name ("text").click ()
        driver.find_element_by_name ("text").send_keys ("http://moss.stanford.edu/results/388411051")

        # Submit form data
        driver.find_element_by_xpath ("//input[@value='Submit']").click ()

        # Assertion
        self.assertEqual ("Uh Oh!", driver.find_element_by_xpath("//h1").text)