money=[1,5,10,20,50]
dp= []
dp[0] = 1
# for(int i = 0;i < 6;++i){
#             for(int j = money[i];j <= n;++j){
#                 dp[j] =(dp[j]+dp[j-money[i]]);
#             }
#         }

print(dp[n]);