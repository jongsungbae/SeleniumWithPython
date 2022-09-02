import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from small_project_03.Locators.locator import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LaptopPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_laptop_locator = Locators.menu_laptop_xpath
        self.menu_all_sub_locator = Locators.menu_sub_all_xpath
        self.quality_locator = Locators.quantity_cssSelector
        self.add_cart_locator = Locators.add_cart_cssSelector
        self.add_cart_success_text_locator = Locators.add_cart_success_text_cssSelector
        self.laptop_title_locator = Locators.laptop_title_xpath
        self.laptop_locator = Locators.laptop_cssSelector
        self.calendar_locator = Locators.calendar_xpath
        self.select_month_locator = Locators.select_month_xpath
        self.nextmonth_button_locator = Locators.next_month_button_xpath
        self.select_day_locator = Locators.select_day_xpath

    def menubar_laptop(self):
        menu_laptop = self.driver.find_element(By.XPATH, self.menu_laptop_locator)

        action = ActionChains(self.driver)
        action.move_to_element(menu_laptop).perform()
        self.driver.find_element(By.XPATH, self.menu_all_sub_locator).click()

    def get_laptop_title(self):
        laptop_title = self.driver.find_element(
            By.XPATH, self.laptop_title_locator
        ).text
        return laptop_title

    def click_laptop(self):
        self.driver.find_element(By.CSS_SELECTOR, self.laptop_locator).click()

    def scroll_element(self):
        add_cart_2 = self.driver.find_element(By.CSS_SELECTOR, self.add_cart_locator)
        add_cart_2.location_once_scrolled_into_view

    def calender(self):
        self.driver.find_element(By.XPATH, self.calendar_locator).click()
        time.sleep(1)
        choose_month = self.driver.find_element(By.XPATH, self.select_month_locator)
        month_next_button = self.driver.find_element(
            By.XPATH, self.nextmonth_button_locator
        )

        while choose_month.text != "September 2022":
            month_next_button.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_day_locator).click()
        time.sleep(1)
