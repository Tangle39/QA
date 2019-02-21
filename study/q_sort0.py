# -*- coding: utf8 -*-
#python快排 神优雅
'''通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
'''
def qsort(L):
	if len(L) <= 1: return L
	return qsort([lt for lt in L[1:] if lt < L[0]]) +\
           [L[0]] + qsort([lt for lt in L[1:] if lt >= L[0]])  #\换行 [L[0]]使得变成list;
    # [...]可以使里面的结果形成list！  [...]+[L[0]]+[...]刚好为一次快排

L = [1,3,5,7,8,-2,55,-55]
l = qsort(L)
print l