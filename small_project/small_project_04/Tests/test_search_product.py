import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from small_project_04.Pages.loginPage import LoginPage
from small_project_04.Pages.indexPage import IndexPage
from small_project_04.Pages.orderPaymentMethodPage import OrderPaymentMethodPage
from small_project_04.Pages.orderShippingPage import OrderShippingPage
from small_project_04.Pages.orderSummaryPage import OrderSummaryPage
from small_project_04.Pages.searchResultPage import SearchResultPage
from small_project_04.Pages.productContentPage import SearchContentPage
from small_project_04.Pages.orderPage import OrderPage
from small_project_04.Pages.orderAddressPage import OrderAddressPage


class SearchProductTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseUrl = "http://automationpractice.com/index.php"
        s = Service("../../driver/chromedriver.exe")

        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_01_validate_indexPage(self):
        global indexPage
        indexPage = IndexPage(self.driver)
        indexPage.indexPage_validate()

    def test_02_input_search_product(self):
        search_text = "t-shirts"
        indexPage.input_search_product(search_text)

    def test_03_validate_search_result(self):
        global searchResultPage
        searchResultPage = SearchResultPage(self.driver)

        searchResultPage.searchResultPage_validate()
        searchResultPage.click_search_image()

    def test_04_validate_content_page(self):
        global contentPage
        contentPage = SearchContentPage(self.driver)
        contentPage.searchResultPage_validate()

    def test_05_search_result(self):
        contentPage.select_quantity("3")
        # contentPage.select_size()
        contentPage.select_color()
        contentPage.add_to_cart()

    def test_06_validate_order_page(self):
        global orderPage
        orderPage = OrderPage(self.driver)

        orderPage.searchResultPage_validate()

    def test_07_check_price(self):
        orderPage.check_price()
        orderPage.checkout_button()

        loginPage = LoginPage(self.driver)
        # input user info
        loginPage.login("test_ecommerce@test.com", "test123!")

    def test_08_address_page(self):
        global orderAddressPage
        orderAddressPage = OrderAddressPage(self.driver)
        orderAddressPage.checkout_button()

    def test_09_shipping_page(self):
        global orderShippingPage
        orderShippingPage = OrderShippingPage(self.driver)
        orderShippingPage.shipping_page()

    def test_10_payment_method_page(self):
        global order_payment_method
        order_payment_method = OrderPaymentMethodPage(self.driver)
        order_payment_method.payment_page()

    def test_11_validate_order_message(self):
        global order_summary
        order_summary = OrderSummaryPage(self.driver)
        order_summary.order_confirm_page()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
