# -*- coding: utf-8 -*-
#pd：pandas
import pandas,time
file =r'test0.xlsx'
df1 = pandas.read_excel(file)
#print df1    #rows x  columns

start_time = pandas.datetime(2019,1,7,00,51,51)

end_time=pandas.datetime(2019,1,8,18,7,48)

#print end_time  #2019-01-08 18:07:48

'''
读取某个时间列
'''
print '1）读取某个时间列:'
#方法1(推荐）
series_time = df1[u'使用起始时间']
#起始时间的列  默认format="%m %d %H %M %S"
#print series_time
'''0   2019-01-08 18:07:49
1   2019-01-07 11:28:27
Name: 使用起始时间, dtype: datetime64[ns]
'''

#方法2 loc函数
t = df1.loc[:,u'使用起始时间']
print t,'\n'  #\n换行

#lambda函数
print '2）lambda函数:(比较） 输出小于endtime的行'
t1 = df1[ lambda df1:  df1[u'使用起始时间'] < end_time  ]
#df1中，取<end time的那行
'''lambda函数有如下特性：

lambda函数是匿名的

lambda函数有输入和输出

lambda函数一般功能简单
原文：https://blog.csdn.net/zjuxsl/article/details/79437563 
lambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
lambda **kwargs: 1；输入是任意键值对参数，输出是1
'''
print t1,'\n'

print '3) 取指定的行/列，计算求和等'
free_data = df1[df1[u'网络类型']=='4G'] #取4g的行
#print free_data
free_data_sum = free_data['flow'].sum()    #取flow列  相加
print "总流量",free_data_sum



