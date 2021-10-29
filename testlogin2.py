from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import time
from 自动化测试03.InitPage import InitPage
from 自动化测试03.LoginOperation import LoginOperation
from selenium import webdriver
@ddt
class testlogin2(TestCase):
    @data(*InitPage.login_error_data)
    def testLoginError(self, testdata):
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]

        # 执行登陆
        driver = webdriver.Chrome()
        loginop = LoginOperation(driver)

        loginop.login(username, pwd)

        #  获取实际结果
        result = loginop.getError_result()

        driver.quit()

        self.assertEqual(result, expect)
