from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread

#加载所有用例
class testlogin1(Thread):
    def run(self):
       tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="testlogin1.py")

       runner = HTMLTestRunner.HTMLTestRunner(
        title = "HKR系统测试成功报告",
        description= "HKR系统登陆成功测试",
        verbosity=1,
        stream = open(file="HKR系统登录成功.html",mode="w+",encoding="utf-8")
)

       runner.run(tests)

class testlogin2(Thread):
    def run(self):
      tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="testlogin2.py")

      runner = HTMLTestRunner.HTMLTestRunner(
        title="HKR系统测试登陆失败报告",
        description="HKR系统登陆失败测试",
        verbosity=1,
        stream=open(file="HKR系统登录失败.html", mode="w+", encoding="utf-8")
    )

      runner.run(tests)
p1 = testlogin1()
p2 = testlogin2()
p1.start()
p2.start()



















# 邮件发送模块





