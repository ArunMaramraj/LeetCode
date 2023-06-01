class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        m = len(grid)
        n = len(grid[0])
        vis = set()
        count = 0
        tempcount = 0
        
        
        def dfs(i,j):
            nonlocal tempcount
            if (i>=m or i<0 or j>=n or j<0 or grid[i][j]!=1 or (i,j) in vis):
                return
            
            vis.add((i,j))
            
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
            
            tempcount+=1
        
        for i in range (m):
            for j in range (n):
                if(grid[i][j]==1 and (i,j) not in vis):
                    dfs(i,j)
                    count  = max(count,tempcount)
                    tempcount=0
        return count
                    