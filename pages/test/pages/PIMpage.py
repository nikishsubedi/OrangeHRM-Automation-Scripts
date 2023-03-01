import time

from selenium import webdriver
from pages.test.pages.Login import OrangeHRM
# Set up the Chrome driver
driver = webdriver.Chrome()

# Instantiate the OrangeHRM class
orangehrm = OrangeHRM(driver)

# Log in with valid credentials
orangehrm.login("Admin", "admin123")
time.sleep(5)
# PIM

