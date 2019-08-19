'''
dp[i]= dp[i-1]+2   #i-1-f(i)表示之前还未匹配的(    {小区间的}
   #要加上以箭头前一位置结尾的最大长度 f(i)=f(i)+f(i−f(i))  if  i>f(i)
dp[i]=0 s[i]为左括号

'''
# 动态规划
s = input()
l = len(s)
dp = [0]*(l+1)  #不加1 会有空列表的问题？
for i in range(1,l):
    if s[i]== ')':
        if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]== '(':
            dp[i] = dp[i-1]+2
            if i-dp[i]>=0:
                dp[i]+=dp[i-dp[i]]

print(max(dp))
