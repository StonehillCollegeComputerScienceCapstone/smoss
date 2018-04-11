#!/usr/bin/env python3.6

#
#   FILE:       SortResultsFrontEndTest.py
#   AUTHOR:     nvidyarthy, mmiddleton
#   DATE:       10 APR 2018
#
#   DESCRIPTION:   
#   This suite runs all of the UAT's from Story #154731155. 
#

import test.frontend.FrontEndConfig as FrontEndConfig
import Config

class SortResultsFrontEndTest (FrontEndConfig.FrontEndTestSuite):
    #
    #   setUp ():       Specifies the build name for the test suite
    #
    def setUp (self):
        FrontEndConfig.FrontEndTestSuite.setUp (self)
        self.buildName = "154731155 - Sort Results"



    #
    #   PercentSortedLowToHigh     -    Ensure that the whole table is sorted low-to-high by percentage
    #
    def test_PercentSortedLowToHigh (self):
        driver = self.InitializeBrowserStackConnection ("Percent Low to High")
        isSorted = False

        try:
            # Navigate to page
            driver.get ("http://127.0.0.1:5000/")

            # Find textarea and input expired URL
            driver.find_element_by_name ("text").click ()
            driver.find_element_by_name("text").clear()
            driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/860369009")

            # Submit form data
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Select proper radio button
            driver.find_element_by_name("selection").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()
            
            # Click on the second column header to sort by percent-match
            driver.find_element_by_xpath("//table[@id='example']/thead/tr/th[2]").click()
            
            # Verify that the list is sorted properly by ensuring variable1 is LE than variable2         
            variable1 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr/td[2]").text
            variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[2]/td[2]").text
            isSorted = (variable1 <= variable2)

        # If there is some sort of Selenium error, catch it here
        except Exception as error:
            print ("\n\n" + str (error) + "\n")


        # Continuing checking until we hit an invalid index OR variable1 > variable2
        index = 3

        while isSorted:
            try:
                variable1 = variable2
                variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[" + index + "]/td[2]").text

            except:
                break

            isSorted = (variable1 <= variable2)
            index += 1

            # If we find a situation where variable1 !<= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue (isSorted)



    #
    #   PercentSortedHighToLow     -    Ensure that the whole table is sorted low-to-high by percentage
    #
    def test_PercentSortedHighToLow (self):
        driver = self.InitializeBrowserStackConnection ("Percent High to Low")
        isSorted = False

        try:
            # Navigate to page
            driver.get ("http://127.0.0.1:5000/")

            # Find textarea and input expired URL
            driver.find_element_by_name ("text").click ()
            driver.find_element_by_name("text").clear()
            driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/860369009")

            # Submit form data
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Select proper radio button
            driver.find_element_by_name("selection").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()
            
            # Click TWICE on the second column header to sort by percent-match
            driver.find_element_by_xpath("//table[@id='example']/thead/tr/th[2]").click()
            driver.find_element_by_xpath("//table[@id='example']/thead/tr/th[2]").click()
            
            # Verify that the list is sorted properly by ensuring variable1 is LE than variable2         
            variable1 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr/td[2]").text
            variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[2]/td[2]").text
            isSorted = (variable1 >= variable2)

        # If there is some sort of Selenium error, catch it here
        except Exception as error:
            print ("\n\n" + str (error) + "\n")


        # Continuing checking until we hit an invalid index OR variable1 > variable2
        index = 3

        while isSorted:
            try:
                variable1 = variable2
                variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[" + index + "]/td[2]").text

            except:
                break

            isSorted = (variable1 >= variable2)
            index += 1

            # If we find a situation where variable1 !<= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue (isSorted)



    #
    #   LinesSortedLowToHigh    -   Ensure that the whole table is sorted low-to-high by lines
    #
    def test_LinesSortedLowToHigh (self):
        driver = self.InitializeBrowserStackConnection ("Lines Low to High")
        isSorted = False

        try:
            # Navigate to page
            driver.get ("http://127.0.0.1:5000/")

            # Find textarea and input expired URL
            driver.find_element_by_name ("text").click ()
            driver.find_element_by_name("text").clear()
            driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/860369009")

            # Submit form data
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Select proper radio button
            driver.find_element_by_name("selection").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Click on the seventh column header to sort by lines-match
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[7]").click()

            # Verify that the list is sorted properly by ensuring variable1 is LE than variable2         
            variable1 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr/td[7]").text
            variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[2]/td[7]").text
            isSorted = (variable1 <= variable2)

        # If there is some sort of Selenium error, catch it here
        except Exception as error:
            print ("\n\n" + str (error) + "\n")


        # Continuing checking until we hit an invalid index OR variable1 > variable2
        index = 3

        while isSorted:
            try:
                variable1 = variable2
                variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[" + index + "]/td[7]").text

            except:
                break

            isSorted = (variable1 <= variable2)
            index += 1

            # If we find a situation where variable1 !<= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue (isSorted)



    #
    #   LinesSortedHighToLow    -   Ensure that the whole table is sorted high-to-low by lines
    #
    def test_LinesSortedHighToLow (self):
        driver = self.InitializeBrowserStackConnection ("Lines High to Low")
        isSorted = False

        try:
            # Navigate to page
            driver.get ("http://127.0.0.1:5000/")

            # Find textarea and input expired URL
            driver.find_element_by_name ("text").click ()
            driver.find_element_by_name("text").clear()
            driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/860369009")

            # Submit form data
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Select proper radio button
            driver.find_element_by_name("selection").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Click TWICE on the seventh column header to sort by lines-match
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[7]").click()
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[7]").click()

            # Verify that the list is sorted properly by ensuring variable1 is GE than variable2         
            variable1 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr/td[7]").text
            variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[2]/td[7]").text
            isSorted = (variable1 >= variable2)

        # If there is some sort of Selenium error, catch it here
        except Exception as error:
            print ("\n\n" + str (error) + "\n")


        # Continuing checking until we hit an invalid index OR variable1 > variable2
        index = 3

        while isSorted:
            try:
                variable1 = variable2
                variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[" + index + "]/td[7]").text

            except:
                break

            isSorted = (variable1 >= variable2)
            index += 1

            # If we find a situation where variable1 !>= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue (isSorted)



    #
    #   UserOneFilenameAToZ     -   Ensure that the whole table's User One Filename is sorted A-to-Z
    #
    def test_UserOneFilenameAToZ (self):
        driver = self.InitializeBrowserStackConnection ("UserOne Filename A to Z")
        isSorted = False

        try:
            # Navigate to page
            driver.get ("http://127.0.0.1:5000/")

            # Find textarea and input expired URL
            driver.find_element_by_name ("text").click ()
            driver.find_element_by_name("text").clear()
            driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/860369009")

            # Submit form data
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Select proper radio button
            driver.find_element_by_name("selection").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Click on the sixth column header to sort alphabetically
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[5]").click()

            # Verify that the list is sorted properly by ensuring variable1 is LE than variable2         
            variable1 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr/td[5]").text
            variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[2]/td[5]").text
            isSorted = (variable1 <= variable2)

        # If there is some sort of Selenium error, catch it here
        except Exception as error:
            print ("\n\n" + str (error) + "\n")


        # Continuing checking until we hit an invalid index OR variable1 > variable2
        index = 3

        while isSorted:
            try:
                variable1 = variable2
                variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[" + index + "]/td[5]").text

            except:
                break

            isSorted = (variable1 <= variable2)
            index += 1

            # If we find a situation where variable1 !<= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue (isSorted)



    #
    #   UserOneFilenameZToA     -   Ensure that the whole table's User One Filename is sorted Z-to-A
    #
    def test_UserOneFilenameZToA (self):
        driver = self.InitializeBrowserStackConnection ("UserOne Filename Z to A")
        isSorted = False

        try:
            # Navigate to page
            driver.get ("http://127.0.0.1:5000/")

            # Find textarea and input expired URL
            driver.find_element_by_name ("text").click ()
            driver.find_element_by_name("text").clear()
            driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/860369009")

            # Submit form data
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Select proper radio button
            driver.find_element_by_name("selection").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Click TWICE on the seventh column header to sort by reverse-alphabetically
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[5]").click()
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[5]").click()

            # Verify that the list is sorted properly by ensuring variable1 is LE than variable2         
            variable1 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr/td[5]").text
            variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[2]/td[5]").text
            isSorted = (variable1 >= variable2)

        # If there is some sort of Selenium error, catch it here
        except Exception as error:
            print ("\n\n" + str (error) + "\n")


        # Continuing checking until we hit an invalid index OR variable1 > variable2
        index = 3

        while isSorted:
            try:
                variable1 = variable2
                variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[" + index + "]/td[5]").text

            except:
                break

            isSorted = (variable1 >= variable2)
            index += 1

            # If we find a situation where variable1 !>= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue (isSorted)



    #
    #   UserTwoFilenameAToZ     -   Ensure that the whole table's User One Filename is sorted A-to-Z
    #
    def test_UserTwoFilenameAToZ (self):
        driver = self.InitializeBrowserStackConnection ("UserOne Filename A to Z")
        isSorted = False
        
        try:
            # Navigate to page
            driver.get ("http://127.0.0.1:5000/")

            # Find textarea and input expired URL
            driver.find_element_by_name ("text").click ()
            driver.find_element_by_name("text").clear()
            driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/860369009")

            # Submit form data
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Select proper radio button
            driver.find_element_by_name("selection").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Click on the sixth column header to sort alphabetically
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[6]").click()

            # Verify that the list is sorted properly by ensuring variable1 is LE than variable2         
            variable1 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr/td[6]").text
            variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[2]/td[6]").text
            isSorted = (variable1 <= variable2)

        # If there is some sort of Selenium error, catch it here
        except Exception as error:
            print ("\n\n" + str (error) + "\n")



        # Continuing checking until we hit an invalid index OR variable1 > variable2
        index = 3

        while isSorted:
            try:
                variable1 = variable2
                variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[" + index + "]/td[6]").text

            except:
                break

            isSorted = (variable1 <= variable2)
            index += 1

            # If we find a situation where variable1 !<= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue (isSorted)



    #
    #   UserTwoFilenameZToA     -   Ensure that the whole table's User One Filename is sorted A-to-Z
    #
    def test_UserTwoFilenameZToA (self):
        driver = self.InitializeBrowserStackConnection ("UserOne Filename Z to A")
        isSorted = False

        try:
            # Navigate to page
            driver.get ("http://127.0.0.1:5000/")

            # Find textarea and input expired URL
            driver.find_element_by_name ("text").click ()
            driver.find_element_by_name("text").clear()
            driver.find_element_by_name("text").send_keys("http://moss.stanford.edu/results/860369009")

            # Submit form data
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Select proper radio button
            driver.find_element_by_name("selection").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()

            # Click TWICE on the seventh column header to sort by reverse-alphabetically
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[6]").click()
            driver.find_element_by_xpath("//table[@id='MOSSResults']/thead/tr/th[6]").click()

            # Verify that the list is sorted properly by ensuring variable1 is LE than variable2         
            variable1 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr/td[6]").text
            variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[2]/td[6]").text
            isSorted = (variable1 >= variable2)

        # If there is some sort of Selenium error, catch it here
        except Exception as error:
            print ("\n\n" + str (error) + "\n")


        # Continuing checking until we hit an invalid index OR variable1 > variable2
        index = 3

        while isSorted:
            try:
                variable1 = variable2
                variable2 = driver.find_element_by_xpath("//table[@id='example']/tbody/tr[" + index + "]/td[6]").text

            except:
                break

            isSorted = (variable1 >= variable2)
            index += 1

            # If we find a situation where variable1 !<= variable2, the list isn't sorting properly
            if (not isSorted):
                break

        self.assertTrue (isSorted)