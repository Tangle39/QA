# -*-coding:utf-8 -*-
from selenium import webdriver
import time
import requests,base64

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')#屏蔽顶部的通知栏

'''br = webdriver.Chrome(chrome_options=option)

br.get('https://memberprod.alipay.com/account/reg/enterpriseIndex.htm')#支付宝注册页面
time.sleep(3)
#br.switch_to.frame(br.find_element_by_css_selector("body > div:nth-child(19) > div.alipay-xbox.alipay-xbox-show > div.alipay-xbox-content > iframe"))
#br.find_element_by_xpath('//*[@id="content"]/div[3]/a[1]/span').click()
#br.quit()
br.refresh() #刷新
br.find_element_by_id('button')
'''
driver = webdriver.Chrome(chrome_options=option)

driver.get("http://www.youdao.com")
#清空输入框原有的内容
driver.find_element_by_id("translateContent").send_keys("test")
time.sleep(2)
driver.find_element_by_id("translateContent").clear()
driver.find_element_by_id("translateContent").send_keys("Hello world")

#提交输入框的内容
driver.find_element_by_id("translateContent").submit()
time.sleep(5)
driver.find_element_by_id("translateContent").quit()