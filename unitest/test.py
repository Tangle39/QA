# coding=utf-8
'''
Created on 2016-7-22
@author: Jennifer
Project:使用有道翻译测试用例
'''
from selenium import webdriver
import unittest, time
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')#屏蔽顶部的通知栏

dr = webdriver.Chrome(chrome_options=option)
dr.get('https:www.baidu.com')
# p = dr.page_source
# print p

dr.find_element_by_id("kw").clear()  # 百度页面的id为kw
dr.find_element_by_id("kw").send_keys("unittest")
dr.find_element_by_id("kw").submit()
time.sleep(1)
dr.quit()