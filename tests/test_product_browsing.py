from utils.base_test import BaseTest
from utils.data_reader import read_login_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class TestProducts(BaseTest):
    def test_products_list(self):
        products = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card"))
        )
        time.sleep(5)
        assert len(products) > 0, "Products are not displayed on the homepage"
        print("Test passed: Products are displayed on the homepage")

    def test_product_category(self):
        self.assertTrue(self.driver.find_element(By.ID, 'itemc').is_displayed())
        time.sleep(5)

    def test_products_next(self):
        time.sleep(5)

        next_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
        )
        next_button.click()
        time.sleep(5)
        products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card"))
        )

        last_product = products[-1]
        last_product.click()
        time.sleep(5)
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))
        )

        add_to_cart_button.click()
        time.sleep(5)
        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            self.assertEqual(alert_text, "Product added")
            print("Test Passed: Alert with expected message displayed")
        except TimeoutException:
            print("Test Failed: Alert not displayed within 5 seconds")
