import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from small_project_03.Pages.global_page import GlobalPage
from small_project_03.Pages.phone import PhonePage
from small_project_03.Pages.laptop import LaptopPage

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
        iphone = PhonePage(self.driver)
        global_page = GlobalPage(self.driver)

        iphone.menubar_phone()
        self.assertEqual("Phones & PDAs", iphone.get_phone_title())

        iphone.click_iphone()
        iphone.click_iphone_picture()
        iphone.right_arrow_picture()

        # modify Qty
        global_page.input_quantity("2")

        # add cart
        global_page.add_cart()
        self.assertTrue("Success: You have added" in global_page.add_cart())


    def test_laptop(self):
        # move to laptop section
        laptop = LaptopPage(self.driver)
        global_page = GlobalPage(self.driver)

        laptop.menubar_laptop()

        # check title
        laptop_title_content = "Laptops & Notebooks"
        self.assertEqual(laptop.get_laptop_title(), laptop_title_content)

        # laptop click
        laptop.click_laptop()

        # scroll element until 'add to cart'
        laptop.scroll_element()
        time.sleep(1)

        # select delivery date
        laptop.calender()

        # select Qty
        global_page.input_quantity("2")

        # add cart
        global_page.add_cart()
        self.assertTrue("Success: You have added" in global_page.add_cart())

        # checkout
        laptop.checkout()

        # New customer
        laptop.new_customer()

        # scroll screen to billing details
        laptop.scroll_screen()

        # input personal information
        laptop.input_first_name("test123")
        laptop.input_last_name("test456")
        laptop.input_email("test@test.com")
        laptop.input_telephone("123-456-789")
        laptop.input_company("selenium test")
        laptop.input_address_1("test 12345")
        laptop.input_address_2("test 45678")
        laptop.input_city("Toronto")
        laptop.input_postcode("AAA BBB")
        laptop.input_country_id("38")
        laptop.input_zone_id("Ontario")
        laptop.shipping_check_box()

        self.assertTrue(laptop.shipping_check_box().is_selected())

        laptop.continue_button()
        laptop.continue_button2()
        laptop.continue_button3()
        laptop.continue_button4()


        laptop.check_order()
        order_success_text = "Your order has been placed!"
        self.assertEqual(laptop.check_order(), order_success_text)

        laptop.continue_button5()


























    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('Test Completed')

if __name__ == "__main__":
    unittest.main()