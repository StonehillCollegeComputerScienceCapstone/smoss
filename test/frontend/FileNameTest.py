#!/usr/bin/env python3.6

#
#   FILE:       SortResultsFrontEndTest.py
#   AUTHOR:     nvidyarthy, mmiddleton, wgreelish
#   DATE:       10 APR 2018
#
#   DESCRIPTION:
#   This suite runs all of the UAT's from Story #154731155.
#

import test.frontend.FrontEndConfig as FrontEndConfig


class FileNameTest (FrontEndConfig.FrontEndTestSuite):

    #
    #   setUp ():       Specifies the build name for the test suite
    #
    def setUp (self):
        FrontEndConfig.FrontEndTestSuite.setUp (self)
        self.buildName = "154706492 - File Name Test"

    def test_CurrentToCurrentOrPreviousChecker(self):
        driver = self.InitializeBrowserStackConnection("Current-Current or Current-Previous")

        driver.get("http://localhost:5000/")

        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys(self.testURL)
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        driver.find_element_by_name("selection").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        var1 = driver.find_element_by_xpath("//table[@id='MOSSResults']/tbody/tr/td[5]").text
        var2 = driver.find_element_by_xpath("//table[@id='MOSSResults']/tbody/tr/td[6]").text

        self.assertNotEqual(var1[:7], var2[:7])
