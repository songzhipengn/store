from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # 事件链对象
#当前浏览器
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.bilibili.com")
#窗口最大化
driver.maximize_window()

driver.implicitly_wait(3)

#定位
#点击登录
try:
 driver.find_element_by_xpath('//*[@id="i_cecream"]/div[1]/div[1]/ul[2]/li[1]/li/div/div/span').click()
except Exception:
    driver.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/span[1]/div/span/div').click()

#切换页面
date = driver.window_handles
driver.switch_to.window(date[1])

driver.implicitly_wait(3)
#输入账号
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("13780291681")
#输入密码
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys("13780291681a+")

driver.implicitly_wait(3)
#点击登录
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()

















