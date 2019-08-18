'''
dp[i]= dp[i-1]+2
dp[i]+= dp[i-dp[i-1]-2]
dp[i]=0 s[i]为左括号

'''
s = input()
l = len(s)
dp = [0 for _ in range(l+1)]
for i in range(1,l):
    if s[i]== ')':
        if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]== '(':
            dp[i] = dp[i-1]+2
            if i-dp[i-1]-2>=0:
                dp[i]+=dp[i-dp[i-1]-2]

print(max(dp))