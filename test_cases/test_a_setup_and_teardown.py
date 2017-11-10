#!/usr/bin/env python
import unittest
import time
import os.path
import socket
import setup_login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class test_a_setup_and_teardown(unittest.TestCase):

    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver

    def test_a_Site(self):
        #Go to idm-dev login but dont actualy login
        self.driver.get("https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf")

    def test_b_LoginLogout(self):
        try:
            #try to signin
            setup_login.fischer_login(self.driver, "cnn71")
        except:
            #login failed, lets take a screenshot
            #TODO: Screenshot
            #Fail the test
            assert 2 ==1

        try:
            #try to signout
            setup_login.fischer_logout(self.driver)
        except:
            #logout failed, lets take a screenshot
            #TODO: Screenshot
            #Fail the test
            assert 2 ==1


    def tearDown(self):
        # close the browser window
        self.driver.quit()
