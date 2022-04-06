import unittest, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SignUpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "https://tech-army-survey.herokuapp.com/"
        s = Service('E:\\selenium\\drivers\\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_check_A_cancelBtn(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Sign Up").click()
        self.assertEqual("Sign Up", driver.title)
        cancelBtn = self.driver.find_element(By.ID, 'registerCancel')
        self.assertTrue(cancelBtn.is_enabled())
        cancelBtn.click()
        self.assertEqual('Home', driver.title)
        driver.find_element(By.LINK_TEXT, "Sign Up").click()

    def test_check_B_linkBtn(self):
        driver = self.driver
        signInLink = self.driver.find_element(By.LINK_TEXT, 'or Sign in here')
        self.assertTrue(signInLink.is_displayed())
        signInLink.click()
        self.assertEqual('Sign In', driver.title)
        driver.back()
        self.assertEqual('Sign Up', driver.title)

    def test_create_account(self):
        name = self.driver.find_element(By.NAME, 'username')
        password = self.driver.find_element(By.NAME, 'password')
        email = self.driver.find_element(By.NAME, 'email')
        createBtn = self.driver.find_element(By.ID, 'registerCreate')
        self.assertTrue(name.is_displayed())
        self.assertTrue(password.is_displayed())
        self.assertTrue(email.is_displayed())
        self.assertTrue(createBtn.is_enabled())

        name.send_keys('test999')
        password.send_keys('test999')
        email.send_keys('test999@test.com')
        createBtn.click()
        time.sleep(2)

        checkID = self.driver.find_element(By.ID, 'dropbtn').text
        self.assertEqual('test999', checkID)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
