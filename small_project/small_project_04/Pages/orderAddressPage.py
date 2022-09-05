import time


from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class OrderAddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button1 = self.driver.find_element(
            By.CSS_SELECTOR, Locators.orderpage_checkout_button1_cssSelector
        )

    def checkout_button(self):
        self.checkout_button.click()
