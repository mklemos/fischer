import socket
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def gotoRequestAccess(driver):
    #Click on the requests tab
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(text(),'Requests')]"))).click()
    #Click on the Request Access tab
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(text(),'Request Access')]"))).click()

def selectIncludeSelf(driver):
    #Click on include self checkbox
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='selectUserFormRequestAccess:addself']"))).click()

def selectDropdownOption(driver, optionvalue):
    
    xpathstart = "//option[@value='"
    xpathend = "']"
    #click on an option via our created xpath
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart + optionvalue +  xpathend))).click()
