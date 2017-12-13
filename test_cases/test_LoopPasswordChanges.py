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


class LoopPasswordChanges(unittest.TestCase):
    def setUp(self):
        driver = setup_login.driver_setup()
        self.driver = driver
        setup_login.fischer_admin_login(driver, "selenium_adm")


    def test_loop_password_changes(self):
        driver = self.driver
        user_ids = ["010008827","946461406","010015314","010000195"]
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | new Array("010008827","946461406","010015314","010000195") | ]]
        # ERROR: Caught exception [unknown command [while]]
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | index | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['people'][storedVars['temp']] | ]]
        #dynamicui:PROFILEID
        # .send_keys(str(search_item))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@id='dynamicui:PROFILEID']"))).send_keys(user_ids[0])
        #WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "html > body > table > tbody > tr > td > table > tbody > tr > td#dynTableDiv > table > tbody > tr > td#td_dynamicui:PROFILEID > input#dynamicui:PROFILEID.textInput120"))).send_keys(user_ids[0])

    #
    #
    #     driver.find_element_by_id("dynamicui:PROFILEID").send_keys(emplid)
    #     driver.find_element_by_css_selector("input.viewButts").click() #Click on search button
	# 	#Timeout loop
    #     for i in range(60):
    #         try:
    #             if self.is_element_present(By.ID, "0"): break
    #         except: pass
    #         time.sleep(1)
    #     else: self.fail("time out")
    #     driver.find_element_by_id("0").click() #click on the first ite in the list
    #     driver.find_element_by_css_selector("#buttons > input.viewButts").click() #click on view profile button
	# 	#timout loop
    #     for i in range(60):
    #         try:
    #             if self.is_element_present(By.ID, "passViewBtn"): break
    #         except: pass
    #         time.sleep(1)
    #     else: self.fail("time out")
    #     self.assertEqual("", driver.find_element_by_id("updateProfBtn").text) #Check that the updateProfBtn exists
    #     driver.find_element_by_id("passViewBtn").click() #Click Twise to confirm you want to change password
    #     driver.find_element_by_id("passViewBtn").click()
	# 	#Wait
    #     for i in range(60):
    #         try:
    #             if self.is_element_present(By.ID, "newpass"): break
    #         except: pass
    #         time.sleep(1)
    #     else: self.fail("time out")
    #     driver.find_element_by_id("newpass").clear() #Clear password input
    #     driver.find_element_by_id("newpass").send_keys(password) #send password
    #     driver.find_element_by_id("cfmpass").clear() #Clear confirm pass
    #     driver.find_element_by_id("cfmpass").send_keys(password) #Iput confirm pass
	# 	#Wait
    #     for i in range(60):
    #         try:
    #             if self.is_element_present(By.ID, "HSU Accounts"): break
    #         except: pass
    #         time.sleep(1)
    #     else: self.fail("time out")
    #     driver.find_element_by_id("HSU Accounts").click() #Check the HSU accounts to confirm you want to change all the hsu passwords
    #     driver.find_element_by_id("btnResetPswd").click() #Click reset password button
	# 	#Add a wait for contains Successful
    #     driver.find_element_by_xpath("//td[@id='adminMenu']/table/tbody/tr[5]/td[2]").click() #Click modifey prfoile to go back to start of loop
    #     # ERROR: Caught exception [unknown command [endWhile]]
    #
    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e: return False
    #     return True
    #
    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException as e: return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True
    #
    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
