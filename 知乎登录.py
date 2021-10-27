from selenium import webdriver

#当前浏览器
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.zhihu.com")
#窗口最大化
driver.maximize_window()
#定位
#点击密码登录
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]').click()
driver.implicitly_wait(3)
#输入账号
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[2]/div/label/input').send_keys("13780291681")
driver.implicitly_wait(3)
#输入密码
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys("13780291681a+")
driver.implicitly_wait(3)

#点击登录
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/button').click()

