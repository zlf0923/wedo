from common.base import BasePage
from selenium import webdriver
import time

login_url = "http://192.168.9.81/enterprise-admin/"


class LoginPage(BasePage):
    user_loc = ("name", "userName")
    psw_loc = ("name", "passWord")
    code_loc = ("id", "inputCode")
    button_loc = ("id", "login")
    tip_loc = ("id", "msg")
    enterprise = ("xpath", ".//*[contains(text(),'1016内网测试')]")

    def input_user(self, text):
        self.send_keys(self.user_loc, text)

    def input_pwd(self, text):
        self.send_keys(self.psw_loc, text)

    def input_code(self, text):
        self.send_keys(self.code_loc, text)

    def click_login_button(self):
        self.click(self.button_loc)

    def click_enterprise(self):
        self.click(self.enterprise)

    def get_tip(self):
        t = self.get_text(self.tip_loc)
        return t

    def get_alert(self):
        t = self.is_alert_present()
        return t

    def click_alert(self):
        self.switch_alert()

    def login(self):
        self.login_driver = LoginPage(self.driver)
        self.login_driver.open(login_url)
        self.login_driver.input_user("13764771995")
        self.login_driver.input_pwd("qwe123")
        self.login_driver.input_code("")
        time.sleep(8)
        self.login_driver.click_login_button()
        self.login_driver.click_enterprise()
