from behave import *
from selenium.webdriver.common.by import By
from tests.acceptance.locators.home_page import HomePageLocators
use_step_matcher('re')

@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    blog_link = context.driver.find_element(By.ID, link_id)
    blog_link.click()
