#!/usr/bin/env python3.6

#
#   FILE:       FrontEndConfig.py
#   AUTHOR:     mmiddleton
#   DATE:       16 MAR. 2018
#
#   DESCRIPTION:
#   Should be extended by all FrontEnd tests. It contains the boiler-plate Selenium/BrowserStack initialization
#   and termination methods.
#

import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FrontEndTestSuite (unittest.TestCase):
    driver = None
    url = None

    #
    #   setUp ():   Selenium/BrowserStack - Required to make initial connection with the BS server.
    #
    def setUp (self):
        self.url = "http://" + os.environ['BROWSERSTACK_USER'] + ":" + os.environ['BROWSERSTACK_ACCESS_KEY'] + "@hub.browserstack.com:80/wd/hub"



    #
    #   InitializeBrowserStackConnection ():    Makes connection to BrowserStack for each test and sets self.driver to a value so
    #                                           that tearDown () will properly execute. Returns self.driver for individual test use. 
    #
    def InitializeBrowserStackConnection (self, testName):
        desiredCapabilities = {
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
        
        self.driver = webdriver.Remote (command_executor = self.url, desired_capabilities = desiredCapabilities)

        return self.driver



    #
    #   tearDown ():    Selenium/BrowserStack - Required to terminating connection to the BS server.
    #
    def tearDown (self):
        self.driver.quit ()