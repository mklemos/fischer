#!/usr/bin/env python
import unittest
import time
import os.path
import socket
import setup_login
import secrets
import dashboard_navigate
from official_website import non_employee_websiteDict_Check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class test_Non_Employee_ATI_wwh36(unittest.TestCase):

    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver

    def test_Non_Employee_ATI_wwh36(self):
        # Set drivers from selenium framework
        driver = self.driver
        self.driver.get("https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf")

        # Login as a user and navigate to Requests and Request Accesss
        setup_login.fischer_login(driver, "wwh36")
        dashboard_navigate.gotoRequestAccess(driver)
        dashboard_navigate.selectIncludeSelf(driver)

        # Select from the dropdown options under "Select resources and permissions"
        dashboard_navigate.selectDropdownOption(driver, "Official website")
        non_employee_websiteDict_Check(driver)
