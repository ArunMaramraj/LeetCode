class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        s= 0
        f= 0
        s2=0
        while(True):
            s = nums[s]
            f = nums[nums[f]]
            if(s==f):
                break
        while(True):
            s= nums[s]
            s2 = nums[s2]
            if(s==s2):
                break
        return s    
 
            
        