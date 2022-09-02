import time


from selenium.webdriver.common.by import By
from small_project_04.Locators.locator import Locators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = self.driver.find_element(By.ID, Locators.orderpage_title_id).text
        self.unitprice = self.driver.find_element(By.XPATH, Locators.orderpage_unitprice_xpath).text
        self.qty = self.driver.find_element(By.CSS_SELECTOR, Locators.orderpage_qty_cssSelector).get_attribute("value")
        self.total_product_price = self.driver.find_element(By.ID, Locators.orderpage_total_product_price_id).text
        self.shipping_fee = self.driver.find_element(By.ID, Locators.orderpage_shipping_fee_id).text
        self.totalPrice = self.driver.find_element(By.ID, Locators.orderpage_total_price_id).text
        self.checkout_button = self.driver.find_element(By.CSS_SELECTOR, Locators.orderpage_checkout_button_cssSelector)

    def searchResultPage_validate(self):
        assert "SHOPPING-CART SUMMARY" in self.title

    def check_price(self):
        unit_price = float(self.unitprice.strip("$"))
        quantity = int(self.qty)
        total_product_price = float(self.total_product_price.strip("$"))
        shipping_fee = float(self.shipping_fee.strip("$"))
        total_price = float(self.totalPrice.strip("$"))

        assert unit_price * quantity == total_product_price
        assert total_price == unit_price * quantity + shipping_fee








