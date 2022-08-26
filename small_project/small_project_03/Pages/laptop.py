import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from small_project_03.Locators.locator import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LaptopPage():
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
        self.go_to_cart_locator = Locators.go_to_cart_xpath
        self.checkout_button_locator = Locators.checkout_button_xpath
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

    def menubar_laptop(self):
        menu_laptop = self.driver.find_element(By.XPATH, self.menu_laptop_locator)

        action = ActionChains(self.driver)
        action.move_to_element(menu_laptop).perform()
        self.driver.find_element(By.XPATH, self.menu_all_sub_locator).click()

    def get_laptop_title(self):
        laptop_title = self.driver.find_element(By.XPATH, self.laptop_title_locator).text
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
        month_next_button = self.driver.find_element(By.XPATH, self.nextmonth_button_locator)

        while(choose_month.text != 'September 2022'):
            month_next_button.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_day_locator).click()
        time.sleep(2)

    def checkout(self):
        self.driver.find_element(By.XPATH, self.go_to_cart_locator).click()
        self.driver.find_element(By.XPATH, self.checkout_button_locator).click()

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
        telephone.send_keys(telephone)

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
