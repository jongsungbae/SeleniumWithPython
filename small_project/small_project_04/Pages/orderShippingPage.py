import time
from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class OrderShippingPage:
    def __init__(self, driver):
        self.driver = driver
        self.shipping_checkbox = self.driver.find_element(
            By.CSS_SELECTOR, Locators.orderpage_shipping_checkbox
        )
        self.checkout_button2 = self.driver.find_element(
            By.CSS_SELECTOR, Locators.orderpage_checkout_button2_cssSelector
        )

    def shipping_page(self):
        if self.shipping_checkbox.isChecked():
            pass
        else:
            self.shipping_checkbox.click()

        self.checkout_button2.click()
