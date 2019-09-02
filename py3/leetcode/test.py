# s = 'abac'
# print(s[3])
# print(s[0:4])
# dp=[[False]*len(s)]*len(s)
# dp1 = [[False for _ in range(4)] for _ in range(4)] #Python中对于无需关注其实际含义的变量可以用_代替
# print(dp)
# print(dp1)
# print(dp == dp1)
# N = [[0]*10 for i in range(10)]
# print(N)
# M=[[False]*4 for i in range(4)]
# print(M)
# W =[5]*6
# W[1]=4
# print(W)
# print(-int('12'))
# print(*[1], *[2], 3)
# print([1,2],[2],3)
#
# l=['12']
# b = int(*l)
# c = l[0]
#
# print(b+6)
# print(b+6== 6+int(c))
# print(*l)
#
# print(5%2)
#
# dict3 = {(1,2,3): "uestc"}
# print('\\123456\123456\t')    # >>\123456S456
# print(["%02d:%02d"%(h,m) for h in range(0, 24) for m in range(0, 60, 5)])
l =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x for x in l if x%2 ==1])
add=lambda x, y: x+y
print(add(1,2))