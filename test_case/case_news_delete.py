from selenium import webdriver
from page.login_page import LoginPage
from page.news_page import NewsPage
import unittest
import time


class NewsDelete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.delete_news_driver = NewsPage(self.driver)
        self.delete_news_driver.click_enterprise_mxp()
        self.delete_news_driver.click_news_core()
        self.delete_news_driver.switch_frame()

    def test_01(self):
        '''删除列表第一条企业新闻'''
        self.delete_news_driver.click_list_news()
        self.delete_news_driver.click_delete_button()
        self.delete_news_driver.click_alert_button1()
        time.sleep(1)
        result = self.delete_news_driver.get_tip()
        print(result)
        self.assertEqual("删除成功", result)

    def test_02(self):
        '''先查询发布成功的，再删除企业新闻'''
        self.delete_news_driver.input_title("测试新闻")
        self.delete_news_driver.click_status_select("发布成功")
        self.delete_news_driver.click_search_button()
        time.sleep(1)
        self.delete_news_driver.click_list_news()
        self.delete_news_driver.click_delete_button()
        self.delete_news_driver.click_alert_button1()
        time.sleep(1)
        result = self.delete_news_driver.get_tip()
        print(result)
        self.assertEqual("删除成功", result)

    def test_03(self):
        '''先查询指定时间范围的，再删除企业新闻'''
        self.delete_news_driver.input_time(js='document.getElementById("startTime").removeAttribute("readonly");'\
                                              'document.getElementById("startTime").value="2017-11-01"')
        self.delete_news_driver.input_time(js='document.getElementById("endTime").removeAttribute("readonly");'\
                                              'document.getElementById("endTime").value="2017-11-28"')
        self.delete_news_driver.click_search_button()
        time.sleep(1)
        self.delete_news_driver.click_list_news()
        self.delete_news_driver.click_delete_button()
        self.delete_news_driver.click_alert_button1()
        time.sleep(1)
        result = self.delete_news_driver.get_tip()
        print(result)
        self.assertEqual("删除成功", result)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

