from selenium import webdriver


#当前浏览器
driver = webdriver.Chrome()

#打开
driver.get("http://www.suning.com")

#窗口最大化

driver.maximize_window()

#定位
# 搜索框
driver.find_element_by_xpath("//*[@id = 'searchKeywords']").send_keys("iphone13")

#确认搜索按钮
driver.find_element_by_xpath("//*[@id = 'searchSubmit']").click()
driver.implicitly_wait(6)

a = driver.current_window_handle

#商品
driver.find_element_by_xpath("//*[@src = '//imgservice2.suning.cn/uimg1/b2c/image/TF6zVo1-qluE7nV_NdWeZQ.png_400w_400h_4e']").click()

driver.implicitly_wait(4)
for i in driver.window_handles:
    if i != a:
        driver.switch_to.window(i)
#抢购
driver.find_element_by_xpath("//*[@id = 'addCart']").click()


