class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)
        
        # Create a DP table to store the state of subproblems
        dp = [[False] * n for _ in range(m)]
        
        def dfs(i, j, index):
            # Base case: If we have reached the end of the word, return True
            if index == word_len:
                return True
            
            # Check for out-of-bounds indices or mismatching characters
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False
            
            # If the subproblem has already been solved, return the result from the DP table
            if dp[i][j]:
                return False
            
            # Mark the subproblem as being solved
            dp[i][j] = True
            
            # Explore the four neighboring cells
            found = (
                dfs(i + 1, j, index + 1)
                or dfs(i - 1, j, index + 1)
                or dfs(i, j + 1, index + 1)
                or dfs(i, j - 1, index + 1)
            )
            
            # Update the DP table with the result of the subproblem
            dp[i][j] = False if not found else True
            
            return found
                            
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
