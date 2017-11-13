#!/usr/bin/env python
import unittest
import time
import os.path
import socket
import setup_login
import secrets
import dashboard_navigate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class test_initial_steps(unittest.TestCase):

    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver

    def test_initial_steps(self):
        driver = self.driver
        #self.driver.implicitly_wait(7) # seconds
        self.driver.get("https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf")

        setup_login.fischer_login(driver, "kmk877")
        dashboard_navigate.gotoRequestAccess(driver)
        assert True
