import unittest
import time
import HTMLTestRunner
import HTMLTestRunner_jpg
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 这个是优化版执行所有用例并发送报告，分四个步骤
# 第一步加载用例
# 第二步执行用例
# 第三步获取最新测试报告
# 第四步发送邮件 （这一步不想执行的话，可以注释掉最后面那个函数就行）

cur_path = os.path.dirname(os.path.relpath(__file__))


def add_case(caseName="test_case", rule="case_brand.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path): os.mkdir(case_path)
    print("test case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    report_abspath = os.path.join(report_path, now + "result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp,
                                               title=u'测试报告',
                                               description=u'用例执行情况：',
                                               verbosity=2,
                                               retry=1)
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    '''第四步：发送最新的测试报告内容'''
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = psw
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Disposition"] = 'attachment; filename= "report.html'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    all_case = add_case()  # 1加载用例
    # 生成测试报告的路径
    run_case(all_case)   # 2执行用例
    # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")
    report_file = get_report_file(report_path)  # 3获取最新的测试报告
    #邮箱配置
    sender = "826161977@qq.com"
    psw = "xxx"
    smtp_server = "smtp.qq.com"
    port = 465
    receiver = "635869873@qq.com"
    send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告

'''
testcase = unittest.TestSuite()

testcase.addTests(discover)

print(discover)
# print(testcase)

# runner = unittest.TextTestRunner()
# runner.run(testcase)


# now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = "E:\\pycharm project\\test_kabao\\report\\" + now +"result.html"
filename = "E:\\pycharm project\\test_kabao\\report\\result.html"
fp = open(filename, "wb")
'''