import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from small_project_03.Locators.locator import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.guest_checkout_locator = Locators.guest_checkout_cssSelector
        self.button_account_locator = Locators.button_account_id
        self.step_2_locator = Locators.step_2_xpath
        self.first_name_locator = Locators.first_name_id
        self.last_name_locator = Locators.last_name_id
        self.email_locator = Locators.email_id
        self.telephone_locator = Locators.telephone_id
        self.company_locator = Locators.company_id
        self.address_1_locator = Locators.address_1_id
        self.address_2_locator = Locators.address_2_id
        self.city_locator = Locators.city_id
        self.postcode_locator = Locators.postcode_id
        self.country_locator = Locators.country_id
        self.zone_locator = Locators.zone_id
        self.shipping_check_box_locator = Locators.shipping_check_box_name
        self.continue_button_01_locator = Locators.continue_button_01_id
        self.continue_button_step_04_locator = Locators.continue_button_step_04_id
        self.continue_button_step_05_locator = Locators.continue_button_step_05_id
        self.continue_button_step_06_locator = Locators.continue_button_step_06_id
        self.continue_button_last_locator = Locators.continue_button_last_xpath
        self.terms_check_box_locator = Locators.terms_check_box_xpath
        self.checkout_success_text_locators = Locators.checkout_success_text_xpath

    def new_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.guest_checkout_locator).click()
        self.driver.find_element(By.ID, self.button_account_locator).click()

    def scroll_screen(self):
        step_2 = self.driver.find_element(By.XPATH, self.step_2_locator)
        step_2.location_once_scrolled_into_view
        time.sleep(2)

    def input_first_name(self, fname):
        first_name = self.driver.find_element(By.ID, self.first_name_locator)
        first_name.click()
        first_name.send_keys(fname)

    def input_last_name(self, lname):
        last_name = self.driver.find_element(By.ID, self.last_name_locator)
        last_name.click()
        last_name.send_keys(lname)

    def input_email(self, email):
        emailAdress = self.driver.find_element(By.ID, self.email_locator)
        emailAdress.click()
        emailAdress.send_keys(email)

    def input_telephone(self, telephone):
        telephoneElem = self.driver.find_element(By.ID, self.telephone_locator)
        telephoneElem.click()
        telephoneElem.send_keys(telephone)

    def input_company(self, company):
        companyElem = self.driver.find_element(By.ID, self.company_locator)
        companyElem.click()
        companyElem.send_keys(company)

    def input_address_1(self, address1):
        address_1 = self.driver.find_element(By.ID, self.address_1_locator)
        address_1.click()
        address_1.send_keys(address1)

    def input_address_2(self, address2):
        address_2 = self.driver.find_element(By.ID, self.address_2_locator)
        address_2.click()
        address_2.send_keys(address2)

    def input_city(self, city):
        cityElem = self.driver.find_element(By.ID, self.city_locator)
        cityElem.click()
        cityElem.send_keys(city)

    def input_postcode(self, postcode):
        postcodeElem = self.driver.find_element(By.ID, self.postcode_locator)
        postcodeElem.click()
        postcodeElem.send_keys(postcode)

    def input_country_id(self, country_id):
        countryElem = self.driver.find_element(By.ID, self.country_locator)
        dropdown_1 = Select(countryElem)
        dropdown_1.select_by_value(country_id)
        time.sleep(2)

    def input_zone_id(self, zone_id):
        zoneElem = self.driver.find_element(By.ID, self.zone_locator)
        dropdown_2 = Select(zoneElem)
        dropdown_2.select_by_visible_text(zone_id)

    def shipping_check_box(self):
        shipping_check_box = self.driver.find_element(By.NAME, self.shipping_check_box_locator)
        if shipping_check_box.is_selected:
            pass
        else:
            shipping_check_box.click()

    def continue_button(self):
        self.driver.find_element(By.ID, self.continue_button_01_locator).click()
        time.sleep(1)

    def continue_button2(self):
        self.driver.find_element(By.ID, self.continue_button_step_04_locator).click()
        time.sleep(1)

    def continue_button3(self):
        self.driver.find_element(By.XPATH, self.terms_check_box_locator).click()
        self.driver.find_element(By.ID, self.continue_button_step_05_locator).click()
        time.sleep(1)

    def continue_button4(self):
        self.driver.find_element(By.ID, self.continue_button_step_06_locator).click()
        time.sleep(1)

    def check_order(self):
        success_text = self.driver.find_element(By.XPATH, self.checkout_success_text_locators).text
        return success_text

    def continue_button5(self):
        self.driver.find_element(By.XPATH, self.continue_button_last_locator).click()

