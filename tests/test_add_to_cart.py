from utils.base_test import BaseTest
from utils.data_reader import read_login_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestAddToCart(BaseTest):
    def test_add_to_cart_positive(self):
        time.sleep(5)
        product = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Nokia lumia 1520"))
        )
        time.sleep(5)
        product.click()
        time.sleep(5)
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))
        )
        add_to_cart_button.click()  
        time.sleep(5)

        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert.accept()
        except NoAlertPresentException:
            print("No alert present")

        time.sleep(5)
        cart_link = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cartur"))
        )
        cart_link.click()
        time.sleep(5)

        cart_contents = WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".success"))
        )
        time.sleep(5)
        product_name = "Nokia lumia 1520" 
        assert any(product_name in content.text for content in cart_contents), f"{product_name} not found in Cart"
        time.sleep(5)

    def test_add_to_cart_negative(self):
        time.sleep(5)
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cartur"))
        )
        cart_link.click()
        time.sleep(5)

        cart_contents = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".success"))
        )
        time.sleep(5)


