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

    def test_a_site(self):
        driver = self.driver
        #Go to idm-dev login but dont actualy login
        self.driver.get("https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf")

    def tearDown(self):
        # close the browser window
        self.driver.quit()


class test_b_login_and_logout(unittest.TestCase):

    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver

    def test_a_login(self):
        #sign in using sign in abstraction
        setup_login.fischer_login(self.driver, "cnn71")

    def tearDown(self):
        #signout
        setup_login.fischer_logout(self.driver)
        # close the browser window
        self.driver.quit()
