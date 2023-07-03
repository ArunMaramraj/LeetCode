class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        


        l = 0
        r = 0
        output = 0
        
        maxi = 0

        while r < len(nums):
         
            
            if nums[r]>threshold:
                l = r+1
                       
            
            elif r!=l and nums[r-1]%2 == nums[r]%2:
                l=r        
            while l<=r and nums[l]%2!=0:
                l+=1
                
                 
            maxi = max(maxi, r-l+1)
            r+=1
            
        return maxi    
            
 