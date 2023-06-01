from typing import List

class Node:
    def __init__(self, i, j, count):
        self.i = i
        self.j = j
        self.count = count

class Solution:    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[0] * n for _ in range(m)]
        queue = []
        output = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append(Node(i, j, 0))
                    vis[i][j] = 2
                    
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1] 
        
        while len(queue) != 0:
            temp = queue.pop(0)
            row, column, time = temp.i, temp.j, temp.count
           
            output = max(output, time)
            
            for i in range(4):
                nrow = row + drow[i]
                ncol = column + dcol[i]
                
                if (nrow >= 0 and nrow < m and ncol >= 0 and ncol < n 
                        and grid[nrow][ncol] == 1 and vis[nrow][ncol] != 2):
                    queue.append(Node(nrow, ncol, time + 1))
                    vis[nrow][ncol] = 2
                    
        for i in range(m):
            for j in range(n):
                if vis[i][j] != 2 and grid[i][j] == 1:
                    return -1
                
        return output
