class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        
        ones = [ i for i in range(len(nums)) if nums[i]==1]
        mod = 10**9 + 7
        n = len(ones)
        output = [1]*n
        if n == 0:
            return 0
        
        for i in range(0,n-1):
            output[i] = ones[i+1] - ones[i]
        
        
        ret = 1
        
        for i in output:
            ret*=i
        
        return ret%(mod)
            
        
                
                