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


class test_add_remove_site(unittest.TestCase):

    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver

    def test_add_remove_site(self):
        # Set drivers from selenium framework
        driver = self.driver
        self.driver.get("https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf")

        # Login as a user and navigate to Requests and Request Accesss
        setup_login.fischer_login(driver, "sls1231")
        dashboard_navigate.gotoRequestAccess(driver)
        dashboard_navigate.selectIncludeSelf(driver)
        time.sleep(2)
        dashboard_navigate.selectDropdownOption(driver, 'Official website')
        dashboard_navigate.selectDropdownOption(driver, 'Create website')
        dashboard_navigate.selectCheckbox(driver, 'Official website')
        dashboard_navigate.enterTextInDatafield(driver, 'Website Name:', "Selenium_test_site")
        dashboard_navigate.clickButton(driver, 'Continue')
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@value='Continue']"))).click()


        time.sleep(100)
    def tearDown(self):
        #log out
        setup_login.fischer_logout(self.driver)
        # close the browser window
        self.driver.quit()

# sls requesting a official site

# mmh approves official site request

# webdriver waits and visits new site

# sls requests to add a developer. puts website name

# sls logs back in, requests sql server (dev checkbox)

# mmh logs in and approves

# sls logs in and sets the password for the sql server requested under "My Accounts", must be unique from the account password.

# webdriver check to see site exists with SQL server go to: http://www-dev.humboldt.edu/phpmyadmin/ username is website truncated to 16 char and the password is the unique one set under my accounts

# sls logs back in and requests the removal of sql server and site in two sequential loops

# mmh approves removal of both, but in two sequential loops

# Webdriver checks to make sure that website is now gone.
