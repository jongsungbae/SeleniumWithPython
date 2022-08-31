import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from small_project_04.Pages.indexPage import IndexPage
from small_project_04.Pages.loginPage import LoginPage
from small_project_04.Pages.createAccountPage import CreateAccountPage
from small_project_04.Pages.myaccountPage import MyAccountPage


class MyStoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseUrl= 'http://automationpractice.com/index.php'
        s = Service('../../driver/chromedriver.exe')

        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_01_logIn_click(self):
        indexPage = IndexPage(self.driver)
        indexPage.signin_button.click()

        loginPage = LoginPage(self.driver)
        loginPage.loginPage_validate()
        loginPage.click_create_account(loginPage.randomEmail())
        
    def test_02_validate(self):
        createPage = CreateAccountPage(self.driver)

        createPage.createPage_validate()



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('Test Completed')

if __name__ == "__main__":
    unittest.main()