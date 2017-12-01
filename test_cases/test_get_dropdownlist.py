#!/usr/bin/env python
import unittest
import pprint
import time
import json
import os.path
import socket
import secrets
import setup_login
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


class test_get_dropdownlist(unittest.TestCase):

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

        # #Check network folder
        # network_folder_check(driver)
        #
        # #Check offical website
        # official_websiteCheck(driver, "employee-ati")
        #
        # #check personal website
        # personal_website_check(driver)
        #
        # #Check deparmental email acount
        # departmental_email_account_check(driver)
        #
        # #maybe doesn't belong here?
        # it_admin_check(driver)

        lister = dashboard_navigate.navigateDropdownOptions(driver)

        #lister_json = json.dumps(lister)
        #pprint.pprint(lister_json)

        thefile = open('lister.txt', 'w')
        for item in lister:
            thefile.write("%s\n" % item)

    def tearDown(self):
        #log out
        setup_login.fischer_logout(self.driver)
        # close the browser window
        self.driver.quit()
