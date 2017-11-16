#!/usr/bin/env python
import unittest
import time
import os.path
import socket
import setup_login
import dashboard_navigate
from treelib import Node, Tree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

offical_websiteList = ["Create website", "Add a developer", "Create MySQL accounts", "Reset website permissions"]


def official_websiteCheck(driver):
        dashboard_navigate.gotoRequestAccess(driver)

        dashboard_navigate.selectIncludeSelf(driver)

        try:
            #Try to select offical website
            dashboard_navigate.selectDropdownOption(driver, "Official website")
        except:
            #We cant find offical website so something is broken
            assert 2 == 1

        for permision in offical_websiteList:
            
            try:
                #Try to select permison
                dashboard_navigate.selectDropdownOption(driver, permision)
            except:
                #We cant find permison in dropdown so fail the test
                assert 2 == 1



class test_c_Test(unittest.TestCase):

    def setUp(self):
        #Setup driver
        driver = setup_login.driver_setup()
        self.driver = driver
        #Login to fischer using driver
        setup_login.fischer_login(self.driver, "sls1231")

    def test_c_Test(self):
       official_websiteCheck(self.driver)


    def tearDown(self):
        #log out
        setup_login.fischer_logout(self.driver)
        # close the browser window
        self.driver.quit()
