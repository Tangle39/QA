# coding=utf-8
from selenium import webdriver
import unittest, time
import HTMLTestRunner

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')#屏蔽顶部的通知栏
print '=====AutoTest Start======'
class Test(unittest.TestCase):
    def setUp(self):   #固有
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(15)  # 隐性等待时间为30秒，比sleep智能
        self.base_url = "https://www.baidu.com"

    def test_learnta(self):
        driver = self.driver
        driver.get(self.base_url+ "/" ) #可以忽略
        driver.find_element_by_id("kw").clear()   #百度页面的id为kw,清空
        driver.find_element_by_id("kw").send_keys(u"论答") #no u :error
        driver.find_element_by_id("su").click()
        time.sleep(1)

        driver.find_element_by_partial_link_text("learnta").click()  #链接定位
        time.sleep(1)

        handles = driver.window_handles
        driver.switch_to_window(handles[1])   #切换窗口！
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[8]/a').click()  #xpath可能较慢  第一个btn
        #driver.find_element_by_css_selector('#root > div > div > div > div.navigation-bar > div.apply-button > a').click()
        #xhf提供的定位方法
        # driver.find_element_by_css_selector('#root > div > div > div > div.applyBtn  > a').click()  #第二个btn?待修正
        time.sleep(2)
        driver.find_element_by_id("orgName").send_keys(u"测试账号-东阳中学-勿回")
        driver.find_element_by_id('mobile').send_keys(15221286041)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys('3694')
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/form/button').click()

        time.sleep(3)


    def tearDown(self):  #固有
        self.driver.quit()


if __name__ == "__main__":

    unittest.main()
