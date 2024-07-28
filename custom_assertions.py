import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CustomAssertions(unittest.TestCase):
    def assertAlertText(self, driver, expected_text):
        try:
            alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            if alert_text != expected_text:
                self.fail(f"Alert text did not match. Expected: '{expected_text}', Got: '{alert_text}'")
            else:
                print("Test Passed: Alert with expected message displayed")
        except TimeoutException:
            self.fail("Alert not displayed within 5 seconds")