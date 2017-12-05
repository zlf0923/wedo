from common.base import BasePage
from selenium import webdriver
import time


class AddServicePage(BasePage):
    service_management = ("link text", "服务管理")
    service_release = ("link text", "服务发布申请")
    staff_frame = ("iframeBody")
    release_button = ("id", "serverReleaseBtn")

    def click_service_management(self):
        self.find_element(self.service_management).click()

    def click_service_release(self):
        self.find_element(self.service_release).click()

    def switch_frame(self):
        self.switch_iframe(self.staff_frame)

    def click_release_button(self):
        self.click(self.release_button)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    add_service_driver = AddServicePage(driver)
    add_service_driver.open("http://192.168.9.81/enterprise-admin/")
