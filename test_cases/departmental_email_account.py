#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

folder_list = ["Departmental Email Account",
               ]

def departmental_email_account_check(driver):
        xpathstart = "//*[contains(text(),"
        xpathend = ")]"
        for i in folder_list:
            WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart +"'"+ i +"'"+ xpathend))).text
        return i
