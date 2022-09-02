import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import HtmlTestRunner


class GoogleSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseUrl = "https://google.com"
        s = Service("../driver/chromedriver.exe")

        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_search_keyword_01(self):
        global search_bar, search_button
        self.driver.find_element(By.NAME, "q").send_keys("Automation step by step")
        self.driver.find_element(By.NAME, "btnK").click()
        time.sleep(2)

    def test_search_keyword_02(self):
        self.driver.find_element(By.NAME, "q").clear()
        time.sleep(2)
        self.driver.find_element(By.NAME, "q").send_keys("Selenium")
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit").click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
