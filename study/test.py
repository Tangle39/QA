# -*-coding:utf-8 -*-
from selenium import webdriver
import time
import requests,base64

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')#屏蔽顶部的通知栏

br = webdriver.Chrome(chrome_options=option)

br.get('https://memberprod.alipay.com/account/reg/enterpriseIndex.htm')#支付宝注册页面
time.sleep(3)
br.switch_to.frame(br.find_element_by_css_selector("body > div:nth-child(19) > div.alipay-xbox.alipay-xbox-show > div.alipay-xbox-content > iframe"))
br.find_element_by_xpath('//*[@id="content"]/div[3]/a[1]/span').click()
#br.quit()