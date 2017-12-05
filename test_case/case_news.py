from selenium import webdriver
from page.news_page import NewsPage
from page.login_page import LoginPage, login_url
import unittest
import time


class News(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.news_driver = NewsPage(self.driver)
        self.login_driver.open(login_url)

    def login_case(self, username, pwd, code):
        self.login_driver.input_user(username)
        self.login_driver.input_pwd(pwd)
        self.login_driver.input_code(code)
        time.sleep(8)
        self.login_driver.click_login_button()

    def test_001(self):
        '''发布企业新闻1'''
        self.login_case("13764771995", "qwe123", "")  # 登录
        self.news_driver.click_enterprise_mxp()  # 点击企业名信片
        self.news_driver.click_news_core()  # 点击新闻中心
        self.news_driver.switch_frame()  # 切换iframe
        self.news_driver.click_add()  # 点击添加新闻按钮
        self.news_driver.input_news_title("测试新闻1129")
        self.news_driver.input_time(js='document.getElementById("addStartTime").removeAttribute("readonly");'\
                                       'document.getElementById("addStartTime").value="2017-11-11"')
        self.news_driver.input_time(js='document.getElementById("addEndTime").removeAttribute("readonly");'\
                                       'document.getElementById("addEndTime").value="2017-11-30"')
        self.news_driver.input_content("cs22")
        self.news_driver.upload_file(r"E:\292-0030.png")
        self.news_driver.click_save_button()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#dvMsgBtns>input").click()
        result = self.driver.find_element_by_xpath(".//*[@id='roleList']/tbody/tr[1]/td[1]/span").text
        print(result)
        self.assertIn("测试新闻11-10-05", result)
        # self.assertTrue(result)

    def test_002(self):
        '''发布企业新闻：标题最大值，内容输入过多的文字'''
        self.login_case("13764771995", "qwe123", "")  # 登录
        self.news_driver.click_enterprise_mxp()  # 点击企业名信片
        self.news_driver.click_news_core()  # 点击新闻中心
        self.news_driver.switch_frame()  # 切换iframe
        self.news_driver.click_add()  # 点击添加新闻按钮
        self.news_driver.input_news_title("测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试")
        self.news_driver.input_time(js='document.getElementById("addStartTime").removeAttribute("readonly");'\
                                       'document.getElementById("addStartTime").value="2017-11-11"')
        self.news_driver.input_time(js='document.getElementById("addEndTime").removeAttribute("readonly");'\
                                       'document.getElementById("addEndTime").value="2017-11-15"')
        self.news_driver.input_content("测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试新闻测试")
        self.news_driver.upload_file(r"E:\292-0030.png")
        self.news_driver.click_save_button()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#dvMsgBtns>input").click()
        result = self.driver.find_element_by_xpath(".//*[@id='roleList']/tbody/tr[1]/td[1]/span").text
        print(result)
        self.assertIn("测试新闻", result)

    def test_003(self):
        '''不输入任何字符，点击发布'''
        self.login_case("13764771995", "qwe123", "")  # 登录
        self.news_driver.click_enterprise_mxp()  # 点击企业名信片
        self.news_driver.click_news_core()  # 点击新闻中心
        self.news_driver.switch_frame()  # 切换iframe
        self.news_driver.click_add()  # 点击添加新闻按钮

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()