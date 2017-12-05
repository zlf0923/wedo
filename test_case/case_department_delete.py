from selenium import webdriver
from page.login_page import LoginPage
from page.department_list_page import DepartmentListPage
import unittest
import time


class DeleteDepartment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        # self.driver.refresh()
        self.delete_department_driver = DepartmentListPage(self.driver)
        self.delete_department_driver.click_staff_management()
        self.delete_department_driver.click_department_list()
        self.delete_department_driver.switch_frame()
        time.sleep(1)

    def test_01(self):
        '''不选择部门点击删除'''
        self.delete_department_driver.click_delete()
        result = self.delete_department_driver.get_tip()
        print(result)
        self.assertEqual("请选择需要删除的部门", result)
        self.delete_department_driver.click_alert_button()

    def test_02(self):
        '''选择部门点击删除'''
        try:
            self.driver.find_element_by_xpath(".//*[@id='departmentList']/tbody/tr[5]").click()
            # self.delete_department_driver.click_department()
            self.delete_department_driver.click_delete()
            result = self.delete_department_driver.get_tip()
            print(result)
            self.assertEqual("删除部门信息成功", result)
            self.delete_department_driver.click_alert_button()
        except:
            print("部门不存在")

    def test_03(self):
        '''查询到部门再点击删除'''
        try:
            self.delete_department_driver.input_department("设计部")
            self.delete_department_driver.click_search()
            self.delete_department_driver.click_department()
            self.delete_department_driver.click_delete()
            result = self.delete_department_driver.get_tip()
            print(result)
            self.assertEqual("删除部门信息成功", result)
            self.delete_department_driver.click_alert_button()
        except:
            print("部门不存在")

    def test_04(self):
        '''删除有员工的部门'''
        try:
            # self.delete_department_driver.click_department()
            self.driver.find_element_by_xpath(".//*[contains(text(),'已建群')]").click()
            self.delete_department_driver.click_delete()
            result = self.delete_department_driver.get_tip()
            print(result)
            self.assertEqual("请先移除该部门所有员工后再做删除", result)
            self.delete_department_driver.click_alert_button()
        except:
            print("部门不存在")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()