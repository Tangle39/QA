# -*- coding: utf-8 -*-
# coding = utf-8   #感觉这个更简单,但是不一定好用
#首先要找到能提出**version的文件目录字符串，暂时存到reslist里   17/9/22
import re
import csv #csv模块
import os
import re
rootdir = 'C:/Users/Administrator/Desktop/20170921164134/txt'
f='C:/Users/Administrator/Desktop/20170921164134/txt/prop'
os.remove(f)

# for parent, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         if filename=='show version.txt':
#             print filename
#         if filename=='display version.txt':
#             print filename


#uroo=unicode(rootdir,'utf-8')    #能显示中文

f_list = os.listdir(rootdir)
root=[]
#print f_list

# for i in list:
#     9
#     print ("序号：%s   值：%s" % (list.index(i) + 1, i))
for i in range(f_list.__len__()):
    r= 'C:/Users/Administrator/Desktop/20170921164134/txt/'+str(f_list[i])
    root.append(r)
#print root
#root现在是一个list  存了这么多子目录，子目录下有需要找的***version
reslist=[]
for i in root:
    rootdir=i
    print rootdir
    f_list = os.listdir(rootdir)
    #print f_list
    for j in f_list:
        if j=='display version.txt':
            reslist.append(i+'/'+j)
        if j=='show version.txt':
            reslist.append(i+'/'+j)
print reslist
