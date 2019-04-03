# -*- coding:utf-8 -*-
# n = 5
# print bin(n)
# print bin(n).replace('0b','').count('1')

# 原码表示法在数值前面增加了一位符号位（即最高位为符号位）：
# 正数该位为0，负数该位为1（0有两种表示：+0和-0），其余位表示数值的大小。
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。



正整数的补码是其二进制表示，与原码相同
求负整数的补码，将其原码除符号位外的所有位取反（0变1，1变0，符号位为1不变）后加1
技巧：对于二进制来说，先减一后取反和先去反后加一结果一样
'''


class Solution:
    def NumberOf1(self, n):
        return bin(n).replace('0b', '').count('1') \
            if n >= 0 else bin(2 ** 32 + n).count('1')  # replace其实没有必要 #count计数

    def NumberOf12(self, n):
        return bin(n & 0xffffffff).count('1')  # 通用正负数
        # 负数 +2^32


s = Solution()
print bin(-1)
print s.NumberOf12(-1)
print s.NumberOf1(-1)
