from selenium import webdriver
from page.login_page import LoginPage
from page.introduction_page import IntroductionPage
import unittest
import time

'''
企业简介用例
'''


class Introduction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.introduction_driver = IntroductionPage(self.driver)
        self.introduction_driver.click_enterprise_mxp()
        self.introduction_driver.click_brand_introduce()
        self.introduction_driver.switch_frame()

    def test_01(self):
        self.introduction_driver.click_edit_button()
        self.introduction_driver.input_content("1201测试")
        self.introduction_driver.click_save_button()
        # self.introduction_driver.click_image()
        # self.driver.find_element_by_class_name("xheBtn").click()
        # button = "$('.xheBtn').click()"
        # self.driver.execute_script(button)
        # self.introduction_driver.click_upload_button()
        # self.introduction_driver.upload_image(r"E:\fo-3155231.jpg")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()