# -*- coding: utf-8 -*-
#对跟目录下的所有文件，以文件夹的名字作为设备名、管理ip，文件，根目录作为uptime时间，文件夹下txt中的* version中有uptime参数
#整理所得数据到res.xls
#0930提取 name ip version bin到第二个sheet
import xlrd
import xlwt
import string
import os
import re

print 'start'    #flag开始
res=xlwt.Workbook() #新建表
s1=res.add_sheet('uptime')  #新建sheet
s2=res.add_sheet('version')
s1.write(0,0,u'设备名称')    #unicode
s1.write(0,1,u'管理IP')
s2.write(0,0,u'设备名称')    #unicode
s2.write(0,1,u'管理IP')
s2.write(0,2,'version')
s2.write(0,3,'BIN')

#设备名&管理地址
rootdir = '/Users/lu/Desktop/UP/20170921164134/txt'
time=rootdir.split('/')

s1.write(0,2,'uptime'+time[-2])   #第三列

f_list = os.listdir(rootdir)
#del f_list[1]    #删除隐藏文件.DS_store（mac特有的文件）,该文件的位置暂时还不确定；目前已经用bash删除所有.ds_store，并且禁止生成

for i in range(f_list.__len__()):
    list=str(f_list[i]).split('_')
    s1.write(i+1,0,list[-1])       #hostname在最后，ip在前
    s1.write(i+1,1,list[0])
    s2.write(i + 1, 0, list[-1])  # hostname在最后，ip在前
    s2.write(i + 1, 1, list[0])

    #uptime
    #1.找到所在的文件位置

    fname=os.path.join(rootdir,f_list[i])  #每次都是某个文件夹，无需二重循环。。- - 。 。 。
    #os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
    #print 'fname:'+fname

    f_list1 = os.listdir(fname)
    res0=''
    for j in f_list1:
        if j=='display version.txt':
            res0 = os.path.join(fname,j)
        if j=='show version.txt':
            res0 = os.path.join(fname,j)

    #2.正则匹配
    #2.1uptime(days)
    f=open(str(res0))
    lines=f.read()
    t = re.findall('uptime.+', lines)  # findall进行正则匹配，不知为何compile不行了o.o
    # .：非换行任意字符，+：1次或任意次数；*：前一个字符0次或任意次
    t_convert = ''.join(t)  # list转string
    list = t_convert.split(' ')  # 根据空格切片
    y = 0
    w = 0
    d = 0
    if ('year,' in list):  # 提取年、周...转换类型计算
        y = list[list.index('year,') - 1]  # index能返回元素在list的第一个匹配位置
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

    s1.write(i+1,2,days)   #写入

    #2.2version
    t1 = re.findall('Version \d{1,3}\.\d{1,3}', lines)   #\d数字  {1，2}1-2个   \.将.转译回.
    t_convert = ''.join(t1)  # list转string
    list = t_convert.split(' ')
    s2.write(i+1,2,list[-1])

    #2.3 BIN
    t2 = re.findall('flash:.+', lines)  # \d数字  {1，2}1-2个   \.将.转译回.
    t_convert = ''.join(t2)  # list转string
    l = t_convert.split(':')
    s0 = str(l[-1])
    l1 = s0.split('"')
    s2.write(i + 1, 3, l1[0])

res.save('res.xls')   #保存结果文件
