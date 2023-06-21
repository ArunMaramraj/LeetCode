#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, n, m, grid):
        
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        
        def compute(i,j1,j2,dp):
            
            if i<0 or j1<0 or j2<0 or j1>=m or j2>=m:
                return -1e8
            
            if i==n-1:
                if j1==j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]
            
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
            
            maxi = -1e8
            
            
            for dj1 in range(-1,2):
                for dj2 in range(-1,2):
                    value  = 0
                    if j1==j2:
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]
                        
                    value+=compute(i+1,j1+dj1,j2+dj2,dp)
        
                    maxi = max(maxi,value)
        
            
            dp[i][j1][j2] = maxi
            
            return maxi
        
        return compute(0,0,m-1,dp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(n)]
        obj = Solution()
        res = obj.solve(n, m, grid)
        print(res)
# } Driver Code Ends