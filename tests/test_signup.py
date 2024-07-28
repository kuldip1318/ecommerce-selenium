from utils.base_test import BaseTest
from utils.data_reader import read_login_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from custom_assertions import CustomAssertions
import time

class TestSignup(BaseTest, CustomAssertions):
    def test_signup_positive(self):
        # Sign up successful.
        validusername = "qweasdzxc454"
        validpassword = "qweasdzxc454"
        self._signup(validusername, validpassword)
        self.assertAlertText(self.driver, "Sign up successful.")

    def test_signup_negative(self):
        # This user already exist.
        invalidusername = "admin"
        invalidpassword = "admin"
        self._signup(invalidusername, invalidpassword)
        self.assertAlertText(self.driver, "This user already exist.")

    def _signup(self, username, password):
        self.driver.find_element(By.ID, 'signin2').click()
        self.driver.find_element(By.ID, 'sign-username').send_keys(username)
        self.driver.find_element(By.ID, 'sign-password').send_keys(password)
        self.driver.find_element(By.XPATH, '//button[text()="Sign up"]').click()
        time.sleep(10)