class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = []
        
        for i in range (len(triangle)):
            dp.append([0]*(i+1))
            
        for i in range(len(triangle)):
            l = len(triangle[i])
            for j in range(l):
                
                ele = triangle[i][j]
                
                if i==0:
                    dp[i][j] = ele
                    
                elif j==0:
                    dp[i][j] = dp[i-1][j] + ele
                
                elif j == l - 1:
                    dp[i][j] = dp[i-1][j-1] + ele
                    
                else:
                    dp[i][j] = min(dp[i-1][j-1] , dp[i-1][j]) + ele
        
        return min(dp[-1])
                    
        
        
        