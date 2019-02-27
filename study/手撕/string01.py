# -*-coding:utf8 -*-
'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，
当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
'''
# -*- coding:utf-8 -*-



class Solution:
    def __init__(self):
        self.s = ""

    def FirstAppearingOnce(self):
        res = list(filter(lambda c: self.s.count(c) == 1, self.s))
        '''匿名函数lambda x: x * x 即
        def f(x):
            return x * x
        filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
        filter(function, iterable)
       Pyhton2.7返回列表，Python3.x返回迭代器对象
       '''
        return res[0] if res else "#"

    def Insert(self, char):
        self.s += char

a = Solution()
a.Insert('#g#')

print a.FirstAppearingOnce()
