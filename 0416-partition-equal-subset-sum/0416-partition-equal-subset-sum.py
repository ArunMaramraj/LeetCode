class Solution:
    def canPartition(self, nums: List[int]) -> bool:
         
        target_sum = sum(nums)
        
        if target_sum%2!=0:
            return False
        
        target_sum = target_sum//2
        
        N = len(nums)
        
        dp = [[False for j in range(target_sum+1)] for i in range(N)]
        
        
        def compute(N,target):
            
            for i in range(N):
                dp[i][0] = True
            
            if nums[0]<=target:
                dp[0][nums[0]] = True
                
            for i in range(1,N):
                for j in range(1,target+1):
                    
                    if nums[i]>target:
                        dp[i][j] = dp[i-1][j]
                        
                    elif nums[i]==target:
                            dp[i][j] = True
                    else:
                        dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
                    
            return dp[N-1][target]
            
        return compute(N,target_sum) 

    
#     class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
        
#         total = sum(nums)
        
#         if total%2!=0:
#             return False
        
#         target_sum = total//2
        
#         n = len(nums)
        
#         def compute(index,curr_sum):
            
#             if curr_sum>target_sum or index>=n:
#                 return False
            
#             if curr_sum == target_sum:
#                 return True
            
#             if compute(index+1,curr_sum+nums[index]):
#                 return True
            
#             if compute(index+1,curr_sum):
#                 return True
            
#             return False
        
#         return compute(0,0)