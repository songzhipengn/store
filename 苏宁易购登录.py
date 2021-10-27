from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#当前浏览器
driver = webdriver.Chrome()

#打开网址
driver.get("http://www.suning.com")

#窗口最大化
driver.maximize_window()

#定位
#点击请登录
driver.find_element_by_xpath('//*[@id="reg-bar-node"]/a[1]').click()
#切换页面
date = driver.window_handles # ["s001","s002"]
driver.switch_to.window(date[0])



#点击账户登录
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a[2]').click()

#输入账号
driver.find_element_by_xpath('//*[@id="userName"]').send_keys("13780291681")
#输入密码
driver.find_element_by_xpath('//*[@id="password"]').send_keys("13780291681a+")
driver.implicitly_wait(3)
#点击验证
driver.find_element_by_xpath('//*[@id="iar1_sncaptcha_button"]/span').click()

driver.implicitly_wait(3)

#滑动验证
ac = ActionChains(driver)
ab = driver.find_element_by_xpath('//*[class="tobe-obfuscate-slider transparent-icon"]').click()  # 点住滑动块/滑块元素
driver.implicitly_wait(3)
ac.click_and_hold(ab).move_by_offset(300, 0).perform()  # 立即执行
ac.release()  # 释放鼠标

driver.implicitly_wait(3)
#登录
driver.find_element_by_xpath('//*[@id="submit"]').click()