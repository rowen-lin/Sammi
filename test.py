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
        url = "https://develop.roo.cash/"
        self.driver.get(url)
        # self.driver.maximize_window()
        self.driver.set_window_size(430, 932)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()

    # def test_open_page(self):
    #     current_url = self.driver.current_url
    #     print(current_url)
    #     assert current_url == "https://develop.roo.cash/"

    # def test_header_roomy(self):
    #     roomy = self.driver.find_element(By.ID, "link-roomy").click()
    #     current_url = self.driver.current_url
    #     assert current_url == "https://develop.roo.cash/community/roomy"

    # def test_header_product_wording(self):
    #     time.sleep(3)
    #     product_tab = self.driver.find_element(
    #         By.XPATH, "//*[@id='nav-content']/ul/li[2]"
    #     )
    #     product_tab.click()
    #     time.sleep(1)
    #     arr = self.driver.find_elements(By.ID, "myToggler")
    #     result = arr[0].text.splitlines()
    #     expected = ["全台信用卡", "信用貸款", "小額借款", "房屋貸款", "數位帳戶", "證券帳戶"]
    #     assert result == expected

    def test_header_product_link_all_creditcard(self):
        self.driver.refresh()
        time.sleep(3)
        product_tab = self.driver.find_element(
            By.XPATH, "//*[@id='nav-content']/ul/li[2]"
        )
        product_tab.click()
        time.sleep(1)

        all_creditcard = self.driver.find_elements(By.XPATH, "//*[@id='link-list']")[0]
        # print("all credit", all_creditcard.text)
        ActionChains(self.driver).move_to_element(all_creditcard).click(
            all_creditcard
        ).perform()
        current_url = self.driver.current_url
        assert current_url == "https://develop.roo.cash/creditcard"

    def test_header_product_link_personal_loan(self):
        self.driver.refresh()
        time.sleep(3)
        burger = self.driver.find_element(By.ID, "btn-nav")
        if burger:
            burger.click()
        product_tab = self.driver.find_element(
            By.XPATH, "//*[@id='nav-content']/ul/li[2]"
        )
        product_tab.click()
        time.sleep(1)

        all_creditcard = self.driver.find_elements(By.XPATH, "//*[@id='link-list']")[1]
        # print("all credit", all_creditcard.text)
        ActionChains(self.driver).move_to_element(all_creditcard).click(
            all_creditcard
        ).perform()
        current_url = self.driver.current_url
        assert current_url == "https://develop.roo.cash/personal-loan"


if __name__ == "__main__":
    unittest.main(verbosity=2)
