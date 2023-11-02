from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import unittest
import time


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):
        url = "https://www.bankrate.com/"
        self.driver.get(url)
        current_url = self.driver.current_url
        print(current_url)
        assert current_url == "https://www.bankrate.com/"


if __name__ == "__main__":
    unittest.main(verbosity=2)
