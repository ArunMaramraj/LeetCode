#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        
        dp = [[0]*(W+1) for _ in range(n)]
        
        def compute():
            
            for i in range(n):
                dp[i][0] = 0
            
            
            if wt[0]<=W:
                index = wt[0]
                for j in range(index,W+1):
                    dp[0][j] = val[0]
                    
            
            for i in range(1,n):
                for j in range(1,W+1):
                    
                    if wt[i]>j:
                        dp[i][j] = dp[i-1][j]
                        
                    else:
                        dp[i][j] = max(dp[i-1][j] , val[i]+dp[i-1][j-wt[i]])
                    
            
            
        compute()
        
        return dp[n-1][W]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends