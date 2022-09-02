import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_image = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_image_cssSelector
        )
        self.more_button = self.driver.find_element(
            By.CSS_SELECTOR, Locators.search_result_more_cssSelector
        )

    def searchResultPage_validate(self):
        assert self.search_image.is_displayed()

    def click_search_image(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.search_image).perform()
        self.more_button.click()
