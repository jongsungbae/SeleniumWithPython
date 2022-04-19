import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class PfcUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "https://pfconenet.herokuapp.com/"
        s = Service('D:\\PFCOneNet\\test\\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def setUp(self):
        logInBtn = self.driver.find_element(By.LINK_TEXT, 'Log in')
        logInBtn.click()
        self.driver.find_element(By.NAME, "username").send_keys('PFCUser7')
        self.driver.find_element(By.NAME, "password").send_keys('PFCPass7')
        self.driver.find_element(By.XPATH, "/html/body/div/main/div/form/input[3]").click()

    def test_unittest1(self):
        welcomMsg = self.driver.find_element(By.CLASS_NAME, "nav-text").text
        self.assertEqual('Welcome: PFCUser7', welcomMsg)
        print("unittest_login_success")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()



