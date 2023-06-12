from heapq import heappop,heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
     
        pq = [(grid[0][0],0,0)]
        
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        
        vis  = set()
        
        while True:
            
            ele, row, col = heappop(pq)
            
            if row==n-1 and col == n-1:
                return ele
                
            for k in range(len(drow)):
                next_row = row + drow[k]
                next_col = col + dcol[k]
                
                if 0<=next_row<=n-1 and 0<=next_col<=n-1 and (next_row,next_col) not in vis:
                    heappush(pq,(max(ele,grid[next_row][next_col]),next_row,next_col))
                    vis.add((next_row,next_col))
                    
            
        
        
        