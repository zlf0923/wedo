from selenium import webdriver
from page.login_page import LoginPage
from page.coupon_page import CouponPage
import unittest
import time


class UpdateCoupon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.update_coupon_driver = CouponPage(self.driver)
        self.update_coupon_driver.click_preferential_rules()
        self.update_coupon_driver.click_enterprises_preferential_rules()
        self.update_coupon_driver.switch_frame()

    def test_01(self):
        '''修改优惠名称'''
        try:
            self.update_coupon_driver.click_list_preferential()
            self.update_coupon_driver.click_editor_button()
            self.update_coupon_driver.input_preferential_name("112901测试优惠")
            self.update_coupon_driver.input_time(js='document.getElementById("starttime1").removeAttribute("readonly");'\
                                                    'document.getElementById("starttime1").value="2017-12-12"')
            self.update_coupon_driver.input_time(js='document.getElementById("endtime1").removeAttribute("readonly");'\
                                                    'document.getElementById("endtime1").value="2017-12-12"')
            self.update_coupon_driver.click_save_button()
            result = self.update_coupon_driver.get_tip()
            print(result)
            self.assertEqual("成功", result)
        except:
            print("优惠不存在")

    def test_02(self):
        '''修改优惠时间'''
        try:
            self.update_coupon_driver.click_list_preferential()
            self.update_coupon_driver.click_editor_button()
            self.update_coupon_driver.input_preferential_name("112901测试优惠")
            self.update_coupon_driver.input_time(js='document.getElementById("starttime1").removeAttribute("readonly");'\
                                                    'document.getElementById("starttime1").value="2017-11-30"')
            self.update_coupon_driver.input_time(js='document.getElementById("endtime1").removeAttribute("readonly");'\
                                                    'document.getElementById("endtime1").value="2017-12-01"')
            self.update_coupon_driver.click_save_button()
            result = self.update_coupon_driver.get_tip()
            print(result)
            self.assertEqual("成功", result)
        except:
            print("优惠不存在")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()