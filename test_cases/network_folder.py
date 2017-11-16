from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

folder_list = ["Increase Quota to 250MB",
               "Increase Quota to 500MB",
               "Increase Quota to 1GB",
               "Increase Quota to 2.5GB",
               "Increase Quota to 5GB",
               "Increase Quota to 10GB",
               "Increase Quota to 12.5GB",
               "Increase Quota to 25GB",
               "Increase Quota to 100GB"
               ]

def network_folder_check(driver):
        xpathstart = "//*[contains(text(),"
        xpathend = ")]"
        for i in folder_list:
            WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpathstart +"'"+ i +"'"+ xpathend))).text
        return i
