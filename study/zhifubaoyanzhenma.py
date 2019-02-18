
# -*-coding:utf-8 -*-
#by iqiyi 席海峰
from selenium import webdriver
import time
import requests,base64

'''options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
browser = webdriver.Chrome(chrome_options=options)
'''
'''--------------------- 

原文：https://blog.csdn.net/zhu940923/article/details/81149050 

'''
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://memberprod.alipay.com/account/reg/enterpriseIndex.htm')#支付宝注册页面
time.sleep(5) #推迟5s执行

driver.switch_to.frame(driver.find_element_by_css_selector("body > div:nth-child(19) > div.alipay-xbox.alipay-xbox-show > div.alipay-xbox-content > iframe"))
driver.find_element_by_xpath('//*[@id="content"]/div[3]/a[1]/span').click()
tupian = driver.find_element_by_id('J-checkcode-img')
tupian.screenshot('./yanzheng.png')#?????这种方法记得有空请教一下  现在是根据坐标定位
# driver.save_screenshot('yanzheng.png')#另外一种方法 更具屏幕位置截图
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=DxUWMVcUDbL3cE5fO1YbXv04&client_secret=2wd66hNR7OmGssOTEqP4lRt4NpIgf8KU'
res = requests.get(host)
r = res.json()
print(r)
token = r['access_token']
print(token)
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token='+token
f = open(r'./yanzheng.png','rb')
img = base64.b64encode(f.read())
params = {"image":img}
imageres = requests.post(url,data=params)
image_json = imageres.json()
print(image_json)


image_num = image_json['words_result'][0]['words']
print(image_num)
time.sleep(4)
driver.quit()
# driver.find_element_by_id('imagecode1').send_keys(image_num)
