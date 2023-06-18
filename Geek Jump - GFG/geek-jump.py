#User function Template for python3

class Solution:
    def minimumEnergy(self, height, n):
        # Code here


    # Write your code here.
        cost = [-1]*len(height)
    
        cost[0] = 0
        
        for i in range (1,len(height)):
            if i==1 : 
                cost[1] = abs(height[1] - height[0])
            else:
                cost[i] = min(cost[i-1]+abs(height[i-1] - height[i]) , 
                                    cost[i-2] + abs(height[i-2] - height[i]))
        
    
        return cost[-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends