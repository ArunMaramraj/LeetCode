class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        dp = [[-1]*n for i in range(m)]
        
        def compute(i,j):
            
            if i<0 or j<0 :
                return 0
            
            if i==0 and j==0:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = compute(i-1,j)
            left = compute(i,j-1)
            
            dp[i][j] = up + left
            
            return dp[i][j]
        
        
        return compute(m-1,n-1)