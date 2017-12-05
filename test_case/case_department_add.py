from selenium import webdriver
from page.login_page import LoginPage
from page.department_list_page import DepartmentListPage
import unittest
import time
import random


class AddDepartment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.driver.refresh()
        self.add_department_driver = DepartmentListPage(self.driver)
        self.add_department_driver.click_staff_management()
        self.add_department_driver.click_department_list()
        self.add_department_driver.switch_frame()

    def test_01(self):
        '''添加部门'''
        a = str(random.randint(0, 1000))
        self.add_department_driver.click_add()
        self.add_department_driver.input_addpage_department("设计部%s" % a)
        self.add_department_driver.click_save()
        result = self.add_department_driver.get_tip()
        print(result)
        self.assertEqual("部门创建成功", result)
        self.add_department_driver.click_alert_button()

    def test_02(self):
        '''添加重复部门'''
        self.add_department_driver.click_add()
        self.add_department_driver.input_addpage_department("设计部")
        self.add_department_driver.click_save()
        result = self.add_department_driver.get_tip()
        print(result)
        self.assertEqual("部门名称不能重复", result)
        self.add_department_driver.click_alert_button()

    def test_03(self):
        '''不输入部门名称，点击确定'''
        self.add_department_driver.click_add()
        # self.add_department_driver.input_addpage_department("设计部")
        self.add_department_driver.click_save()
        result = self.add_department_driver.get_tip()
        print(result)
        self.assertEqual("请输入部门名称", result)
        self.add_department_driver.click_alert_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()