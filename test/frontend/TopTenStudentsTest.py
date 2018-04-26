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
        driver.get ("http://localhost:5000/")

        # Find textarea and input expired URL
        driver.find_element_by_name ("text").click ()
        driver.find_element_by_name ("text").send_keys ("http://moss.stanford.edu/results/388411051")

        # Submit form data
        driver.find_element_by_xpath ("//input[@value='Submit']").click ()

        # Assertion
        self.assertEqual ("Uh Oh!", driver.find_element_by_xpath("//h1").text)



    #
    #   InvalidURLSubmission ():    Enters in an expired URL into the text ara and submits it
    #
    def test_InvalidURLSubmission (self):
        driver = self.InitializeBrowserStackConnection ("Test an Invalid URL")
        
        # Navigate to page
        driver.get ("http://localhost:5000/")

        # Find textarea and input expired URL
        driver.find_element_by_name ("text").click ()
        driver.find_element_by_name ("text").send_keys ("http://moss.stanford.edu/results/xyz")

        # Submit form data
        driver.find_element_by_xpath ("//input[@value='Submit']").click ()

        # Assertion
        self.assertEqual ("Uh Oh!", driver.find_element_by_xpath("//h1").text)







    #
    #   SingleURLCheckUsingAllURLsButton ():    Enters in a valid URL and submits using the 'All URLs' button to confirm data entry
    #
    def test_SingleURLCheckUsingAllURLsButton (self):
        driver = self.InitializeBrowserStackConnection ("Submit One URL - Select all")
        
        # Navigate to page
        driver.get ("http://localhost:5000/")

        # Find textarea and input expired URL
        driver.find_element_by_name ("text").click ()
        driver.find_element_by_name ("text").send_keys (self.testURL)

        # Submit form data
        driver.find_element_by_xpath("//input[@value='Submit']").click ()

        # Select 'All URLs' button and submit
        driver.find_element_by_xpath ("(//input[@name='selection'])[last()]").click ()
        driver.find_element_by_xpath ("//input[@value='Submit']").click ()

        # Assert that we successfully landed on the /moss page when submitting in this way.
        self.assertEqual (driver.current_url, 'http://localhost:5000/moss')



    #
    #   MultipleURLsProvidedOneChosen ():   Enters in multiple URLs but only selects one URL to investigate
    #
    def test_MultipleURLsProvidedOneChosen (self):
        driver = self.InitializeBrowserStackConnection ("Submit multiple URLs - Select one")
        
        # Navigate to page
        driver.get ("http://localhost:5000/")

        # Find textarea, input a collection of URLs, and submit form data
        driver.find_element_by_name ("text").click ()
        driver.find_element_by_name ("text").send_keys('\n'.join (self.testURLGroup))        
        driver.find_element_by_xpath ("//input[@value='Submit']").click ()

        # Select the second item in the list of submitted URLs and submit form data again
        driver.find_element_by_xpath ("(//input[@name='selection'])[2]").click ()
        driver.find_element_by_xpath ("//input[@value='Submit']").click ()

        # Assert that we successfully landed on the /moss page when submitting in this way
        self.assertEqual (driver.current_url, 'http://localhost:5000/moss')




    #
    #   MultipleURLsProvidedAllChosen ():   Enters in multiple URLs but only selects one URL to investigate
    #
    def test_MultipleURLsProvidedAllChosen (self):
        driver = self.InitializeBrowserStackConnection ("Submit multiple URLs - Select all")
        
        # Navigate to page
        driver.get ("http://localhost:5000/")

        # Find textarea, input a collection of URLs, and submit form data
        driver.find_element_by_name ("text").click ()
        driver.find_element_by_name ("text").send_keys('\n'.join (self.testURLGroup))        
        driver.find_element_by_xpath ("//input[@value='Submit']").click ()

        # Select the last item in the list of submitted URLs and submit form data again
        driver.find_element_by_xpath ("(//input[@name='selection'])[last()]").click ()
        driver.find_element_by_xpath ("//input[@value='Submit']").click ()

        # Assert that we successfully landed on the /moss page when submitting in this way
        self.assertEqual (driver.current_url, 'http://localhost:5000/moss')