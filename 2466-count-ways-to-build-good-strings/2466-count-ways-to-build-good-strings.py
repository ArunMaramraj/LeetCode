class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = {0:1}
        
        mod = 10**9 + 7
        
        
        for i in range(1,high+1):
            dp[i] = dp.get(i-zero,0) + dp.get(i-one,0)
        
        
        return sum(dp[i] for i in range(low,high+1))%mod
        
        
        
#         def compute(length):
#             if length>high:
#                 return 0
            
#             if length in dp:
#                 return dp[length]
            
#             if length>=low:
#                 dp[length]=1
#             else:
#                 dp[length] = 0
                
#             dp[length]+=compute(length+zero) + compute(length+one)
            
            
                