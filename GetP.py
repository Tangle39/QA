# -*- coding: utf-8 -*-
#允许中文注释
#需要提取文本夹下所有文本的一些信息(***有些需要转换格式****)，存到一个新文件res.txt中

import re #正则模块
import os #文件处理模块
import string  #字符串


fres = open('C:/Users/Administrator/Desktop/res.txt', 'w')
rootdir = 'C:/Users/Administrator/Desktop/log'
for parent, dirnames, filenames in os.walk(rootdir):
    i=0
    for filename in filenames:
        #print filename
        i=i+1
        fres.write(filename+',')  #记录一下文件名
        # 提取hostname/sysname
        f = open('C:/Users/Administrator/Desktop/log/'+str(filename))
        lines = f.readlines()  # .readlines() 自动将文件内容分析成一个行的列表，加快编译速度
        for line in lines:
            pattern = re.compile('(hostname|sysname).*')  # s:space;()分组
            match = pattern.match(line)
            if match:
                # 使用Match获得分组信息
                fres.write(match.group() + ',')  # Ctrl /可以注释多行
        f.close()

        # 提取uptime，将格式转换为days
        f1 = open('C:/Users/Administrator/Desktop/log/'+str(filename))  # 重新打开，不然无法成功写入
        lines = f1.read()
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
        fres.write('uptime  ' + str(days) + ',')  # 需进行类型转换
        f1.close()

        # loopback要提取的地址在下一行
        f2 = open('C:/Users/Administrator/Desktop/log/'+str(filename))
        lines = f2.read()
        t = re.findall('interface Loopback.+\n ip address \S*', lines)
        t_convert = ''.join(t)
        list = t_convert.split(' ')
        t = re.findall(' Loopback.+\n ip address \S*', lines)
        t_convert = ''.join(t)
        list = t_convert.split(' ')
        while 'ip' in list:
            list.remove('ip')  # 移除列表中某个值的第一个匹配项
        while 'address' in list:
            list.remove('address')
        # print list
        t_convert = ''.join(list)
        list = t_convert.split('\n')
        fres.write(str(list))
        fres.write('\n')
        f2.close()
    print i

fres.close()
