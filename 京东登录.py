from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #事件链对象
#当前浏览器
driver = webdriver.Chrome()
#打开
driver.get("http://www.jd.com")
#窗口最大化
driver.maximize_window()
#定位
#点击请登录
driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()

#点击账户登录
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()

#切换页面
date = driver.window_handles # ["s001","s002"]
driver.switch_to.window(date[0])

#输入账号
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("13780291681")
#输入密码
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys("13780291681a+")
#点击登录
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()

#滑动条
ac = ActionChains(driver)
ele = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]').click() #点住滑动块/滑块元素
driver.implicitly_wait(2)
ac.click_and_hold(ele).move_by_offset(99,0).perform()  #立即执行
ac.release() #释放鼠标
