import time
import unittest, xlrd
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@ddt
class SignInTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "https://tech-army-survey.herokuapp.com/"
        s = Service('D:\SeleniumProject\driver_100\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)

        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    @data(('test01', 'test01'))
    @unpack
    def test_createSurvey_move(self, username, password):
        self.driver.find_element(By.LINK_TEXT, "Create Survey").click()
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, 'signinBtn').click()

        WebDriverWait(self.driver, 10).until(expected_conditions.title_contains("Home"))
        self.driver.find_element(By.LINK_TEXT, "Create Survey").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


