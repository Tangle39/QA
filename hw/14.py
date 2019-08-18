# 给定n个字符串，请对n个字符串按照字典序排列。
n = int(input())
res = []
for i in range(n):
    res.append(input())
res = sorted(res)
for i in res:
    print(i)