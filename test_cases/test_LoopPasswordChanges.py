# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#added after export
import setup_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random

class LoopPasswordChanges(unittest.TestCase):
    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver
        setup_login.fischer_admin_login(driver, "selenium_adm")


    def test_loop_password_changes(self):
        driver = self.driver
        #set uid array
        user_ids = ["010008827","946461406","010015314","010000195"]

        #set empty pwd list, about to be generated
        pwd_list = []

        #for loop to generate random new password
        for ids in user_ids:
            #set password
            x = random.randint(0,99999)
            passwords = 'Fischer'
            passwords += str(x)
            pwd_list.append(passwords)

        #creating dictionary to store passwords with associated users
        user_tuple_list = zip(user_ids, pwd_list)
        user_dict = dict(user_tuple_list)

        #Switch to the frame our elements are on
        WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//frame[@name='mainFrame']")))
        driver.switch_to.frame("mainFrame")

        #enter loop for user dictionary to reset all passwords in user_dict
        for user in user_dict:
            #send uid for the first user in the user_dict
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, 'dynamicui:PROFILEID'))).clear()

            #send uid for the first user in the user_dict
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, 'dynamicui:PROFILEID'))).send_keys(user)

            #click the "search" button
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'input.viewButts'))).click()

            #click the checkbox for the user specified by uid earlier, there should be one user because of the unique id
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, '0'))).click()

            #click the "View Profile" button
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#buttons > input.viewButts'))).click()

            #click "Password View" number
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "passViewBtn"))).click()

            #wait for the full set of checkbox items to load, this will wait for the "Profile View" to be present onscreen
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "btnProfileView")))

            #send password
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "newpass"))).send_keys(user_dict.get(user))

            #send password confirmation
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "cfmpass"))).send_keys(user_dict.get(user))

            #Check the HSU accounts to confirm you want to change all the hsu passwords
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "HSU Accounts"))).click()

            #Click "Reset Password" button
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "btnResetPswd"))).click()

            #wait for success response
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "refresh_btn")))

            #Click modifey prfoile to go back to start of loop
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//td[@id='adminMenu']/table/tbody/tr[5]/td[2]"))).click()


    def tearDown(self):
        #log out
        setup_login.fischer_admin_logout(self.driver)
        # close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
