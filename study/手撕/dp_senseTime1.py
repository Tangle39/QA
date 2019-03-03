# -*- coding:utf-8 -*-
'''
有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。
现在给一串数字，给出有多少种可能的译码结果。
'''
#解法1，后面没看 请看2
s = raw_input().strip()
#strip(): 用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
n = len(s)
legal = set(map(str,range(1,27)))
'''range(1,27:[1~26], str:string
 map(func,iter1,iter2):它接收一个函数 f
 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
 set: 无序不重复元素集
legal：set(['24', '25', '26', '20', '21', '22', '23', 
'1', '3', '2', '5', '4', '7', '6', '9', '8', 
'11', '10', '13', '12', '15', '14', '17', '16', '19', '18'])
'''
#print n
#print legal
char = lambda x:1 if x in legal else 0
#print char
data = {}
#s = "20"
if n == 0:
    print 0
elif n==1: #else if
    print char(s)
else:
    data[0] = char(s[0])*char(s[1])
    data[1] = char(s[0])*char(s[1])+char(s[:2])

    for i in range(2,n):# 2~1
        data[i] =data[i-1]*char(s[i])+data[i-2]*char(s[i-1:i+1])
    print data[n-1]

