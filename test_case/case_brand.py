from selenium import webdriver
from page.login_page import LoginPage
from page.brand_page import BrandPage
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

'''
品牌介绍用例
'''


class Brand(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.brand_driver = BrandPage(self.driver)
        self.brand_driver.click_enterprise_mxp()
        self.brand_driver.click_brand_introduce()
        self.brand_driver.switch_frame()

    def test_01(self):
        self.brand_driver.click_edit_button()
        self.brand_driver.input_brand_name("SportsCar")
        self.brand_driver.input_brand_introduce("跑车的英文名是SportsCar或SportyCar，属于一种低底盘、线条流畅、动力突出的汽车类型，其最大特点是不断追求速度极限。"
                                                "跑车的分类有很多种，按车身结构可分为轿跑、敞篷跑车、双门跑车，按价值可分为平民跑车、超级跑车。")
        self.brand_driver.upload_image(r"E:\fo-3155231.jpg")
        self.brand_driver.click_save_button()
        time.sleep(1)
        name_result = self.brand_driver.get_brand_name()
        print(name_result)
        self.assertEqual("SportsCar", name_result)
        content_result = self.brand_driver.get_brand_content()
        print(content_result)
        self.assertIn("敞篷跑车", content_result)
        # s = r"E:\fo-3155231.jpg"
        # for a in s:
        #     print(a)
        #     self.brand_driver.upload_image(s)
        # b = self.brand_driver.file_is_click()
        # b = self.brand_driver.file_is_visibility()
        # b = self.brand_driver.file_is_exists()
        # print(b)

    def test_02(self):
        '''删除图片'''
        self.brand_driver.click_edit_button()
        self.brand_driver.move_to_image()
        self.brand_driver.click_close_image()
        self.brand_driver.click_alert_button3()
        self.brand_driver.click_save_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()