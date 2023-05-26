class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
         
        output = []
        temp = nums
        
        def compute(i):   
            if (i>= len(nums)):
                output.append(temp[:])
                return
            for j in range (i , len(nums)):
                temp[i] , temp[j] = temp[j] , temp[i]
                compute(i+1)
                temp[i] , temp[j] = temp[j] , temp[i]
        
        compute(0)
        return output        
                