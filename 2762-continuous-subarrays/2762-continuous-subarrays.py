class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
     
    
        dic = {}
        
        def search(j, x, y):
            if j >= n:
                return 0
            if (j,x,y) in dic:
                return dic[(j,x,y)]
            
            xx = min(x, nums[j])
            yy = max(y, nums[j])
            
            if abs(xx - yy) <= 2:
                temp = 1 + search(j+1,xx,yy)
                dic[(j,x,y)] = temp
                return temp
            
            return 0
        
        ans = 0
        for i in range(n):
            ans += search(i, nums[i], nums[i])
        return ans
        