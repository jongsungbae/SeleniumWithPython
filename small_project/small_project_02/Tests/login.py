import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import HtmlTestRunner
from small_project_02.Pages.homePage import HomePage
from small_project_02.Pages.loginPage import LoginPage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseUrl= 'https://opensource-demo.orangehrmlive.com/'
        s = Service('../../driver/chromedriver.exe')

        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_01_login_page(self):
        driver = self.driver
        login = LoginPage(driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

    def test_02_logout(self):
        driver = self.driver
        logout = HomePage(driver)
        logout.click_welcome()
        logout.click_logout()

        time.sleep(2)

    def test_03_login_page_invalid(self):
        driver = self.driver
        login = LoginPage(driver)

        login.enter_username("test")
        login.enter_password("test")
        login.click_login()
        self.assertEqual(login.invalid_login(), "Invalid credentials")


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('Test Completed')

if __name__ == "__main__":
    unittest.main()