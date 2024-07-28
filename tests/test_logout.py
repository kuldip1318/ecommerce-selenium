from utils.base_test import BaseTest
from utils.data_reader import read_login_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestLogout(BaseTest):

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
        self.driver.find_element(By.ID, 'logout2').click()
        time.sleep(5)

    def _login(self, username, password):
        self.driver.find_element(By.ID, 'login2').click()
        self.driver.find_element(By.ID, 'loginusername').send_keys(username)
        self.driver.find_element(By.ID, 'loginpassword').send_keys(password)
        self.driver.find_element(By.XPATH, '//button[text()="Log in"]').click()
        time.sleep(10)  

