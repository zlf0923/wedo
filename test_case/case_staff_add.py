from selenium import webdriver
from page.login_page import LoginPage
from page.add_staff_page import AddStaffPage
import unittest
import time


class AddStaff(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.add_staff_driver = AddStaffPage(self.driver)
        self.add_staff_driver.click_staff_management()
        self.add_staff_driver.click_staff_maintenance()
        self.add_staff_driver.switch_frame()

    def test_01(self):
        self.add_staff_driver.click_addstaff_button()
        time.sleep(2)
        self.add_staff_driver.input_phone("13764771994")
        self.add_staff_driver.click_checkbox()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
