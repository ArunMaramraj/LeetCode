class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        
        T = amount
        n = len(coins)
        dp = [[0 for _ in range(T + 1)] for _ in range(n)]
        
        for i in range(T + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
        
        for i in range(n):
            dp[i][0] = 1
        
        for ind in range(1, n):
            for target in range(T + 1):
                nottake = dp[ind - 1][target]
                take = 0
                if coins[ind] <= target:
                    if dp[ind][target-coins[ind]]!=0:
                        take +=  dp[ind][target - coins[ind]]
                dp[ind][target] = take + nottake
        
        
        return dp[-1][-1]