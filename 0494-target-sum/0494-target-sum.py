class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dic = {}
        
        def compute(i,t):
            
            if i>=len(nums):
                return 1 if t==target else 0
            
            if (i,t) in dic:
                return dic[(i,t)]
            
            
            plus  = compute(i+1 , t+nums[i])
            minus = compute(i+1 , t-nums[i])
            
            dic[(i,t)] = plus+minus
            
            return dic[(i,t)]
        
        return compute(0,0)
            