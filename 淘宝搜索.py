from selenium import webdriver


#当前浏览器
driver = webdriver.Chrome()

#打开
driver.get("http://www.taobao.com")

#窗口最大化

driver.maximize_window()

#定位
# 搜索框
driver.find_element_by_xpath("//*[@id = 'q']").send_keys("iphone13")

#确认搜索按钮
driver.find_element_by_xpath("//*[@class = 'btn-search tb-bg']").click()
driver.implicitly_wait(6)







