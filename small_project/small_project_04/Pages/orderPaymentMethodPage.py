import time
from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class OrderPaymentMethodPage:
    def __init__(self, driver):
        self.driver = driver

        self.payment_bank_button = self.driver.find_element(
            By.CSS_SELECTOR, Locators.orderpage_payment_method_bank_cssSelector
        )
        self.payment_check_button = self.driver.find_element(
            By.CSS_SELECTOR, Locators.orderpage_payment_method_check_cssSelector
        )

    def payment_page(self):
        self.payment_bank_button.click()
