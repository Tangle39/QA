class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c   #注意是+=
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

b = Solution()
print(b.convert('abcdef',3))

'''
res[i] += c：把每个字符c填入对应行 s_is 
i
​	
  ；
i += flag：更新当前字符c对应的行索引；
flag = - flag：在达到 ZZ 字形转折点时，执行反向。


'''