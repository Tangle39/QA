# -*- coding: utf-8 -*-
#允许中文注释

import csv  #csv格式，类似txt结合excel
import re #正则模块
import os #文件处理模块
import string  #字符串

fres = open('C:/Users/Administrator/Desktop/res.csv', 'wb')
writer=csv.writer(fres)
writer.writerow(['hostname','loopback','uptime'])
rootdir = 'C:/Users/Administrator/Desktop/log'
rootdir = 'C:/Users/Administrator/Desktop/log'

for parent, dirnames, filenames in os.walk(rootdir):
    i=0
    for filename in filenames:
        i=i+1
        f = open('C:/Users/Administrator/Desktop/log/'+str(filename))
        lines = f.read()
        #hostname
        t = re.findall('hostname.+',lines)
        t_convert = ''.join(t)
        list = t_convert.split('hostname')
        fres.write(list[1])

        #loopback
        t = re.findall('interface Loopback0.*\n ip address \S*', lines)
        t_convert = ''.join(t)
        list = t_convert.split(' ')
        fres.write(','+list[-1])

        #uptime
        t = re.findall('uptime.+', lines)  # findall进行正则匹配，不知为何compile不行了o.o
        # .：非换行任意字符，+：1次或任意次数；*：前一个字符0次或任意次
        t_convert = ''.join(t)  # list转string
        list = t_convert.split(' ')  # 根据空格切片
        y=0
        w=0
        d=0
        if ('year,' in list):  # 提取年、周...转换类型计算
            y = list[list.index('year,') - 1]      #index能返回元素在list的第一个匹配位置
        if ('years,' in list):
            y = list[list.index('years,') - 1]
        if ('weeks,' in list):
            w = list[list.index('weeks,') - 1]
        if ('week,' in list):
            w = list[list.index('week,') - 1]
        if ('days,' in list):
            d = list[list.index('days,') - 1]
        if ('day,' in list):
            d = list[list.index('day,') - 1]
        y = int(y)
        w = int(w)
        d = int(d)
        days = 365 * y + 7 * w + d
        fres.write(','+str(days)+'\n')
    print '总共'+str(i)+'个文件'
fres.close()
