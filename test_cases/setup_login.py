#This Module if for seting up our testing envierment and for loging into/out of fisher

import socket
import time
import secrets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Setup takes the driver to let the calling class know which session it's controlling
# at the time it's called. We then modify this session, based on host.
# Driver_setup was created for the OBI autotest project by Maximilian Lemos
def driver_setup():
    server_hostname = "dwdb2-dev.humboldt.edu"
    
    if socket.gethostname() == server_hostname:
        # driver = webdriver.Remote(command_executor='http://dw-autotest-dev:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) #dw-autotest-dev or localhost
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
             "(KHTML, like Gecko) Chrome/15.0.87"
             )
        #self.driver = webdriver.PhantomJS(desired_capabilities=dcap)
        driver = webdriver.Remote(command_executor='http://dw-autotest-dev:4444/wd/hub', desired_capabilities=dcap)
        driver.set_window_size(1920,1080)

        return driver
    
    else:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) #dw-autotest-dev or localhost

        return driver


def fischer_login(driver, user_name):
    #Go to idm login
    driver.get("https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf")

    #input User
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='loginform:userid']"))).send_keys(str(user_name))
    #input Password
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='loginform:password']"))).send_keys(secrets.userpass[str(user_name)])
    #click sign in
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='loginform:loginButton']"))).click()
    #Sleep for a second
    time.sleep(1)


def fischer_logout(driver):
    #Signout
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@name='bannerform:logoutlink']"))).click()
    #Sleep for a second to let singout happen
    time.sleep(1)