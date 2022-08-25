import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest

from selenium.webdriver.support.select import Select

from small_project_02.Pages.homePage import HomePage
from small_project_02.Pages.loginPage import LoginPage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseUrl= 'http://tutorialsninja.com/demo/'
        s = Service('../../driver/chromedriver.exe')

        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_iphone(self):
        menu_phone = self.driver.find_element(By.LINK_TEXT, "Phones & PDAs")
        menu_phone.click()

        iphone = self.driver.find_element(By.LINK_TEXT, "iPhone")
        iphone.click()

        first_picture = self.driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
        first_picture.click()
        time.sleep(2)

        # screenshot 고민!!!!! => IF ELSE 돌리면 될거 같음
        right_arrow_button = self.driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')
        for i in range(0, 5):
            self.driver.save_screenshot(f'screenshot_iphone_#{i}.png')
            right_arrow_button.click()
            time.sleep(2)



        self.driver.find_element(By.CSS_SELECTOR, 'button[class="mfp-close"]').click()

        # modify Qty
        quantity = self.driver.find_element(By.CSS_SELECTOR, 'input[id="input-quantity"]')
        quantity.click()
        quantity.clear()
        quantity.send_keys('2')
        time.sleep(2)

        # add cart
        add_cart = self.driver.find_element(By.CSS_SELECTOR, 'button[id="button-cart"]')
        add_cart.click()

        # assert 확인하는 것이 좋겠음

    def test_laptop(self):
        # move to laptop section
        menu_laptop = self.driver.find_element(By.XPATH, '//a[text()="Laptops & Notebooks"]')
        menu_sub_all = self.driver.find_element(By.XPATH, '//a[text()="Show All Laptops & Notebooks"]')

        action = ActionChains(self.driver)
        action.move_to_element(menu_laptop).perform()
        menu_sub_all.click()

        # title 확인
        laptop_title = self.driver.find_element(By.XPATH, '//div[@id="content"]/h2').text
        laptop_title_content = "Laptops & Notebooks"
        self.assertEqual(laptop_title, laptop_title_content)

        # laptop click
        selected_laptop = self.driver.find_element(By.XPATH, '//a[text()="HP LP3065"]')
        selected_laptop.click()

        # scroll element until 'add to cart'
        add_cart_2 = self.driver.find_element(By.CSS_SELECTOR, 'button[id="button-cart"]')
        add_cart_2.location_once_scrolled_into_view
        time.sleep(1)

        # # select delivery date
        # calendar_button = self.driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
        # calendar_button.click()
        # time.sleep(1)

        choose_month = self.driver.find_element(By.XPATH, '//th[@class="picker-switch"]')
        month_next_button = self.driver.find_element(By.XPATH, '//th[@class="next"]')


        # while(choose_month.text != 'September 2022'):
        #     month_next_button.click()
        # time.sleep(2)
        #
        # day = self.driver.find_element(By.XPATH, '//td[text()="26"]')
        # time.sleep(2)
        # day.click()

        quantity = self.driver.find_element(By.CSS_SELECTOR, 'input[id="input-quantity"]')
        quantity.click()
        quantity.clear()
        quantity.send_keys('2')

        # add cart
        add_cart = self.driver.find_element(By.CSS_SELECTOR, 'button[id="button-cart"]')
        add_cart.click()

        # checkout
        co_to_cart_button = self.driver.find_element(By.XPATH, '//span[@id="cart-total"]')
        co_to_cart_button.click()
        checkout_button = self.driver.find_element(By.XPATH, '//p[@class="text-right"]/a[2]')
        checkout_button.click()



        # New customer
        guest_checkout = self.driver.find_element(By.CSS_SELECTOR, 'input[value="guest"]')
        guest_checkout.click()
        self.driver.find_element(By.ID, 'button-account').click()

        # scroll screen to billing details
        step_2 = self.driver.find_element(By.XPATH, '//a[text()="Step 2: Billing Details "]')
        step_2.location_once_scrolled_into_view
        time.sleep(2)


        # personal details
        first_name = self.driver.find_element(By.ID, 'input-payment-firstname')
        last_name = self.driver.find_element(By.ID, 'input-payment-lastname')
        email = self.driver.find_element(By.ID, 'input-payment-email')
        telephone = self.driver.find_element(By.ID, 'input-payment-telephone')
        company = self.driver.find_element(By.ID, 'input-payment-company')
        address_1 = self.driver.find_element(By.ID, 'input-payment-address-1')
        address_2 = self.driver.find_element(By.ID, 'input-payment-address-2')
        city = self.driver.find_element(By.ID, 'input-payment-city')
        postcode = self.driver.find_element(By.ID, 'input-payment-postcode')
        country_id = self.driver.find_element(By.ID, 'input-payment-country')
        zone_id = self.driver.find_element(By.ID, 'input-payment-zone')
        shipping_check_box = self.driver.find_element(By.NAME, 'shipping_address')
        continue_button = self.driver.find_element(By.ID, 'button-guest')

        first_name.click()
        first_name.send_keys('Jongsung')
        last_name.click()
        last_name.send_keys('Bae')
        email.click()
        email.send_keys('jongsung.jay@gmail.com')
        telephone.click()
        telephone.send_keys('4379901770')
        company.click()
        company.send_keys(' ')
        address_1.click()
        address_1.send_keys('45 hendon ave')
        address_2.click()
        address_2.send_keys('')
        city.click()
        city.send_keys('north york')
        postcode.click()
        postcode.send_keys('M2M 1A4')
        time.sleep(2)

        dropdown_1 = Select(country_id)
        dropdown_1.select_by_value("38")
        time.sleep(2)

        dropdown_2 = Select(zone_id)
        dropdown_2.select_by_visible_text("Ontario")

        self.assertTrue(shipping_check_box.is_selected())
        time.sleep(3)
        continue_button.click()

        # step4
        continue_button_02 = self.driver.find_element(By.ID, 'button-shipping-method')
        continue_button_02.click()

        # step5
        terms_check_box = self.driver.find_element(By.XPATH, '//input[@name="agree"]')
        terms_check_box.click()

        continue_button_03 = self.driver.find_element(By.ID, 'button-payment-method')
        continue_button_03.click()

        # step6
        continue_button_04 = self.driver.find_element(By.ID, 'button-confirm')
        continue_button_04.click()

        # check - Fail => check again
        success_text = self.driver.find_element(By.XPATH, '//div[@class="col-sm-12"]/h1')
        print(success_text.text)
        order_success_text = "Your order has been placed!"
        self.assertEqual(success_text, order_success_text)

        continue_button_05 = self.driver.find_element(By.XPATH, '//div[@class="pull-right"]/a')
        continue_button_05.click()
























    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('Test Completed')

if __name__ == "__main__":
    unittest.main()