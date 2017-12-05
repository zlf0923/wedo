from selenium import webdriver
import unittest
import time

class Baidu(unittest.TestCase):
    '''百度搜索'''
    def setUp(self):
        print("start")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(10)

    def test_001(self):
        '''百度搜索selenium'''
        print("1111")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        t = self.driver.title
        print(t)
        self.assertEqual(t, u"selenium_百度搜索")

    def test_002(self):
        '''百度搜索python'''
        print("2222")
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        t = self.driver.title
        print(t)
        self.assertEqual(t, u"python_百度搜索")

    def tearDown(self):
        print("end")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
