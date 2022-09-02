from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.my_account_title = self.driver.find_element(
            By.XPATH, Locators.myAccount_title_value_xpath
        ).text
        self.wishlist_button = self.driver.find_element(
            By.XPATH, Locators.wishlist_xpath
        )
        self.orderhistory_button = self.driver.find_element(
            By.XPATH, Locators.orderhistory_xpath
        )

    def my_account_validate(self):
        assert self.my_account_title == "MY ACCOUNT"
        assert self.wishlist_button.is_enabled()
        assert self.orderhistory_button.is_enabled()

    def wishlist_click(self):
        self.wishlist_button.click()

    def orderhistory_click(self):
        self.orderhistory_button.click()
