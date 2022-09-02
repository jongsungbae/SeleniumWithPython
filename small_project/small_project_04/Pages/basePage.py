from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    def __init__(self, driver):
        self.driver = driver
