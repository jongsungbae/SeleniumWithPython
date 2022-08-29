import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from small_project_03.Pages.global_page import GlobalPage
from small_project_03.Pages.phone import PhonePage
from small_project_03.Pages.laptop import LaptopPage
from small_project_03.Pages.checkout_page import CheckoutPage

class EcommerceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseUrl= 'http://tutorialsninja.com/demo/'
        s = Service('../../driver/chromedriver.exe')

        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    @unittest.skip("demonstrating skipping")
    def test_01_iphone(self):
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


    def test_02_laptop(self):
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
        time.sleep(2)

    def test_03_checkout(self):
        global_page = GlobalPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # checkout
        global_page.checkout()

        # New customer
        checkout_page.new_customer()

        # scroll screen to billing details
        checkout_page.scroll_screen()

        # input personal information
        checkout_page.input_first_name("test123")
        checkout_page.input_last_name("test456")
        checkout_page.input_email("test@test.com")
        checkout_page.input_telephone("123-456-789")
        checkout_page.input_company("selenium test")
        checkout_page.input_address_1("test 12345")
        checkout_page.input_address_2("test 45678")
        checkout_page.input_city("Toronto")
        checkout_page.input_postcode("AAA BBB")
        checkout_page.input_country_id("38")
        checkout_page.input_zone_id("Ontario")
        checkout_page.shipping_check_box()

        checkout_page.continue_button()
        checkout_page.continue_button2()
        checkout_page.continue_button3()
        checkout_page.continue_button4()


        checkout_page.check_order()
        order_success_text = "Your order has been placed!"
        self.assertEqual(checkout_page.check_order(), order_success_text)

        checkout_page.continue_button5()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('Test Completed')

if __name__ == "__main__":
    unittest.main()