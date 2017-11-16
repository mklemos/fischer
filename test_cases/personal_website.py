#!/usr/bin/env python
import unittest
import time
import os.path
import socket
import setup_login
import secrets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def personal_website(driver):
