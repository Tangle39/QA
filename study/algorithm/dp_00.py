# -*- coding:utf-8 -*-
# 最大连续子序列和
l = [-2, 11, -4, 13, -5, -2, 8]
# max = 11-4+13 =20
'''
动态规划 复杂度O(n)
步骤1：令dp[i]为以A[i]作为末尾的连续序列的最大和
步骤2：
两种情况：
1.最大连续序列只有1个元素，A[i],此时最大和s = A[i]
2.多个元素，从A[p]到A[i],p<i,此时s = dp[i-1]+A[i]
得 状态转移方程：
    dp[i] = max{A[i],dp[i-1]+A[i]}
从小到大枚举i得dp数组，数组的最大值即为最大连续子序列

'''
dp = [l[0]]

s = l[0]
for i in range(1, len(l)):
    tmp = max(l[i], dp[i - 1] + l[i])
    dp.append(tmp)
print max(dp)  # 20
