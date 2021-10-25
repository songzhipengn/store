from selenium import webdriver
import time
#当前浏览器
driver = webdriver.Chrome()

#打开页面
driver.get(r"D:\pythontask\自动化测试\day1\练习的html\跳转页面\pop.html")

#窗口最大化
driver.maximize_window()

#定位
time.sleep(2)
driver.find_element_by_xpath("//*[@id = 'goo']").click()

driver.quit()

























