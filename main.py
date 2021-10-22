from HTMLTestRunner import HTMLTestRunner
import unittest
import os # 系统
from threading import Thread
# 加载所有用例
class testbank(Thread):
    def run(self):
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Testbank1.py")
        runner = HTMLTestRunner.HTMLTestRunner(
            title="银行的测试报告",
            description="转账测试",
            verbosity=1,
            stream=open(file="计算器转账测试报告.html", mode="w+", encoding="utf-8")
        )
        runner.run(tests)
# 执行器
class testbank1(Thread):
    def run(self):
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestCalc.py")
        runner = HTMLTestRunner.HTMLTestRunner(
            title= "计算器的测试报告",
            description="加法的测试报告",
            verbosity=1,
            stream = open(file="计算器加法测试报告.html",mode="w+",encoding="utf-8")
)
        runner.run(tests)
class testbank3(Thread):
    def run(self):
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestCalc1.py")
        runner = HTMLTestRunner.HTMLTestRunner(
            title= "计算器的测试报告",
            description="减法的测试报告",
            verbosity=1,
            stream = open(file="计算器减法测试报告.html",mode="w+",encoding="utf-8")
)
        runner.run(tests)
class testbank4(Thread):
    def run(self):
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Testbank.py")
        runner = HTMLTestRunner.HTMLTestRunner(
            title= "银行的测试报告",
            description="开户的测试报告",
            verbosity=1,
            stream = open(file="银行开户测试报告.html",mode="w+",encoding="utf-8")
)
        runner.run(tests)
p1 = testbank()
p2 = testbank1()
p3 = testbank3()
p4 = testbank4()
p1.start()
p2.start()
p3.start()
p4.start()








