class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        m = len(nums1)
        n = len(nums2)
        
        dic = {}
        
        def compute(i1,i2):
            if i1>=m or i2>=n:
                return 0
            
            if (i1,i2) in dic:
                return dic[(i1,i2)]
            
            if nums1[i1] == nums2[i2]:
                return 1 + compute(i1+1, i2+1)
            
            dic[(i1,i2)] = max(compute(i1+1,i2) , compute(i1,i2+1))
            
            return dic[(i1,i2)]
        
        return compute(0,0)