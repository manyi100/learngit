
from splinter.browser import Browser
 
b = Browser(driver_name="chrome")
 
b.visit("http://www.baidu.com")  ###注意不要去掉http://

b.fill("wd","splinter")

button = b.find_by_value(u"百度一下")

#button = b.find_by_id(u"su")

button.click()

#b.quit()
