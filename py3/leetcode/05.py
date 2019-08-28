#最长回文字符串
def longestPalindrome(s: str) -> str:
    size = len(s)
    if size <= 1: return s
    dp = [[False for _ in range(size)] for _ in range(size)]  # n*n的false 二维数组的写法？ #使用 * 语法创建的是引用，引用的意思就是“改一个，复制出来的另一个也跟着改了”。
    longest_l = 1
    res = s[0]
    for r in range(1, size):
        for l in range(r):
            # 状态转移方程：如果头尾字符相等并且中间也是回文
            # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
            # 否则要继续看收缩以后的区间的回文性
            # 重点理解 or 的短路性质在这里的作用
            if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                dp[l][r] = True
                cur_len = r - l + 1
                if cur_len > longest_l:
                    longest_l = cur_len
                    res = s[l:r + 1]

    return res


print(longestPalindrome('poppopo'))
