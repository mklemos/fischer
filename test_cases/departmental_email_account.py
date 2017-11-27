#!/usr/bin/env python
import dashboard_navigate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

folder_list = ["Departmental Email Account",
               ]

def departmental_email_account_check(driver):
    #Navgate to deparment email by selecting it as a dropdown option
    dashboard_navigate.selectDropdownOption(driver, "Departmental Email Account")

    xpathstart = "//label[contains(text(),"
    xpathend = ")]"
    for i in folder_list:
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart +"'"+ i +"'"+ xpathend)))
