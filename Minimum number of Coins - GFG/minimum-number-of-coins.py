#User function Template for python3
class Solution:
    def minPartition(self, N):
        
        arr = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        T = N
        n = len(arr)
        dp = [[0 for _ in range(T + 1)] for _ in range(n)]
        
        for i in range(T + 1):
            if i % arr[0] == 0:
                dp[0][i] = i // arr[0]
            else:
                dp[0][i] = 0
        
        for ind in range(1, n):
            for target in range(T + 1):
                notTake = 0 + dp[ind - 1][target]
                take = float('inf')
                if arr[ind] <= target:
                    take = 1 + dp[ind][target - arr[ind]]
                dp[ind][target] = min(notTake, take)
        
        
        result = []
        i = n - 1
        j = T
        while i >= 0 and j > 0:
            if i == 0:
                result.append(arr[i])
                j -= arr[i]
            elif dp[i][j] != dp[i - 1][j]:
                result.append(arr[i])
                j -= arr[i]
            else:
                i -= 1

        return result
                        
                        
                        
                        
                        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends