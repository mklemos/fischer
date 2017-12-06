#!/usr/bin/env python
import unittest
import time
import os.path
import socket
import secrets
import setup_login
import dashboard_navigate
from knownPermissions import user_permissions
from compare_lists import compare_lists
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


class test_employee_ATI_WebAlias_sls1231(unittest.TestCase):

    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver

    def test_employee_ATI_WebAlias_sls1231(self):
        # Set drivers from selenium framework
        driver = self.driver
        self.driver.get("https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf")

        # Login as a user and navigate to Requests and Request Accesss
        setup_login.fischer_login(driver, "sls1231")
        dashboard_navigate.gotoRequestAccess(driver)
        dashboard_navigate.selectIncludeSelf(driver)

        dynamicPermisons = dashboard_navigate.DropdownOptionsListCreate(driver)

        knownPermisons = user_permissions["sls1231"]

        boolpermisontest = compare_lists(knownPermisons, dynamicPermisons, "sls1231")

        if boolpermisontest:
            pass
        else:
            assert 2 == 1
 

    def tearDown(self):
        #log out
        setup_login.fischer_logout(self.driver)
        # close the browser window
        self.driver.quit()
