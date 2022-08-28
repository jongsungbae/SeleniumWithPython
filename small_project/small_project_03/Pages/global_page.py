import time

from selenium.webdriver.support import expected_conditions

from small_project_03.Locators.locator import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class GlobalPage():
    def __init__(self, driver):
        self.driver = driver
        self.quantity_locator = Locators.quantity_cssSelector
        self.add_cart_locator = Locators.add_cart_cssSelector
        self.add_cart_success_text_locator = Locators.add_cart_success_text_cssSelector
        self.go_to_cart_locator = Locators.go_to_cart_id
        self.checkout_button_locator = Locators.checkout_button_xpath

    def input_quantity(self, quantity):
        quantity_field = self.driver.find_element(By.CSS_SELECTOR, self.quantity_locator)
        quantity_field.clear()
        time.sleep(3)
        quantity_field.send_keys(quantity)

    def add_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_cart_locator).click()
        success_text = self.driver.find_element(By.CSS_SELECTOR, self.add_cart_success_text_locator).text
        return success_text

    def checkout(self):
        self.driver.find_element(By.ID, self.go_to_cart_locator).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.checkout_button_locator).click()
