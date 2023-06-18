#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		output = [-1]*n
		
		output[0] = arr[0]
		
		for k in range(1,n):
		    
		    inc = arr[k]
		    
		    if k>=2:
		        inc+=output[k-2]
		        
		    output[k] = max(inc,output[k-1])
		
		return output[-1]    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends