#!/usr/bin/env/python

#
#   FILE:       GoogleSearch.py
#   AUTHOR:     mmiddleton
#   DATE:       28 FEB 2018
#
#   DESCRIPTION:   
#   This file tests a basic connection to Google. It is the initial test run on our Browser Stack server.
#

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearch (unittest.TestCase):
    def setUp (self):
        url = "http://michaelmiddleton2:KzeJ27iophC6F8Lonvhi@hub.browserstack.com:80/wd/hub"
        desiredCapabilities = {
            'os' : 'Windows',
            'os_version' : '10',
            'browserstack.timezone' : 'EST',
            'browserstack.selenium_version' : '3.5.2',  
            'browser' : 'Chrome',
            'browser_version' : '64.0',
            'project' : 'SMOSS',
            'name' : 'Google Search (Demo)',
            'browserstack.local' : 'false'
        }
        self.driver = webdriver.Remote (command_executor = url, desired_capabilities = desiredCapabilities)

    def test_search_in_python_org (self):
        driver = self.driver
        driver.get ("http://www.google.com")
        elem = driver.find_element_by_name ("q")
        elem.send_keys ("selenium")
        elem.submit ()
        self.assertIn ("Google", driver.title)

    def tearDown (self):
        self.driver.quit ()

if __name__ == "__main__":
    unittest.main ()