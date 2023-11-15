from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from pages.page import Page


class Footer(Page):
    TITLE = (By.CLASS_NAME, "mt-0 text-lg font-bold text-NRooBlue-100 md:mb-4")

    def __init__(self, driver):
        super(Footer, self).__init__(driver)

    def get_all_title(self):
        ele = self.get_elements_by(self.TITLE)
        print(len(ele))
