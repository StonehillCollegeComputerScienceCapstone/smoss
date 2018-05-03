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
    '''
    def test_MultipleURLsTopTenLinesMultipleAssignments(self):
        driver = self.InitializeBrowserStackConnection("Test Top Ten Lines Matched Multiples Assignments")

        # Navigate to page
        driver.get("http://localhost:5000/")

        # Find textarea and input Single URLs
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys(self.testURL)
        # Submit form data
        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # Select the sixth item in the list of submitted URLs and submit form data again
        driver.find_element_by_xpath("(//input[@name='selection'])[2]").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # Store the values of the top ten lines matched
        var1 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr/td[2]").text
        var2 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[2]/td[2]").text
        var3 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[3]/td[2]").text
        var4 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[4]/td[2]").text
        var5 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[5]/td[2]").text
        var6 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[6]/td[2]").text
        var7 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[7]/td[2]").text
        var8 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[8]/td[2]").text
        var9 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[9]/td[2]").text
        var10 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[10]/td[2]").text

        # Assertion
        self.assertTrue(var1 >= var2 >= var3 >= var4 >= var5 >= var6 >= var7 >= var8 >= var9 >= var10)
    '''
    def test_MultipleURLsTopTenPercentsMultipleAssignments(self):
        driver = self.InitializeBrowserStackConnection("Test Top Ten Percent Matched Multiple Assignments")

        # Navigate to page
        driver.get("http://localhost:5000/")

        # Find textarea and input Single URLs
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys(self.testURL)
        # Submit form data
        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # Select the sixth item in the list of submitted URLs and submit form data again
        driver.find_element_by_xpath("(//input[@name='selection'])[2]").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # Store the values of the top ten lines matched
        var1 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr/td[2]").text
        var2 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[2]/td[2]").text
        var3 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[3]/td[2]").text
        var4 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[4]/td[2]").text
        var5 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[5]/td[2]").text
        var6 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[6]/td[2]").text
        var7 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[7]/td[2]").text
        var8 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[8]/td[2]").text
        var9 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[9]/td[2]").text
        var10 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[10]/td[2]").text

        # Assertion
        self.assertTrue(var1 >= var2 >= var3 >= var4 >= var5 >= var6 >= var7 >= var8 >= var9 >= var10)
    '''
    def test_MultipleURLsTopTenLinesSingleAssignment(self):
        driver = self.InitializeBrowserStackConnection("Test Top Ten Lines Matched Single Assignment")
        driver.get("http://localhost:5000/")
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/47342166")
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        driver.find_element_by_xpath("(//input[@name='selection'])[2]").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        var1 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr/td[2]").text
        var2 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[2]/td[2]").text
        var3 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[3]/td[2]").text
        var4 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[4]/td[2]").text
        var5 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[5]/td[2]").text
        var6 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[6]/td[2]").text
        var7 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[7]/td[2]").text
        var8 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[8]/td[2]").text
        var9 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[9]/td[2]").text
        var10 = driver.find_element_by_xpath("//table[@id='HighestLinesMatched']/tbody/tr[10]/td[2]").text

        # Assertion
        self.assertTrue(var1 >= var2 >= var3 >= var4 >= var5 >= var6 >= var7 >= var8 >= var9 >= var10)
    '''

    def test_MultipleURLsTopTenPercentSingleAssignment(self):
        driver = self.InitializeBrowserStackConnection("Test Top Ten Percent Matched Single Assignment")

        # Navigate to page
        driver.get("http://localhost:5000/")

        # Find textarea and input Single URLs
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys(self.testURL)
        # Submit form data
        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # Select the sixth item in the list of submitted URLs and submit form data again
        driver.find_element_by_xpath("(//input[@name='selection'])[2]").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # Store the values of the top ten lines matched
        var1 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr/td[2]").text
        var2 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[2]/td[2]").text
        var3 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[3]/td[2]").text
        var4 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[4]/td[2]").text
        var5 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[5]/td[2]").text
        var6 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[6]/td[2]").text
        var7 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[7]/td[2]").text
        var8 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[8]/td[2]").text
        var9 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[9]/td[2]").text
        var10 = driver.find_element_by_xpath("//table[@id='HighestPercentMatched']/tbody/tr[10]/td[2]").text

        # Assertion
        self.assertTrue(var1 >= var2 >= var3 >= var4 >= var5 >= var6 >= var7 >= var8 >= var9 >= var10)

    def test_MultipleURLFormSubmission(self):
        driver = self.InitializeBrowserStackConnection("Test Multiple URL Form Submission")
        driver = self.driver
        driver.get("http://localhost:5000/")
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys('\n'.join(self.testURLGroup))
        driver.find_element_by_xpath("//input[@value='Submit']").click()


