import unittest
from pages.header import Header


class TestMainHeader:
    def test_direct_roomy(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_roomy()
        assert current_url == "https://develop.roo.cash/community/roomy"

    def test_direct_blog(self, driver_class):
        roo_header = Header(driver_class)
        current_url = roo_header.click_blog()
        assert current_url == "https://roo.cash/blog/"

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

    def test_title_wording(self, driver_class):
        roo_header = Header(driver_class)
        expected = ["Roomy 袋鼠金融知室", "信用卡", "貸款", "數位帳戶", "證券帳戶", "專欄文章"]

    def test_creditcard_wording(self, driver_class):
        roo_header = Header(driver_class)
        expected = [
            "信用卡比較",
            "所有信用卡",
            "獨家首刷禮",
            "即時熱門排行",
            "精選信用卡推薦",
            "常用消費推薦",
            "現金回饋",
            "海外消費",
            "交通通勤",
            "網購",
        ]

    def test_loan_wording(self, driver_class):
        roo_header = Header(driver_class)
        expected = [
            "信用卡比較",
            "所有信用卡",
            "獨家首刷禮",
            "即時熱門排行",
            "精選信用卡推薦",
            "常用消費推薦",
            "現金回饋",
            "海外消費",
            "交通通勤",
            "網購",
        ]


if __name__ == "__main__":
    unittest.main(verbosity=2)
