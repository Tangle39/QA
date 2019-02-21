# -*- coding:utf8 -*-
import requests
import os

'''payload = {'key1': '咲く伯伯', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
'''
#r = requests.get('https://www.baidu.com')
#print r.content
#print r
#print r.json()

#京东
'''url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败！")
'''

#亚马逊
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
   # kv = {'user-agent':'Mozilla/5.0'}
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
   # print(r.status_code)
    print(r.text[:1000])
except:
    print("爬取失败")

#百度
'''url="http://www.baidu.com/s"
try:
    kv={'wd':'Python'}
    r=requests.get(url,params=kv)
  #  print(r.request.url)
   # r.raise_for_status()
   # print(len(r.text))
    print(r.text[:500])
except:
    print("爬取失败")
'''
#网络图片的爬取和存储--结合os库和文件操作的使用

url="http://tc.sinaimg.cn/maxwidth.800/tc.service.weibo.com/p3_pstatp_com/6da229b421faf86ca9ba406190b6f06e.jpg"
root="/Users/lu/Documents/Code/QA/image/"
path=root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")


'''--------------------- 
 
原文：https://blog.csdn.net/i_chaoren/article/details/63266154 

'''


