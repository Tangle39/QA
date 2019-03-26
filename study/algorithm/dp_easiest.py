# -*- coding:utf-8 -*-
#大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
#n<=39

class Solution:
    def Fibonacci(self, n):
        # write code here
        res=[0,1]
        while len(res)<=n:
            res.append(res[-1]+res[-2])
        return res[n]
s = Solution()
for n in range(0,10):#从0开始，10个
    print s.Fibonacci(n),  #,使之不换行  py2  ，py3：  end="" 可使输出不换行
# for n in range(0,10):
#     print n换行
l = [1,2,3,4,5]
print l[-2]