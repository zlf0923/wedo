import unittest
import time
import HTMLTestRunner
import HTMLTestRunner_jpg

case_dir = r"E:\pycharm project\test_kabao\test_case"

testcase = unittest.TestSuite()

discover = unittest.defaultTestLoader.discover(start_dir=case_dir,
                                               pattern="case_news.py",
                                               top_level_dir=None)

testcase.addTests(discover)

print(discover)
# print(testcase)

# runner = unittest.TextTestRunner()
# runner.run(testcase)


# now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = "E:\\pycharm project\\test_kabao\\report\\" + now +"result.html"
filename = "E:\\pycharm project\\test_kabao\\report\\result.html"
fp = open(filename, "wb")
runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp,
                                       title=u'测试报告',
                                       description=u'用例执行情况：',
                                       verbosity=2,
                                       retry=1)
runner.run(discover)
fp.close()
