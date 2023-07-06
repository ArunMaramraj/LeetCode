class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        text1 = s
        text2 = s[::-1]
        
        n,m = len(text1),len(text2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if j==0:
                    dp[i][j] = 0
                elif i==0:
                    dp[i][j] =0 
                else:
                    if text2[i-1] == text1[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        return dp[-1][-1]