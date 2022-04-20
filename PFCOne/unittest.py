from lib2to3.pgen2 import driver
import unittest
from regex import B
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class PfcUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "https://pfconenet.herokuapp.com/"
        s = Service('E:\\PFCOneNet\\test\\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_unittest1_login(self):
        self.driver.find_element(By.LINK_TEXT, 'Log in').click()
        self.driver.find_element(By.NAME, "username").send_keys('PFCUser7')
        self.driver.find_element(By.NAME, "password").send_keys('PFCPass7')
        self.driver.find_element(By.XPATH, "/html/body/div/main/div/form/input[3]").click()
        welcomMsg = self.driver.find_element(By.CLASS_NAME, "nav-text").text
        self.assertEqual('Welcome: PFCUser7', welcomMsg)

    def test_unittest2_move_to_fee_menu(self):
        self.driver.find_element(By.LINK_TEXT, "FEE").click()

        self.driver.find_element(By.LINK_TEXT, "Whiteboard").click()
        self.assertEqual("FEE WhiteBoard", self.driver.title)

        self.driver.find_element(By.LINK_TEXT, "Material Datasheets").click()
        self.assertEqual("FEE Material Datasheets", self.driver.title)

        self.driver.find_element(By.LINK_TEXT, "Job Library").click()
        self.assertEqual("FEE Job Library", self.driver.title)

        self.driver.find_element(By.LINK_TEXT, "Presentation & Articles").click()
        self.assertEqual("FEE Presentation&Articles", self.driver.title)

        self.driver.find_element(By.LINK_TEXT, "Job Search").click()
        self.assertEqual("FEE Job Search", self.driver.title)

        self.driver.find_element(By.LINK_TEXT, "Customer Profiles").click()
        self.assertEqual("FEE Customer Profile", self.driver.title)

    def test_unittest3_datasheets(self):
        datasheet_name = "unittest01"
        datasheet_description = "unittest01"

        self.driver.find_element(By.LINK_TEXT, "Material Datasheets").click()
        self.driver.find_element(By.ID, "addBtn").click()
        self.driver.find_element(By.ID, "name").send_keys(datasheet_name)
        self.driver.find_element(By.ID, "description").send_keys(datasheet_description)
        self.driver.find_element(By.ID, "myFile").send_keys("D:\\PFCOneNet\\test\\TestSample.xlsx")
        self.driver.find_element(By.XPATH, "//*[@id='saveAndcancelBtn']/div/button").click()

        datasheet = []
        datasheet_list = self.driver.find_elements(By.XPATH, "/html/body/div/div/div[1]/ul/li/a")

        for option in datasheet_list:
            datasheet.append(option.text)
        self.assertEqual(datasheet_name, datasheet[-1])

    def test_unittest4_customer_profile(self):
        input_text = "unit test"
        self.driver.find_element(By.LINK_TEXT, "Customer Profiles").click()
        self.driver.find_element(By.ID, "addBtn").click()
        self.driver.find_element(By.ID, "customerName").send_keys(input_text)
        self.driver.find_element(By.ID, "genDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "salesDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "camDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "drillDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "processDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "solderDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "processEngDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "assemblyDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "qualityDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "packDesc").send_keys(input_text)
        self.driver.find_element(By.ID, "myFile").send_keys("D:\\PFCOneNet\\test\\TestSample.xlsx")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='saveAndcancelBtn']/div/button").send_keys("\n")

        customer = []
        customer_list = self.driver.find_elements(By.XPATH, "//*[@id='wrapper']/div[1]/ul/li")

        for option in customer_list:
            customer.append(option.text)
        self.assertEqual(input_text, customer[-1])

    def test_unittest5_logout(self):
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        loginBtn = self.driver.find_element(By.LINK_TEXT, "Log in")
        self.assertTrue(loginBtn.is_enabled())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()



