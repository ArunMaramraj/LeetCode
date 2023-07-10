class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        
        l = 0
        r = len(nums)-1
        n = r
        output = None
        
        while(l<r):
            
            mid = (l+r)//2
            index = mid
            
            if mid-1>=0 and nums[mid-1] == nums[mid]:
                index = mid-1
            
            elif mid+1<=n and nums[mid+1] == nums[mid]:
                index = mid+1
                
            
            if index == mid:
                return nums[index]
            
            if index<mid:
                if (index-l)%2==0:
                    l = mid+1
                else:
                    r = index-1
                    
            else:
                if (r-index)%2 == 0 :
                    r = mid-1
                else:
                    l = index+1
            
        return nums[l]        
            