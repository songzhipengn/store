from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #事件链对象
#当前浏览器
driver = webdriver.Chrome()

#打开网址
driver.get("http://www.taobao.com")

#窗口最大化
driver.maximize_window()

#定位
#点击请登录
driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
#切换页面
date = driver.window_handles # ["s001","s002"]
driver.switch_to.window(date[0])

#点击密码登录
driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/a[1]').click()
#输入账号
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("13780291681")
#输入密码
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("13780291681a+")

driver.implicitly_wait(3)

try:
#鼠标滑动验证
  ac = ActionChains(driver)
  ab = driver.find_element_by_xpath("//*[@id='nc_1__scale_text']/span").click() #点住滑动块/滑块元素
  driver.implicitly_wait(3)
  ac.click_and_hold(ab).move_by_offset(258,0).perform()  #立即执行
  ac.release() #释放鼠标
except Exception:
    print("滑块就是动不了。")



#点击登录
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
