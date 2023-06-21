class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        
        n = len(matrix)
        dp = [[0]*n for _ in range(n)] 
        
        for i in range(n):
            for j in range(n):
                ele  = matrix[i][j]
                if i==0:
                    dp[i][j] = ele
                        
                elif j==0:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j+1]) + ele
                    
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1]) + ele
                    
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + ele
                    
                    
        return min(dp[-1])