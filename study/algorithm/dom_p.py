# -*- coding: utf-8 -*-
'''
支配数：数组中某个元素出现的次数大于数组总数的一半时就成为支配数，其所在位序成为支配点；
比如int[] a = {3,3,1,2,3};3为支配数，0，1，4分别为支配点；
要求：返回任何一个支配点
'''

orgin = [3, 3, 1, 2, 3]
numbers = [3, 3, 1, 2, 3]  # 这里 = orgin是错误的 orgin也会被操作
# 进行排序 因为支配数数目大于整体的一半，所以找 中位数 一定为支配数
numbers.sort()
# 拿到长度便于比较
lens = len(numbers)
# 取到中位数
num = numbers[int(lens / 2)]
count = 0  # 计数
for nums in numbers:
    if nums == num:
        count += 1

# 打印答案
if count > lens / 2:
    print '支配数为---', num
    print '支配点：'
    for j, k in enumerate(orgin):
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标

        if k == num:
            print j
else:
    print("没有支配数")

    # 原文：https://blog.csdn.net/weixin_42784553/article/details/83338384

    # print 'sakubobo伯伯'
