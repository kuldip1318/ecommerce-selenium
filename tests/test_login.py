from utils.base_test import BaseTest
from utils.data_reader import read_login_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestLogin(BaseTest):

    def test_login_positive(self):
        valid_username = "admin" 
        valid_password = "admin" 
        self._login(valid_username, valid_password)
        try:
            self.assertTrue(self.driver.find_element(By.ID, 'logout2').is_displayed())
            time.sleep(5)
            print("Test Passed: Login successful")
        except IndexError:
            print("Warning: Login data CSV might be empty or missing valid data")

    def test_login_negative(self):
        invalid_username = "invalid_username"
        invalid_password = "invalid_password"
        self._login(invalid_username, invalid_password)
        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            self.assertEqual(alert_text, "Wrong password.")
            print("Test Passed: Alert with expected message displayed")
        except TimeoutException:
            print("Test Failed: Alert not displayed within 5 seconds")


    def _login(self, username, password):
        self.driver.find_element(By.ID, 'login2').click()
        self.driver.find_element(By.ID, 'loginusername').send_keys(username)
        self.driver.find_element(By.ID, 'loginpassword').send_keys(password)
        self.driver.find_element(By.XPATH, '//button[text()="Log in"]').click()
        time.sleep(10)  

