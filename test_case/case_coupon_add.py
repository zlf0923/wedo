from selenium import webdriver
from page.login_page import LoginPage
from page.coupon_page import CouponPage
import unittest
import time


class AddCoupon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.add_coupon_driver = CouponPage(self.driver)
        self.add_coupon_driver.click_preferential_rules()
        self.add_coupon_driver.click_enterprises_preferential_rules()
        self.add_coupon_driver.switch_frame()

    def test_01(self):
        '''不输入任何信息，点击保存'''
        self.add_coupon_driver.click_add_button()
        self.add_coupon_driver.click_save_button()
        result = self.add_coupon_driver.get_tip()
        print(result)
        self.assertEqual("请选择实体店", result)
        self.add_coupon_driver.click_alert_button()

    def test_02(self):
        '''创建一个满减优惠的优惠券'''
        self.add_coupon_driver.click_add_button()
        self.add_coupon_driver.click_shop()
        self.add_coupon_driver.choice_shop_name()
        self.add_coupon_driver.input_preferential_name("112701测试优惠")
        self.add_coupon_driver.input_time(js='document.getElementById("starttime1").removeAttribute("readonly");'\
                                             'document.getElementById("starttime1").value="2017-12-12"')
        self.add_coupon_driver.input_time(js='document.getElementById("endtime1").removeAttribute("readonly");'\
                                             'document.getElementById("endtime1").value="2017-12-12"')
        self.add_coupon_driver.input_money("500")
        self.add_coupon_driver.input_reduction("100")
        self.add_coupon_driver.input_remark("全场满500-100")
        self.add_coupon_driver.click_save_button()
        result = self.add_coupon_driver.get_tip()
        print(result)
        self.assertEqual("成功", result)
        self.add_coupon_driver.click_alert_button()

    def test_03(self):
        '''创建一个优惠名称重复的优惠券'''
        self.add_coupon_driver.click_add_button()
        self.add_coupon_driver.click_shop()
        self.add_coupon_driver.choice_shop_name()
        self.add_coupon_driver.input_preferential_name("112701测试优惠")
        self.add_coupon_driver.input_time(js='document.getElementById("starttime1").removeAttribute("readonly");'\
                                             'document.getElementById("starttime1").value="2017-12-12"')
        self.add_coupon_driver.input_time(js='document.getElementById("endtime1").removeAttribute("readonly");'\
                                             'document.getElementById("endtime1").value="2017-12-12"')
        self.add_coupon_driver.input_money("500")
        self.add_coupon_driver.input_reduction("100")
        self.add_coupon_driver.input_remark("全场满500-100")
        self.add_coupon_driver.click_save_button()
        result = self.add_coupon_driver.get_tip()
        print(result)
        self.assertEqual("同一企业下的优惠规则名称不可重复", result)
        self.add_coupon_driver.click_alert_button()

    def test_04(self):
        '''创建一个满减金额大于或等于单笔订单金额的优惠券'''
        self.add_coupon_driver.click_add_button()
        self.add_coupon_driver.click_shop()
        self.add_coupon_driver.choice_shop_name()
        self.add_coupon_driver.input_preferential_name("112702测试优惠")
        self.add_coupon_driver.input_time(js='document.getElementById("starttime1").removeAttribute("readonly");'\
                                             'document.getElementById("starttime1").value="2017-12-12"')
        self.add_coupon_driver.input_time(js='document.getElementById("endtime1").removeAttribute("readonly");'\
                                             'document.getElementById("endtime1").value="2017-12-12"')
        self.add_coupon_driver.input_money("1")
        self.add_coupon_driver.input_reduction("100")
        self.add_coupon_driver.input_remark("全场满500-100")
        self.add_coupon_driver.click_save_button()
        result = self.add_coupon_driver.get_tip()
        print(result)
        self.assertEqual("满减金额不能大于单笔订单金额", result)
        self.add_coupon_driver.click_alert_button()
        self.add_coupon_driver.input_reduction("1")
        self.add_coupon_driver.click_save_button()
        result = self.add_coupon_driver.get_tip()
        print(result)
        self.assertEqual("满减金额不能大于或者等于单笔订单金额", result)

    def test_05(self):
        '''创建一个打折优惠的优惠券'''
        self.add_coupon_driver.click_add_button()
        self.add_coupon_driver.click_shop()
        self.add_coupon_driver.choice_shop_name()
        self.add_coupon_driver.input_preferential_name("112703测试打折优惠")
        self.add_coupon_driver.input_time(js='document.getElementById("starttime1").removeAttribute("readonly");'\
                                             'document.getElementById("starttime1").value="2017-12-12"')
        self.add_coupon_driver.input_time(js='document.getElementById("endtime1").removeAttribute("readonly");'\
                                             'document.getElementById("endtime1").value="2017-12-12"')
        self.add_coupon_driver.input_money("299")
        self.add_coupon_driver.click_discounted_radio()
        self.add_coupon_driver.input_discount("9")
        self.add_coupon_driver.input_remark("全场满299打9折")
        self.add_coupon_driver.click_save_button()
        result = self.add_coupon_driver.get_tip()
        print(result)
        self.assertEqual("成功", result)
        self.add_coupon_driver.click_alert_button()

    def test_06(self):
        '''折扣输入0折和10折'''
        self.add_coupon_driver.click_add_button()
        self.add_coupon_driver.click_shop()
        self.add_coupon_driver.choice_shop_name()
        self.add_coupon_driver.input_preferential_name("1127034测试打折优惠")
        self.add_coupon_driver.input_time(js='document.getElementById("starttime1").removeAttribute("readonly");'\
                                             'document.getElementById("starttime1").value="2017-12-12"')
        self.add_coupon_driver.input_time(js='document.getElementById("endtime1").removeAttribute("readonly");'\
                                             'document.getElementById("endtime1").value="2017-12-12"')
        self.add_coupon_driver.input_money("299")
        self.add_coupon_driver.click_discounted_radio()
        self.add_coupon_driver.input_discount("0")
        self.add_coupon_driver.input_remark("全场满299打9折")
        self.add_coupon_driver.click_save_button()
        result = self.add_coupon_driver.get_tip()
        print(result)
        self.assertEqual("折扣必须在0和10之间", result)
        self.add_coupon_driver.click_alert_button()
        self.add_coupon_driver.input_discount("10")
        self.add_coupon_driver.click_save_button()
        result = self.add_coupon_driver.get_tip()
        print(result)
        self.assertEqual("打折额度只能输入0到10之间的数字", result)

    def test_07(self):
        print(1)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()