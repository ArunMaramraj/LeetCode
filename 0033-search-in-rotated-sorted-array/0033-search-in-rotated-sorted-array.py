class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def getpivot():
            s = 0
            e = len(nums)-1       
            while(s<e):
                mid = (e+s)//2
                if(nums[mid]>=nums[0]):
                    s= mid+1
                else:
                    e=mid
                    
            return s
        
        
        def binarysearch(l,r):
            while(l<=r):
                mid = (l+r)//2
                if (nums[mid]==target):
                    return mid
                elif (nums[mid]>target):
                    r = mid-1
                else:
                    l= mid+1
            return -1        
                    
        pivot = getpivot()
        
        if(target>=nums[pivot] and target<=nums[len(nums)-1]):
            return binarysearch(pivot,len(nums)-1)
        else:
            return binarysearch(0,pivot-1)