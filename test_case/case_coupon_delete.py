from selenium import webdriver
from page.login_page import LoginPage
from page.coupon_page import CouponPage
import unittest
import time


class CouponDelete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.delete_coupon_driver = CouponPage(self.driver)
        self.delete_coupon_driver.click_preferential_rules()
        self.delete_coupon_driver.click_enterprises_preferential_rules()
        self.delete_coupon_driver.switch_frame()

    def test_01(self):
        '''不选择优惠点击删除按钮'''
        self.delete_coupon_driver.click_delete_button()
        result = self.delete_coupon_driver.get_tip()
        print(result)
        self.assertEqual("请选择要删除的优惠", result)
        self.delete_coupon_driver.click_alert_button()

    def test_02(self):
        '''取消删除'''
        self.delete_coupon_driver.click_list_preferential()
        self.delete_coupon_driver.click_delete_button()
        self.delete_coupon_driver.click_alert_button2()

    def test_03(self):
        '''删除优惠'''
        try:
            self.delete_coupon_driver.click_list_preferential()
            self.delete_coupon_driver.click_delete_button()
            self.delete_coupon_driver.click_alert_button1()
            result = self.delete_coupon_driver.get_tip()
            print(result)
            self.assertEqual("删除优惠规则成功", result)
        except:
            print("优惠不存在")

    def test_04(self):
        '''删除生效中的优惠'''
        time.sleep(2)
        self.delete_coupon_driver.click_list_preferential()
        time.sleep(2)
        self.delete_coupon_driver.click_delete_button()
        w = self.delete_coupon_driver.is_alert_exists()  # 判断是否弹出删除提示框，False表示删除按钮不可点
        print(w)
        self.assertFalse(w)
        # result = self.delete_coupon_driver.is_click_delete_button()
        # print(result)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()