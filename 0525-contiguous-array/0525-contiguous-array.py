class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        dic = {0:-1}
        
        s = 0
        
        output = 0
        
        for index,num in enumerate(nums):
            if num :
                s+=1
            else:
                s-=1
                    
            if s in dic:
                output = max(output,index-dic[s])
            
            else:
                dic[s] = index 
            
            
        return output    
            