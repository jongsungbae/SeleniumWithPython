import time
from random import *
import string

from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_title = self.driver.find_element(
            By.XPATH, Locators.login_title_value_xpath
        ).text
        self.username = self.driver.find_element(By.ID, Locators.login_email_box_id)
        self.password = self.driver.find_element(By.ID, Locators.login_password_box_id)
        self.signin_button = self.driver.find_element(
            By.ID, Locators.login_submit_button_id
        )
        self.create_account_button = self.driver.find_element(
            By.ID, Locators.login_create_account_id
        )
        self.create_email = self.driver.find_element(
            By.ID, Locators.long_create_email_id
        )

    def loginPage_validate(self):
        assert self.login_title == "AUTHENTICATION"
        assert self.username.is_enabled()
        assert self.password.is_enabled()
        assert self.signin_button.is_enabled()
        assert self.signin_button.is_enabled

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.signin_button.click()

    def randomEmail(self):
        srting_pool = string.ascii_letters
        random_email = "".join(choice(srting_pool) for _ in range(12)) + "@test.com"
        return random_email

    def click_create_account(self, email):
        self.create_email.send_keys(email)
        print(email)
        self.create_account_button.click()
