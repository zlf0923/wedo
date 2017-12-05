from selenium import webdriver
from page.login_page import LoginPage
from page.staff_list_page import StaffListPage
import unittest
import time


class StaffList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.staff_driver = StaffListPage(self.driver)
        self.staff_driver.click_staff_management()
        self.staff_driver.click_staff_maintenance()
        self.staff_driver.switch_frame()

    def test_01(self):
        '''默认查询'''
        self.staff_driver.click_search_button()

    def test_02(self):
        '''模糊查询'''
        self.staff_driver.input_phone("1376477")
        self.staff_driver.input_name("张")
        self.staff_driver.input_job("测")
        self.staff_driver.click_department_select("总裁办")
        self.staff_driver.click_Status_select("已认证")
        self.staff_driver.click_Role_select("全部")
        self.staff_driver.click_search_button()

    def test_03(self):
        '''精确查询'''
        self.staff_driver.input_phone("13764771996")
        self.staff_driver.input_name("张领峰")
        self.staff_driver.input_job("测试")
        self.staff_driver.click_department_select("总裁办")
        self.staff_driver.click_Status_select("已认证")
        self.staff_driver.click_Role_select("全部")
        self.staff_driver.click_search_button()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()