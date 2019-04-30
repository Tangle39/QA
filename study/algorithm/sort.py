# -*- coding: utf8 -*-
# python快排 神优雅
'''快排思路：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
'''
L = [1, 3, 5, 7, 8, -2, 55, -55]
print L


def qsort(L):  # 变量最好小写
    if len(L) <= 1: return L       #递归出口！
    return qsort([lt for lt in L[1:] if lt < L[0]]) + \
           [L[0]] + qsort([lt for lt in L[1:] if lt >= L[0]])  # \换行 [L[0]]使得变成list;


#  [...]可以使里面的结果形成list！  [...]+[L[0]]+[...]刚好为一次快排

# 冒泡


def bubble_sort(L):
    for i in range(len(L) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(L) - i - 1):  # j为列表下标
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]  # 交换
    return L


#print bubble_sort(L)

# print L
print qsort(L)
# print L
