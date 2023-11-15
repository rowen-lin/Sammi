from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from pages.page import Page


class Header(Page):
    PRODUCT_TITLE = (By.XPATH, "//*[@id='nav-content']/ul/li[2]")
    PRODUCT_SPAN = (By.XPATH, "/html/body/div[2]/nav/div/div[3]/ul/li[2]/div[2]")
    TOOL_TITLE = (By.XPATH, "//*[@id='nav-content']/ul/li[3]")
    TOOL_SPAN = (By.XPATH, "/html/body/div[2]/nav/div/div[3]/ul/li[3]/div[2]")
    ROOMY_BTN = (By.ID, "link-roomy")
    BLOG_BTN = (By.ID, "link-blog")
    CREDITCARD_BTN = (By.XPATH, "/html/body/div[2]/nav/div/div[3]/ul/li[2]/div[2]/a[1]")
    PERSONAL_LOAN_BTN = (
        By.XPATH,
        "/html/body/div[2]/nav/div/div[3]/ul/li[2]/div[2]/a[2]",
    )
    SECURED_LOAN_BTN = (
        By.XPATH,
        "/html/body/div[2]/nav/div/div[3]/ul/li[2]/div[2]/a[3]",
    )
    MORTGAGE_BTN = (By.XPATH, "/html/body/div[2]/nav/div/div[3]/ul/li[2]/div[2]/a[4]")
    ACCOUNT_BTN = (By.XPATH, "/html/body/div[2]/nav/div/div[3]/ul/li[5]")
    SERCURITIES_BTN = (By.XPATH, "/html/body/div[2]/nav/div/div[3]/ul/li[6]")

    def __init__(self, driver):
        super(Header, self).__init__(driver)

    def get_all_product_name(self):
        product_title = self.get_element_by(self.PRODUCT_TITLE)
        product_title.click()
        self.wait_for_visible(self.PRODUCT_SPAN)
        time.sleep(3)
        product_span = self.get_element_by(self.PRODUCT_SPAN)
        all_product_arr = product_span.text.splitlines()
        return all_product_arr

    def get_all_tool_name(self):
        tool_title = self.get_element_by(self.TOOL_TITLE)
        tool_title.click()
        self.wait_for_visible(self.TOOL_SPAN)
        time.sleep(3)
        tool_span = self.get_element_by(self.TOOL_SPAN)
        all_tool_arr = tool_span.text.splitlines()
        return all_tool_arr

    def click_roomy(self):
        roomy_link = self.get_element_by(self.ROOMY_BTN)
        roomy_link.click()
        current_url = self.get_current_url()
        return current_url

    def click_blog(self):
        blog_link = self.get_element_by(self.BLOG_BTN)
        blog_link.click()
        current_url = self.get_current_url()
        return current_url

    def click_all_product(self):
        product_title = self.get_element_by(self.PRODUCT_TITLE)
        product_title.click()
        self.wait_for_visible(self.PRODUCT_SPAN)
        time.sleep(3)

    def click_creditcard(self):
        self.click_all_product()
        creditcard_btn = self.get_element_by(self.CREDITCARD_BTN)
        creditcard_btn.click()
        current_url = self.get_current_url()
        return current_url

    def click_personal_loan(self):
        self.click_all_product()
        personal_loan_btn = self.get_element_by(self.PERSONAL_LOAN_BTN)
        personal_loan_btn.click()
        current_url = self.get_current_url()
        return current_url

    def click_secured_loan(self):
        self.click_all_product()
        secured_loan_btn = self.get_element_by(self.SECURED_LOAN_BTN)
        secured_loan_btn.click()
        current_url = self.get_current_url()
        return current_url

    def click_mortgage(self):
        self.click_all_product()
        mortgage_btn = self.get_element_by(self.MORTGAGE_BTN)
        mortgage_btn.click()
        current_url = self.get_current_url()
        return current_url

    def click_account(self):
        account_btn = self.get_element_by(self.ACCOUNT_BTN)
        account_btn.click()
        current_url = self.get_current_url()
        return current_url

    def click_securities(self):
        securities_btn = self.get_element_by(self.SERCURITIES_BTN)
        securities_btn.click()
        current_url = self.get_current_url()
        return current_url
