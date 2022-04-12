import time
import unittest, xlrd
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
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
    def test_A_createSurvey_move(self,username,password):
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        username1 = self.driver.find_element(By.NAME, 'username')
        password1 = self.driver.find_element(By.NAME, 'password')
        signInBtn = self.driver.find_element(By.CLASS_NAME, 'signinBtn')

        username1.send_keys(username)
        password1.send_keys(password)
        self.assertTrue(signInBtn.is_enabled())
        signInBtn.send_keys("\n")

        WebDriverWait(self.driver, 10).until(expected_conditions.title_contains("Home"))
        self.driver.find_element(By.LINK_TEXT, "Create Survey").click()
        self.assertTrue('Survey', self.driver.title)

    def test_B_creteSurvey(self):
        self.driver.find_element(By.NAME, 'startDate').send_keys('03312022')
        self.driver.find_element(By.NAME, 'endDate').send_keys('04302022')
        self.driver.find_element(By.ID, 'surveyTextField').send_keys('test survey for automation')
        self.driver.find_element(By.ID, 'addQues').click()
        self.driver.find_element(By.NAME, 'question1').send_keys('question01 for automation')

        exp_options = ['Select Type', 'Single Textbox', 'Multiple Choice']
        act_options = []
        select_list = Select(self.driver.find_element(By.NAME, 'question1type'))
        # check number of options in dropdown
        self.assertEqual(3, len(select_list.options))
        # get options in a list
        for option in select_list.options:
            act_options.append(option.text)
        # check expected options list with actual options list
        self.assertEqual(exp_options, act_options)
        # check default selected option is "Select Type"
        self.assertEqual("Select Type", select_list.first_selected_option.text)

        select_list.select_by_visible_text('Single Textbox')
        self.driver.find_element(By.ID, 'createSurvey').send_keys("\n")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


