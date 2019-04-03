# -*- coding:utf-8 -*-
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
ar = [1, 2, 3, 4, 6]
b = sorted(ar, key=lambda c: c % 2, reverse=True)  # 按照key = 是否被2整除排序（即奇偶数） 但是会偶数在前；所以加reverse=true
print b


def reOrderArray(array):
    eve = []
    odd = []
    for i in array:
        odd.append(i) if i % 2 == 1 else eve.append(i)
    return odd + eve


print reOrderArray([1, 2, 3, 4, 6])
