class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)
        
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        
        def dfs(i, j, index):
            if index == word_len:
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"  # Mark the cell as visited
            
            for k in range(len(drow)):
                next_row = i + drow[k]
                next_col = j + dcol[k]
                
                if dfs(next_row, next_col, index + 1):
                    return True
            
            board[i][j] = temp  # Restore the cell's original value
            
            return False
                            
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
