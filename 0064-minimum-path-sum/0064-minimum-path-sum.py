class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0]*n for i in range(m)]
        
        dp[0][0] = grid[0][0]
            
        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1,m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        def compute():
            
            for row in range(1,m):
                for col in range(1,n):
                        dp[row][col] = min(dp[row-1][col] , dp[row][col-1]) + grid[row][col]
                        
            return dp[m-1][n-1]
        
        return compute()
    