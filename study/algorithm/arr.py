# -*- coding:utf-8 -*-
'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n = len(array)
        flag = 'false'
        for i in range(n):
            if target in array[i]:
                flag = 'true'
                break
        return flag
while True:
    try:    #输入正确时连续测试？
        S=Solution()
        # 字符串转为list
        L=list(eval(raw_input()))
        #eval功能：将字符串str当成有效的表达式来求值并返回计算结果。(type(a):a的类型）
        array=L[1]
        target=L[0]
        print(S.Find(target, array))
    except:
        break

