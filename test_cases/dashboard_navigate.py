#!/usr/bin/env python
import socket
import time
from pprint import pprint
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
    #Get our first dropdown
    optionDropdown = WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"tr > td:nth-of-type(2) > select.combores" )))
    #Create a select from the first dropdown
    optionSelect = Select(optionDropdown)
    #Create a list for storing the text of each option for the first dropdown
    optionTextList = []
    #Create a list that we will populate with each option and its suboption to return at the end of this function
    PermissionProfileList = []
    #for each options in the dropdwn slect
    for option in optionSelect.options:
        #Store that options contains text in a list, igornoring the "Select" the u means its unicode
        if(option.text != u"Select"):
            optionTextList.append(option.text)

    for optionText in optionTextList:
        #navigate to each option
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//option[contains(text(),'" + optionText + "')]"))).click()
        #Check to see if we have another dropdown now present
        #If so lets do this same thing again and get all the dropdown options
        try:
            #Try to get the second dropdown to see if it exists
            optionDropdownTwo = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"tr > td:nth-of-type(5) > select.combores" )))
            #Create an select out of the second dropdown
            optionSelectTwo = Select(optionDropdownTwo)
            #Create a list for storing the text of each option for the second dropdown
            optionTextListTwo = []
            #populate a list of the contains text in each option, ex "Create MySQL accounts"
            for optiontwo in optionSelectTwo.options:
                #igornoring the "Select" the u means its unicode
                if(optiontwo.text != u"Select"):
                    optionTextListTwo.append(optiontwo.text)

            #For each text in the optiontextlist append to the list of lists
            for optiontexttwo in optionTextListTwo:
                #Apend to the list the dropdown options avalible in this sub option
                PermissionProfileList.append([optionText, optiontexttwo])
                
        except:
            #If we cant find that second dropdown we dont have one, so just output the first option and a blank as its child option
            PermissionProfileList.append([optionText, ""])

        #pprint for debug
        pprint(PermissionProfileList)

    return PermissionProfileList
