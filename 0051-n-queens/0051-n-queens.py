import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        temp = [['.']*n for i in range(n)]
        output = []
        
        posD = set()
        negD = set()
        col = set()
        
        
        def compute(r):
            
            if r==n : 
                copy = ["".join(row) for row in temp]
                output.append(copy)
                return
            
            for c in range (n):
                if c in col or (r-c) in negD or (r+c) in posD : 
                    continue
                
                temp[r][c] = 'Q'
                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                
                
                compute(r+1)
                
                temp[r][c] = '.'
                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
        
        compute(0)
        return output