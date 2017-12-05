from selenium import webdriver
from page.login_page import LoginPage, login_url
import unittest
import time
import ddt

data_dict = [{"username": "13764771995", "pwd": "qwe123", "code": ""},
             {"username": "13764771995", "pwd": "qwe12345", "code": ""},
             {"username": "13755555555", "pwd": "qwe12345", "code": ""}]

d2 = {"username": "13764771995", "pwd": "qwe12345"}
d3 = {"username": "13755555555", "pwd": "qwe12345"}
d4 = ("13764771995", "qwe123")


@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.open(login_url)

    def login_case(self, username, pwd, code):
        self.login_driver.input_user(username)
        self.login_driver.input_pwd(pwd)
        self.login_driver.input_code(code)
        time.sleep(8)
        self.login_driver.click_login_button()

    def is_login_sucess(self):
        # 判断是否获取到登录名称
        try:
            text = self.driver.find_elements_by_css_selector(".brand>small")[1].text
            print(text)
            return True
        except:
            return False


    @ddt.data(*data_dict)
    def test_001(self, data):
        print(data)
        '''输入正确的账号密码'''
        self.login_case(data["username"], data["pwd"], data["code"])
        # self.login_case(*d4, "")
        time.sleep(2)
        result = self.is_login_sucess()
        print(result)
        self.assertTrue(result)
        # t = self.driver.find_elements_by_css_selector(".brand>small")[1].text
        # print(t)
        # self.assertIn(u"张万根", t)

    # def test_002(self):
    #     '''输入错误的密码'''
    #     self.login_case(d2["username"], d2["pwd"], "")
    #     t = self.login_driver.get_tip()
    #     print(t)
    #     self.assertEqual(u"CAS认证失败，请检查用户名或密码！", t)
    #
    # def test_003(self):
    #     '''输入不存在的账号'''
    #     self.login_case(d3["username"], d3["pwd"], "")
    #     t = self.login_driver.get_tip()
    #     print(t)
    #     self.assertEqual(u"CAS认证失败，请检查用户名或密码！", t)
    #
    # def test_004(self):
    #     '''不输入验证码'''
    #     self.login_case(d3, "")
    #     time.sleep(2)
    #     t = self.driver.switch_to.alert.text
    #     print(t)
    #     self.assertIn(u"请输入验证码", t)
    #     self.driver.switch_to.alert.accept()
    #     time.sleep(2)
    #
    # def test_005(self):
    #     '''输入错误的验证码'''
    #     self.login_case(d3, "6666")
    #     time.sleep(2)
    #     t = self.driver.switch_to.alert.text
    #     print(t)
    #     self.assertIn(u"验证码输入错误", t)
    #     self.driver.switch_to.alert.accept()
    #     time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
