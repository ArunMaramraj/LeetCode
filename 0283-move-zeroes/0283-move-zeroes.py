class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        j = 0 
        
        n = len(nums)-1
        
        while j<=n:
            if nums[i]!=0:
                i+=1
                j+=1
            
            else:
    
                while j<=n and nums[j]==0:
                    j+=1
                    
                if j<=n:
                    nums[i],nums[j] = nums[j],nums[i]
                    i+=1
                    j+=1
        
        return nums
        
        