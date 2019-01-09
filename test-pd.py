# -*- coding: utf-8 -*-

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
#print t
t1 = df1[ lambda df1:  df1[u'使用起始时间'] < end_time  ]
#取<end time的那行
print t1
