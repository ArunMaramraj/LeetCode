class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
                
        def partition(l,r):
            partition_index = l
            
            for i in range (l,r):
                if(nums[i]<nums[r]):
                    nums[i],nums[partition_index] = nums[partition_index],nums[i]
                    partition_index+=1
            nums[r],nums[partition_index] = nums[partition_index],nums[r]
            return partition_index
            
                    
       
        l = 0
        r = len(nums)-1
        

        while(l<=r):  
            pivot_index = partition(l,r)           
            if pivot_index > len(nums)-k:
                r = pivot_index-1
            elif pivot_index < len(nums)-k :
                l = pivot_index+1
            else:
                return nums[pivot_index]

                   
        
        
        
        
        