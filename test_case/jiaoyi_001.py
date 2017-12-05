from selenium import webdriver
import unittest
import time

class JiaoYi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.9.81/enterprise-admin/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_name("userName").send_keys("13585832653")
        self.driver.find_element_by_name("passWord").send_keys("w123456")
        time.sleep(10)
        self.driver.find_element_by_id("login").click()
        self.driver.find_element_by_xpath(".//*[@id='form1']/div/div[9]/a").click()

    def test_01(self):
        self.driver.find_element_by_xpath(".//*[@id='mdiv']/ul/li[5]").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("分类管理").click()
        time.sleep(2)
        self.driver.switch_to.frame("iframeBody")
        time.sleep(2)
        self.driver.find_element_by_class_name("span8").send_keys("测试")
        time.sleep(2)
        self.driver.find_element_by_id("sortSearch").click()


    def tearDown(self):
        self.driver.quit()