from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.create_account_title = self.driver.find_element(
            By.XPATH, Locators.create_account_title_xpath
        ).text
        self.gender1 = self.driver.find_element(
            By.ID, Locators.create_account_gender1_id
        )
        self.gender2 = self.driver.find_element(
            By.ID, Locators.create_account_gender2_id
        )
        self.first_name = self.driver.find_element(
            By.ID, Locators.create_account_firstName_id
        )
        self.last_name = self.driver.find_element(
            By.ID, Locators.create_account_lastName_id
        )
        self.password = self.driver.find_element(
            By.ID, Locators.create_account_password_id
        )
        self.address = self.driver.find_element(
            By.ID, Locators.create_account_address1_id
        )
        self.city = self.driver.find_element(By.ID, Locators.create_account_city_id)
        self.postcode = self.driver.find_element(
            By.ID, Locators.create_account_postcode_id
        )
        self.state = self.driver.find_element(By.ID, Locators.create_account_state_id)
        self.phone = self.driver.find_element(
            By.ID, Locators.create_account_phone_mobile_id
        )
        self.submitbutton = self.driver.find_element(
            By.ID, Locators.create_account_submit_button_id
        )

    def createPage_validate(self):
        assert self.create_account_title == "CREATE AN ACCOUNT"
        assert self.gender1.is_enabled()
        assert self.gender2.is_enabled()
        assert self.first_name.is_enabled()
        assert self.last_name.is_enabled()
        assert self.password.is_enabled()
        assert self.address.is_enabled
        assert self.city.is_enabled()
        assert self.postcode.is_enabled()
        assert self.state.is_enabled()
        assert self.phone.is_enabled
        assert self.submitbutton.is_enabled

    def create_name(self, first_name, last_name):
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)

    def create_password(self, password):
        self.password.send_keys(password)
