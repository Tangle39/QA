# coding=utf-8
'''
http://www.cnblogs.com/yufeihlf/p/5707929.html#test1
'''
from selenium import webdriver
import unittest, time

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')#屏蔽顶部的通知栏
class BaiduTest(unittest.TestCase):
    def setUp(self):   #固有
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"

    def test_baidu0(self):
        driver = self.driver
        driver.get(self.base_url+ "/" ) #
        driver.find_element_by_id("kw").clear()   #百度页面的id为kw
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(5)
        title = driver.title   #浏览器标题
        self.assertEqual(title, u"unittest_百度搜索") #check

    def tearDown(self):  #固有
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

