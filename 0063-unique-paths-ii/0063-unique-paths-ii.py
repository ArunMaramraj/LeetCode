class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for i in range(m)]
        
        
        
        def compute():
            
            for row in range(0,m):
                for col in range(0,n):
                    
                    if obstacleGrid[row][col] == 1:
                        dp[row][col] = 0
                        continue
                    
                    elif row==0 and col==0 :
                        dp[row][col] = 1
                        continue
                    
                    up = 0
                    left = 0
                    
                    if col>0:
                        left = dp[row][col-1]
                    if row>0:
                        up = dp[row-1][col]
                        
                    dp[row][col] = up + left    
                        
            return dp[m-1][n-1]            
                        
                         
                       
        return compute()
    
    
                