from selenium import webdriver
from page.login_page import LoginPage
from page.news_page import NewsPage
import unittest
import time


class NewsUpdate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.login()
        self.delete_news_driver = NewsPage(self.driver)
        self.delete_news_driver.click_enterprise_mxp()
        self.delete_news_driver.click_news_core()
        self.delete_news_driver.switch_frame()
        time.sleep(2)

    def test_01(self):
        '''修改新闻标题'''
        self.delete_news_driver.click_list_news()
        self.delete_news_driver.click_update_button()
        self.delete_news_driver.input_news_title("1129新闻")
        self.delete_news_driver.input_content("hi")
        self.delete_news_driver.click_save_button()
        result = self.delete_news_driver.get_tip()
        print(result)
        self.assertEqual("添加或编辑新闻成功", result)

    def test_02(self):
        '''修改新闻有效期'''
        self.delete_news_driver.click_list_news()
        self.delete_news_driver.click_update_button()
        self.delete_news_driver.input_news_title("1129新闻")
        self.delete_news_driver.input_time(js='document.getElementById("addStartTime").removeAttribute("readonly");'\
                                              'document.getElementById("addStartTime").value="2017-11-29"')
        self.delete_news_driver.input_time(js='document.getElementById("addEndTime").removeAttribute("readonly");'\
                                              'document.getElementById("addEndTime").value="2017-11-30"')
        self.delete_news_driver.input_content("hi")
        self.delete_news_driver.click_save_button()
        result = self.delete_news_driver.get_tip()
        print(result)
        self.assertEqual("添加或编辑新闻成功", result)

    def test_03(self):
        '''修改新闻封面图'''
        self.delete_news_driver.click_list_news()
        self.delete_news_driver.click_update_button()
        self.delete_news_driver.move_to_image()
        self.delete_news_driver.click_close_image()
        self.delete_news_driver.click_alert_button3()
        self.delete_news_driver.upload_file(r"E:\fo-3155231.jpg")
        self.delete_news_driver.click_save_button()
        result = self.delete_news_driver.get_tip()
        print(result)
        self.assertEqual("添加或编辑新闻成功", result)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()