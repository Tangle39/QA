s = 'abac'
print(s[3])
print(s[0:4])
dp=[[False]*len(s)]*len(s)
dp1 = [[False for _ in range(4)] for _ in range(4)] #Python中对于无需关注其实际含义的变量可以用_代替
print(dp)
print(dp1)
print(dp == dp1)
N = [[0]*10 for i in range(10)]
print(N)
M=[[False]*4 for i in range(4)]
print(M)
W =[5]*6
W[1]=4
print(W)