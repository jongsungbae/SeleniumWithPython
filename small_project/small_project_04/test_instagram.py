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


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('Test Completed')

if __name__ == "__main__":
    unittest.main()