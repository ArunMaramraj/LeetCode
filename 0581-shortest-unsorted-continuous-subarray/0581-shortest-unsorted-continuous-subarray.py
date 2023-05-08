class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1
        
        if(len(nums)==1):
            return 0
        
        while(l<len(nums)-1 and nums[l]<=nums[l+1]):
            l+=1
        while(r>=1 and nums[r]>=nums[r-1]):
            r-=1
       
        if(r== 0 and l == len(nums)-1):
            return 0
       
        maxi = max(nums[l:r+1])       
        mini = min(nums[l:r+1])

        l2 = 0
        r2= len(nums)-1
        
        while(mini > nums[l2] or mini == nums[l2]):
            l2+=1           
        while(maxi < nums[r2] or maxi == nums[r2]):
            r2-=1
        
        return r2-l2+1
        