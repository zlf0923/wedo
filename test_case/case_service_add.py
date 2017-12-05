from selenium import webdriver
from page.login_page import LoginPage
from page.add_service_page import AddServicePage
import unittest
import time


class AddService(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.add_service_driver = AddServicePage(self.driver)
        self.add_service_driver.click_service_management()
        self.add_service_driver.click_service_release()
        self.add_service_driver.switch_frame()
        time.sleep(1)

    def test_01(self):
        self.add_service_driver.click_release_button()
        self.driver.find_element_by_id("title").send_keys("123")



    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
