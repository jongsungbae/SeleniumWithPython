import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class InstagramTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseUrl= 'http://instagram.com/'
        s = Service('../driver/chromedriver.exe')

        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_01_login(self, username, pwd):
        user_name = self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        password = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        login_button = self.driver.find_element(By.XPATH, '//div/button/div')

        # accepting cookies
        try:
            cookies_accept = self.driver.find_element(By.XPATH, '//button[text()="Accept]')
            cookies_accept.click()
        except:
            pass

        user_name.click()
        user_name.send_keys(username)
        password.click()
        password.send_keys(pwd)
        login_button.click()

        # credential storage
        try:
            credentials = self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')
            credentials.click()
        except:
            pass

        # notifications
        try:
            notification = self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')
            notification.click()
        except:
            pass

    def test_02_follow_like_comment(self):
        profile_list = ['duck._lover', 'rabbit._lover']
        comments = ['so cute!', 'cutie', 'very sweet!', 'nice!', 'love it', 'looks very special']

        search_bar = self.driver.find_element(By.XPATH, '//span[text()="Search"]')
        input_text = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "Search"]')

        search_bar.click()
        time.sleep(1)
        input_text.send_keys(profile_list[0])

        # input Enter key two times
        count = 0
        while count <3:
            input_text.send_keys(Keys.Enter)
            count += 1
            time.sleep(1)



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('Test Completed')

if __name__ == "__main__":
    unittest.main()