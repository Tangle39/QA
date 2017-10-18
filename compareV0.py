# -*- coding: UTF-8 -*-
import re
import sys
import os

"""
关于read()方法：
1、读取整个文件，将文件内容放到一个字符串变量中
2、如果文件大于可用内存，不可能使用这种处理
"""
"""
关于readline()方法：
1、readline()每次读取一行，比readlines()慢得多
2、readline()返回的是一个字符串对象，保存当前行的内容
"""
"""
关于readlines()方法：
1、一次性读取整个文件。
2、自动将文件内容分析成一个行的列表。
"""

#10/18
#task:比较两个文件夹内所有同名文件的增删（改），结果放到res中
#先写循环遍历文件夹，找到同名文件，保存路径

root1='/Users/lu/Desktop/UP/Compare/20171016'
root2='/Users/lu/Desktop/UP/Compare/20171017'

flist1=os.listdir(root1)

flist2=os.listdir(root2)


#用之前写的程序来做循环处理比较
#先保存了需要比较的路径rc1、rc2
'''格式：
主机 ip date
del：***
add：***
'''
fres = open("resCompare.txt", 'w+')
ld=root2.split('/')
date=ld[-1]

for i in flist1:
    for j in flist2:
        if i==j:
            fres.write(j+' '+date+'\n')
            rc1=os.path.join(root1,j)

            rc2 = os.path.join(root2, j)

            str1 = []
            str2 = []
            str_dump = []
            fa = open(rc1, 'r')
            fb = open(rc2, 'r')


            # 将A.txt的内容逐行读到str1中
            for line in fa.readlines():
                str1.append(line.replace("\n", ''))

            # 将B.txt中的内容逐行读到str2中
            for line in fb.readlines():
                str2.append(line.replace("\n", ''))

            # 将两个文件中重复的行，添加到str_dump中
            for i in str1:
                if i in str2:
                    str_dump.append(i)

            # 将两个文件的行合并，并去重
            #str_all = set(str1 + str2)   #set是按hashtable排序
            #将重复的行remove掉，剩下的就是不重复的行了
            for i in str_dump:
                if i in str1:
                    str1.remove(i)

            for i in str_dump:
                if i in str2:
                    str2.remove(i)
            #print str1
            #print str2
            #写行文件中
            for i in str1:
                fres.write('del: '+i+'\n')

            for i in str2:
                fres.write('add: '+i+'\n')

            fres.write('\n')
            fa.close()
            fb.close()
fres.close()