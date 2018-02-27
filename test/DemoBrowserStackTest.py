#!/usr/bin/python

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# class DemoBrowserStackTest (unittest.TestCase):
#   def setUp (self):
#     url = 'http://michaelmiddleton2:[ACCESS_KEY]@hub.browserstack.com:80/wd/hub'
    
#     self.driver = webdriver.Remote(command_executor=url,
#       desired_capabilities = {
#         'os' : 'Windows',
#         'os_version' : '10',
#         'browser' : 'Chrome',
#         'browser_version' : '64.0',
#         'project' : 'SMOSS',
#         'name' : 'Google Search (Demo)',
#         'browserstack.local' : 'false',
#         'browserstack.timezone' : 'EST',
#         'browserstack.selenium_version' : '3.5.2'  
#       })

#   def test_search_in_python_org (self):
#     driver = self.driver
#     driver.get ("http://www.google.com")
#     elem = driver.find_element_by_name ("q")
#     elem.send_keys ("selenium")
#     elem.submit ()
#     self.assertIn ("Google", driver.title)

#   def tearDown (self):
#     self.driver.quit ()