from selenium import webdriver
from page.login_page import LoginPage
from page.coupon_page import CouponPage
import unittest
import time


class SearchCoupon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.search_coupon_driver = CouponPage(self.driver)
        self.search_coupon_driver.click_preferential_rules()
        self.search_coupon_driver.click_enterprises_preferential_rules()
        self.search_coupon_driver.switch_frame()

    def test_01(self):
        self.search_coupon_driver.input_list_preferential_name("112701测试优惠")
        self.search_coupon_driver.input_list_shop_name("所有门店")
        self.search_coupon_driver.select_type("满减")
        self.search_coupon_driver.select_status("未生效")
        self.search_coupon_driver.input_time(js='document.getElementById("starttime").removeAttribute("readonly");'\
                                             'document.getElementById("starttime").value="2017-12-12"')
        self.search_coupon_driver.input_time(js='document.getElementById("endtime").removeAttribute("readonly");'\
                                             'document.getElementById("endtime").value="2017-12-12"')
        self.search_coupon_driver.click_search_button()

    def test_02(self):
        '''模糊查询'''
        self.search_coupon_driver.input_list_preferential_name("1111")
        self.search_coupon_driver.input_list_shop_name("所有")
        self.search_coupon_driver.select_type("全部")
        self.search_coupon_driver.select_status("全部")
        self.search_coupon_driver.input_time(js='document.getElementById("starttime").removeAttribute("readonly");'\
                                             'document.getElementById("starttime").value="2016-12-12"')
        self.search_coupon_driver.input_time(js='document.getElementById("endtime").removeAttribute("readonly");'\
                                             'document.getElementById("endtime").value="2018-12-12"')
        self.search_coupon_driver.click_search_button()

    def test_03(self):
        '''查询所有打折的优惠'''
        self.search_coupon_driver.select_type("打折")
        self.search_coupon_driver.click_search_button()

    def test_04(self):
        '''查询所有满减的优惠'''
        self.search_coupon_driver.select_type("满减")
        self.search_coupon_driver.click_search_button()

    def test_05(self):
        '''查看优惠详情'''
        self.search_coupon_driver.click_list_preferential()
        self.search_coupon_driver.click_see_button()
        time.sleep(3)
        self.search_coupon_driver.click_detail_back_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()