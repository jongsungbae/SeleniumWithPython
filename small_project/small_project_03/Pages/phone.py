import time

from selenium.webdriver.support import expected_conditions

from small_project_03.Locators.locator import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class PhonePage():
    def __init__(self, driver):
        self.driver = driver
        self.menu_phone_locator = Locators.menu_phone_xpath
        self.phone_title_locator = Locators.phone_title_xpath
        self.iphone_locator = Locators.iphone_cssSelector
        self.first_picture_locator = Locators.first_picture_xpath
        self.right_arrow_button_locator = Locators.right_arrow_button_cssSelector
        self.picture_close_locator = Locators.picture_close_cssSelector


    def menubar_phone(self):
        self.driver.find_element(By.XPATH, self.menu_phone_locator).click()

    def get_phone_title(self):
        phone_title = self.driver.find_element(By.XPATH, self.phone_title_locator).text
        return phone_title

    def click_iphone(self):
        self.driver.find_element(By.CSS_SELECTOR, self.iphone_locator).click()

    def click_iphone_picture(self):
        self.driver.find_element(By.XPATH, self.first_picture_locator).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.right_arrow_button_locator)))

    def right_arrow_picture(self):
        right_arrow_button = self.driver.find_element(By.CSS_SELECTOR, self.right_arrow_button_locator)
        for i in range(0, 6):
            if i < 5:
                self.driver.save_screenshot(f'screenshot_iphone_#{i + 1}.png')
                right_arrow_button.click()
                time.sleep(1)
            else:
                self.driver.save_screenshot(f'screenshot_iphone_#{i + 1}.png')

        self.driver.find_element(By.CSS_SELECTOR, self.picture_close_locator).click()







