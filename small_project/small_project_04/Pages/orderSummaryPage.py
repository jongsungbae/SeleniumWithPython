import time

from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class OrderSummaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.order_summary_button = self.driver.find_element(By.XPATH, Locators.orderpage_order_summary_button_xpath)


    def order_confirm_page(self):
        self.order_summary_button.click()
        self.order_confirm_message = self.driver.find_element(By.XPATH, Locators.orderpage_order_confirm_xpath).text
        assert "Your order on My Store is complete." == self.order_confirm_message
