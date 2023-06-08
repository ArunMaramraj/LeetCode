class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = set()
        atl = set()
        m  = len(heights)
        n = len(heights[0])
        
        vis = [[0]*n for _ in range(m)]
        
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        
        output =[]
        
        def dfs(i,j,paci):
            
            paci.add((i,j))
                
            vis[i][j]=1
            
            for k in range(len(drow)):
                row = i + drow[k]
                col = j + dcol[k]
                if( row>=0 and row<m and col>=0 and col<n 
                   and heights[row][col]>=heights[i][j] and (row,col) not in paci and vis[row][col]==0):
                    dfs(row,col,paci)
                    
            vis[i][j]=0    
  
        
        for col in range(n):
            dfs(0,col,pac)
            dfs(m-1,col,atl)
        for row in range(m):
            dfs(row,0,pac)
            dfs(row,n-1,atl)  
                  
        common_ele = pac.intersection(atl)
        
        for ele in common_ele:
            output.append(list(ele))
        
        return output
        
        