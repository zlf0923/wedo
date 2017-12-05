from common.base import BasePage
from selenium import webdriver
import time


class AddStaffPage(BasePage):
    staff_management = ("link text", "员工管理")
    staff_maintenance = ("link text", "员工维护")
    staff_frame = ("iframeBody")
    add_staff_button = ("id", "btnAddStaff")
    phone_loc = ("id", "identifyPhoneNumber")
    check_loc = ("class name", "checkbox_icon")
    deparment_loc = ("id", "staffAddDeparment")
    job_loc = ("id", "job")

    def click_staff_management(self):
        self.find_element(self.staff_management).click()

    def click_staff_maintenance(self):
        self.find_element(self.staff_maintenance).click()

    def switch_frame(self):
        self.switch_iframe(self.staff_frame)

    def click_addstaff_button(self):
        self.click(self.add_staff_button)

    def input_phone(self, text):
        self.send_keys(self.phone_loc, text)

    def click_checkbox(self):
        self.click(self.check_loc)

    def select_deparment(self, text):
        self.select_by_text(self.deparment_loc, text)

    def input_job(self, text):
        self.send_keys(self.job_loc, text)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # addemployee_driver = AddEmployee(driver)
    driver.get("http://192.168.9.81/enterprise-admin/")
    driver.maximize_window()
    driver.find_element_by_name("userName").send_keys("13764771995")
    driver.find_element_by_name("passWord").send_keys("qwe123")
    time.sleep(8)
    driver.find_element_by_id("login").click()
    time.sleep(2)
    driver.find_element_by_link_text("员工管理").click()
    driver.find_element_by_link_text("员工维护").click()
    driver.switch_to.frame("iframeBody")
    time.sleep(1)
    driver.find_element_by_id("btnAddStaff").click()
    driver.switch_to.default_content()
    time.sleep(1)
    # addemployee_driver.input_phone("13764771998")
    # addemployee_driver.click_checkbox()
    # addemployee_driver.select_deparment()

