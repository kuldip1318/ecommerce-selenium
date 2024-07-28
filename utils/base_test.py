
from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # or use any other browser driver
        self.driver.get("https://www.demoblaze.com/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
