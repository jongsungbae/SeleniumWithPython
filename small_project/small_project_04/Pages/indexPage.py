import time

from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class IndexPage:
    def __init__(self, driver):
        self.driver = driver
        self.logo = self.driver.find_element(By.XPATH, Locators.logo_image_value_xpath)
        self.mystore_title = self.driver.title
        self.searchBox = self.driver.find_element(By.ID, Locators.search_box_value_id)
        self.search_button = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_submit_value_cssSelector
        )
        self.signin_button = self.driver.find_element(
            By.XPATH, Locators.signin_button_value_xpath
        )

    def indexPage_validate(self):
        assert self.mystore_title == "My Store"
        assert self.logo.is_enabled()
        assert self.searchBox.is_enabled()
        assert self.search_button.is_enabled()
        assert self.signin_button.is_enabled()

    def input_search_product(self, search_product):
        # time.sleep(2)
        self.searchBox.click()
        time.sleep(1)
        self.searchBox.send_keys(search_product)
        self.search_button.click()
