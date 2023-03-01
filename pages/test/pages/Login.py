import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_field = (By.CSS_SELECTOR, "input[placeholder='Username']")
        self.password_field = (By.CSS_SELECTOR, "input[placeholder='Password']")
        self.login_button = (By.CSS_SELECTOR, "button[type='Submit']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.welcome_message = (By.ID, "welcome")

    def get_welcome_message_text(self):
        return self.driver.find_element(*self.welcome_message).text


class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()

        time.sleep(5)

    def get_welcome_message_text(self):
        return self.home_page.get_welcome_message_text()
