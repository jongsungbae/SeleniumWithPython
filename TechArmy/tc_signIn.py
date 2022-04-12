import unittest, xlrd

from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#pip install xlrd==1.2.0

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

    def test_check_A_linkBtn(self):
        self.driver.find_element(By.LINK_TEXT, 'Sign In').click()
        signUp_link = self.driver.find_element(By.LINK_TEXT, 'or Sign up here')
        self.assertTrue(signUp_link.is_displayed())
        signUp_link.click()
        self.assertEqual('Sign Up', self.driver.title)
        self.driver.back()
        self.assertEqual('Sign In', self.driver.title)

    @data(('test999','test999'))
    @unpack
    def test_login(self, username, password):
        username1 = self.driver.find_element(By.NAME, 'username')
        password1 = self.driver.find_element(By.NAME, 'password')
        signInBtn = self.driver.find_element(By.CLASS_NAME, 'signinBtn')

        username1.send_keys(username)
        password1.send_keys(password)
        signInBtn.click()

        checkID = self.driver.find_element(By.ID, 'dropbtn').text
        self.assertEqual(username, checkID)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()



