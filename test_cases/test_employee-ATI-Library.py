#!/usr/bin/env python
import unittest
import time
import os.path
import socket
import setup_login
import secrets
import dashboard_navigate
from network_folder import network_folder_check
from personal_website import personal_website_check
from departmental_email_account import departmental_email_account_check
from it_admin import it_admin_check
from official_website import official_websiteCheck
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class test_test_employee_ATI_Library(unittest.TestCase):

    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver

    def test_test_employee_ATI_Library(self):
        # Set drivers from selenium framework
        driver = self.driver
        self.driver.get("https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf")

        # Login as a user and navigate to Requests and Request Accesss
        setup_login.fischer_login(driver, "")
        dashboard_navigate.gotoRequestAccess(driver)
        dashboard_navigate.selectIncludeSelf(driver)

        # Select from the dropdown options under "Select resources and permissions"

        network_folder_check(driver)

        official_websiteCheck(driver, "employee-ati")


    def tearDown(self):
        #log out
        setup_login.fischer_logout(self.driver)
        # close the browser window
        self.driver.quit()
