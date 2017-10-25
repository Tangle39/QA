## -*- coding: UTF-8 -*-

# 10/28
# 先检查excel红色行的配置是否正确
# 准备：先从word里保存r1的cisco正确配置ciscofirewall.txt

import re
r1='/Users/lu/Desktop/UP/配置文件/SHSHFW01005__144.20.9.6__2017-01-11.txt'
f1=open(r1,'r')
lines=f1.read()

fres = open("CheckRes.txt", 'w+')
n=r1.split('/')
fres.write('    ******'+n[-1]+'*********'+'\n')
#找出sh...中的类似ciscofirewall的行

str1=re.findall('snmp-server host.+',lines)

#运用compare方法，进行比对检查
str2=[]
fb = open("ciscofirewall.txt", 'r')
for line in fb.readlines():
    str2.append(line.replace("\n", ''))

str_dump = []
for i in str1:
    if i in str2:
        str_dump.append(i)

for i in str_dump:
    if i in str1:
        str1.remove(i)

for i in str_dump:
    if i in str2:
        str2.remove(i)
#print str1
#print str2
#写行文件中
for i in str2:
    fres.write('del: '+i+'\n')

for i in str1:
    fres.write('add: '+i+'\n')



fb.close()
fres.close()
#第二个文件貌似没有找到相应配置？