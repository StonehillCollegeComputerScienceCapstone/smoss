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

    def test_CurrentToPreviousChecker(self):
        driver = self.InitializeBrowserStackConnection("Test Current-Previous")

        driver.get("http://localhost:5000/")

        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys(self.testURL)
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        driver.find_element_by_name("selection").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        var1 = driver.find_element_by_xpath("//table[@id='MOSSResults']/tbody/tr/td[5]").text
        var2 = driver.find_element_by_xpath("//table[@id='MOSSResults']/tbody/tr/td[6]").text

        self.assertNotEqual(var1[:8], "previous")
        self.assertEqual(var2[:8], "previous")

    def test_CurrentToCurrentChecker(self):
        driver = self.InitializeBrowserStackConnection("Test Current-Current")

        driver.get("http://localhost:5000/")

        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys(self.testURL)
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        driver.find_element_by_name("selection").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        var1 = driver.find_element_by_xpath("//table[@id='MOSSResults']/tbody/tr[3]/td[5]").text
        var2 = driver.find_element_by_xpath("//table[@id='MOSSResults']/tbody/tr[3]/td[6]").text

        self.assertNotEqual(var1[:8], "previous")
        self.assertNotEqual(var2[:8], "previous")

    def test_CurrentToCurrentOrCurrentToPreviousChecker(self):
        driver = self.InitializeBrowserStackConnection("Test Current-Current and Current-Previous and no Previous-Previous")

        driver.get("http://localhost:5000/")

        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys(self.testURL)
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        driver.find_element_by_name("selection").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        index = 3
        isSorted = True
        while isSorted:
            try:
                variable1 = driver.find_element_by_xpath("//table[@id='MOSSResults']/tbody/tr[" + index + "]/td[5]").text
                variable2 = driver.find_element_by_xpath("//table[@id='MOSSResults']/tbody/tr[" + index + "]/td[6]").text

            except:
                break

            if (variable1[:8] == "previous") and (variable2[:8] == "previous"):
                isSorted = False
            elif ((variable1[:8] == "previous") and (variable2[:8] != "previous") or (variable1[:8] != "previous") and (variable2[:8] == "previous")):
                isSorted = True
            index += 1

            # If we find a situation where variable1 !>= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue(isSorted)
