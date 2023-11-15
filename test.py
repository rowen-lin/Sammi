import unittest
import time

from pages.header import Header
from pages.footer import Footer


class Test:
    def test_direct_roomy(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_roomy()
        assert current_url == "https://develop.roo.cash/community/roomy"

    def test_direct_blog(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_blog()
        assert current_url == "https://roo.cash/blog/"

    def test_header_product_wording(self, driver_class):
        roo_header = Header(driver_class)
        result = roo_header.get_all_product_name()
        expected = ["全台信用卡", "信用貸款", "小額借款", "房屋貸款", "數位帳戶", "證券帳戶"]
        assert result == expected

    def test_header_tool_wording(self, driver_class):
        roo_header = Header(driver_class)
        result = roo_header.get_all_tool_name()
        expected = ["個人財務建議 BETA", "信貸月付金試算", "信貸額度試算", "房貸月付金試算"]
        assert result == expected

    def test_direct_creditcard_page(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_creditcard()
        assert current_url == "https://develop.roo.cash/creditcard"

    def test_direct_personal_loan(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_personal_loan()
        assert current_url == "https://develop.roo.cash/personal-loan"

    def test_direct_secured_loan(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_secured_loan()
        assert current_url == "https://develop.roo.cash/secured-loan/recommendation"

    def test_direct_mortgage(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_mortgage()
        assert current_url == "https://develop.roo.cash/mortgage/recommendation"

    def test_direct_account(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_account()
        assert current_url == "https://develop.roo.cash/account/recommendation"

    def test_direct_securities(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_securities()
        assert (
            current_url == "https://develop.roo.cash/securities/account-recommendation"
        )

    def test_footer_title_wording(self, driver_class):
        roo_footer = Footer(driver_class)
        title = roo_footer.get_all_title()


if __name__ == "__main__":
    unittest.main(verbosity=2)
