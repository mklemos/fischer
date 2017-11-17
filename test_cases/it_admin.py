#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

folder_list = ["Google Apps - Admin",
               "Active Directory - Admin",
               "LDAP bnd Account",
               ]

def it_admin_check(driver):
        for label in folder_list:
            #Build xpath
            xpathstart = "//label[contains(text(),'"
            xpathend = "')]"
            #Run contains check using thestring of the label getting it from the dictionary
            WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart + label + xpathend)))
