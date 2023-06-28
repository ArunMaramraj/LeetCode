class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        
        W = maxPts
        K = k
        N=n
        # Write your code here.
        if K == 0: 
            return 1.0
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            if i < K: 
                Wsum += dp[i]
            if i - W >= 0 and i-W<k: 
                Wsum -= dp[i - W]
        return sum(dp[K:])