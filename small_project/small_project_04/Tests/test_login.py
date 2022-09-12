import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from small_project_04.Pages.indexPage import IndexPage
from small_project_04.Pages.loginPage import LoginPage
from small_project_04.Pages.myaccountPage import MyAccountPage
from small_project_04.Pages.searchResultPage import SearchResultPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseUrl = "http://automationpractice.com/index.php"
        s = Service("../../driver/chromedriver.exe")

        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_01_validate_indexPage(self):
        global indexPage
        indexPage = IndexPage(self.driver)

        indexPage.indexPage_validate()

    def test_02_logIn(self):
        indexPage.signin_button.click()

        global loginPage
        loginPage = LoginPage(self.driver)

        loginPage.loginPage_validate()

        # input user info
        loginPage.login("test_ecommerce@test.com", "test123!")

    def test_03_my_account(self):
        global myAccountPage
        myAccountPage = MyAccountPage(self.driver)

        myAccountPage.my_account_validate()
        time.sleep(1)
        # myAccountPage.wishlist_click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
