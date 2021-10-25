from selenium import webdriver


#当前浏览器
driver = webdriver.Chrome()

#打开
driver.get("http://www.jd.com")

#窗口最大化

driver.maximize_window()

#定位
# 搜索框
driver.find_element_by_xpath("//*[@id = 'key']").send_keys("iphone13")

#确认搜索按钮
driver.find_element_by_xpath("//*[@class = 'button']").click()
driver.implicitly_wait(6)

a = driver.current_window_handle

#商品
driver.find_element_by_xpath("//*[@href ='//item.jd.com/100026667884.html']").click()

driver.implicitly_wait(4)
for i in driver.window_handles:
    if i != a:
        driver.switch_to.window(i)
#抢购
driver.find_element_by_xpath("//*[@class = 'btn-special1 btn-lg']").click()





