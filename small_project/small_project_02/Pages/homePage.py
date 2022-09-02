from selenium.webdriver.common.by import By
from small_project_02.Locators.locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_dropdown_CSSSELECTOR = Locators.welcome_dropdown_CSSSELECTOR
        self.logout_linktext = Locators.logout_linktext

    def click_welcome(self):
        self.driver.find_element(
            By.CSS_SELECTOR, self.welcome_dropdown_CSSSELECTOR
        ).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_linktext).click()
