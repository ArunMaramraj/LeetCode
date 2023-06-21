#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        
        
        
        dp = [[-1 for j in range(sum+1)] for i in range(N+1)]
        
        
        def compute(ind,target):
            
            if target == 0:
                return True
    
            if ind == 0:
                return arr[0] == target
        
            if dp[ind][target] != -1:
                return dp[ind][target]
        
            notTaken = compute(ind-1, target)
        
            taken = False
            
            if arr[ind] <= target:
                taken = compute(ind-1, target-arr[ind])
        
            dp[ind][target] = notTaken or taken
            
            return dp[ind][target]

        if compute(N-1, sum) == True:
            return 1
            
        return 0    
           
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends