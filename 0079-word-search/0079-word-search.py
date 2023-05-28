class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        s = ""
        index = 0
        m = len(board)
        n = len(board[0])
        booli = False
        
        tempset = set() 
        
        def compute(i, j):
            nonlocal booli
            nonlocal index
            nonlocal s
            nonlocal tempset  
            
            if booli:
                return
            
            if i >= m or i < 0 or j >= n or j < 0 or word[index] != board[i][j] or (i, j) in tempset:
                return 
            
            s += board[i][j]
            index += 1
            
            if s == word:
                booli = True
                return
            
            tempset.add((i, j))
            
            compute(i, j + 1)
            compute(i, j - 1)
            compute(i + 1, j)
            compute(i - 1, j)
            
            index -= 1
            s = s[:-1]
            tempset.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                if booli:
                    break
                else:
                    compute(i, j)
        
        return booli
