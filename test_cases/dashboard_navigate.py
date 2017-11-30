#!/usr/bin/env python
import socket
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


def gotoRequestAccess(driver):
    #Click on the requests tab
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(text(),'Requests')]"))).click()
    #Click on the Request Access tab
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(text(),'Request Access')]"))).click()

def selectIncludeSelf(driver):
    #Click on include self checkbox
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='selectUserFormRequestAccess:addself']"))).click()

def selectDropdownOption(driver, optioncontains):

    xpathstart = "//option[contains(text(),'"
    xpathend = "')]"
    #click on an option via our created xpath
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart + optioncontains +  xpathend))).click()


def navigateDropdownOptions(driver):
    #Get our first list of options
    optionDropdown = WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"tr > td:nth-of-type(2) > select.combores" )))
    optionSelect = Select(optionDropdown)
    optionTextList = []
    for option in optionSelect.options:
        #navigate to that option
        optionTextList.append(option.text)
        time.sleep(1)

