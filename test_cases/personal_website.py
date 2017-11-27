#!/usr/bin/env python
import dashboard_navigate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

folder_list = ["Personal website - MySQL",
               ]

def personal_website_check(driver):
        #Navitage to personal website
        dashboard_navigate.selectDropdownOption(driver, "Personal website")

        xpathstart = "//label[contains(text(),"
        xpathend = ")]"
        for i in folder_list:
            WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart +"'"+ i +"'"+ xpathend)))
