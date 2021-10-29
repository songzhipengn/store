from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import time
from 自动化测试03.InitPage import InitPage
from 自动化测试03.LoginOperation import LoginOperation
from selenium import webdriver
@ddt
class testlogin1(TestCase):


    @data(*InitPage.login_success_date)
    def testLoginSuccess(self,testdata):
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect =  testdata["expect"]

        # 执行登陆
        driver = webdriver.Chrome()
        loginop = LoginOperation(driver)

        loginop.login(username,pwd)

        #  获取实际结果
        result = loginop.getSuccess_result()
        # if result != expect:
        #     driver.save_screenshot("img/error.png")
        driver.quit()

        self.assertEqual(result,expect)