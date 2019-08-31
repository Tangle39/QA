class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            b = int(str(x)[::-1])
            if b > 2**31 -1:return 0
            else:return b
        else:
            b = int(str(-x)[::-1])
            if b > 2 ** 31 - 1: return 0
            else:return -b

s = Solution()
print(s.reverse(1534346469))