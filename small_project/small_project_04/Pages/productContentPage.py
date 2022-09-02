import time

from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class SearchContentPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_image = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_image_cssSelector
        )
        self.quantity = self.driver.find_element(
            By.ID, Locators.search_result_quantity_id
        )
        self.select_size = self.driver.find_element(
            By.XPATH, Locators.search_result_size_xpath
        )
        self.select_size_small = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_size_small_cssSelector
        )
        self.select_size_medium = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_size_medium_cssSelector
        )
        self.select_size_large = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_size_large_cssSelector
        )
        self.color_orange = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_color_orange_cssSelector
        )
        self.color_blue = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_color_blue_cssSelector
        )
        self.add_cart_button = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_add_cart_button_cssSelector
        )
        self.add_cart_result_text = self.driver.find_element(By.XPATH, Locators.add_cart_result_xpath).text
        self.checkout_button = self.driver.find_element(By.CSS_SELECTOR, Locators.checkout_button_cssSelector)

    def searchResultPage_validate(self):
        assert self.search_image.is_displayed()
        assert self.quantity.is_enabled()
        assert self.select_size.is_enabled()
        assert self.add_cart_button.is_enabled()

    def select_quantity(self, qty):
        self.quantity.click()
        self.quantity.clear()
        self.quantity.send_keys(qty)
        time.sleep(2)

    def select_size(self):
        self.select_size().click()
        time.sleep(5)
        self.select_size_large.click()
        time.sleep(5)

    def select_color(self):
        self.color_blue.click()

    def add_to_cart(self):
        self.add_cart_button.click()
        success_text = "Product successfully added"

        assert self.add_cart_result_text in success_text
        self.checkout_button.click()






