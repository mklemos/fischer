#!/usr/bin/env python
import unittest
import time
import os.path
import socket
import setup_login
import dashboard_navigate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

offical_websiteDict = {"Create website":["Official website"], "Add a developer":[], "Create MySQL accounts":["MySQL Account - Prod", "MySQL Account - Dev Server"], "Reset website permissions":["Production Website - Permission Reset"]}

non_employee_websiteDict = {"Create website":["Official website"], "Add a developer":[], "Reset website permissions":["Production Website - Permission Reset"]}


def official_websiteCheck(driver):
        try:
            #Try to select offical website
            dashboard_navigate.selectDropdownOption(driver, "Official website")
        except:
            #We cant find offical website so something is broken
            assert 2 == 1

        for permision in offical_websiteDict:

            try:
                #Try to select permison
                dashboard_navigate.selectDropdownOption(driver, permision)
                #Make sure each label exists on the page once we select the permision if the permison has labels
                for label in offical_websiteDict[permision]:
                    #Build xpath
                    xpathstart = "//label[contains(text(),'"
                    xpathend = "')]"
                    #Run contains check using thestring of the label getting it from the dictionary
                    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart + label + xpathend)))
            except:
                #We cant find permison in dropdown so fail the test
                assert 2 == 1

def non_employee_websiteDict_Check(driver):
       # added this function so that non-employee types could have access to a sub-dictionary
        try:
            #Try to select offical website
            dashboard_navigate.selectDropdownOption(driver, "Official website")
        except:
            #We cant find offical website so something is broken
            assert 2 == 1

        for permision in non_employee_websiteDict:

            try:
                #Try to select permison
                dashboard_navigate.selectDropdownOption(driver, permision)
                #Make sure each label exists on the page once we select the permision if the permison has labels
                for label in offical_websiteDict[permision]:
                    #Build xpath
                    xpathstart = "//label[contains(text(),'"
                    xpathend = "')]"
                    #Run contains check using thestring of the label getting it from the dictionary
                    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart + label + xpathend)))
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

       dashboard_navigate.gotoRequestAccess(self.driver)
       dashboard_navigate.selectIncludeSelf(self.driver)
       official_websiteCheck(self.driver)


    def tearDown(self):
        #log out
        setup_login.fischer_logout(self.driver)
        # close the browser window
        self.driver.quit()
