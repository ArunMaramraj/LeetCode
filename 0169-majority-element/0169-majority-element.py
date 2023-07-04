class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        candidate = None
        count = 0
        
        for i in range(n):
            if count == 0 :
                count = 1
                candidate = nums[i]
                
            elif nums[i] == candidate:
                count+=1
            
            else:
                count-=1
        
        return candidate