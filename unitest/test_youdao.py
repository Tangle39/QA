# coding=utf-8
'''
updated
'''
from selenium import webdriver
import unittest, time
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')#屏蔽顶部的通知栏

class YoudaoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "http://www.youdao.com"

    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys(u"你好")
        driver.find_element_by_id("translateContent").submit()  #由于翻译无具体id，用submit提交
        time.sleep(3)
        page_source = driver.page_source
        #page_source方法可以直接返回页面源码
        self.assertIn("hello", page_source)
        #assertIn(arg1, arg2, msg=None)	验证arg1是arg2的子串，不是则fail
       # time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()