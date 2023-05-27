class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        candidates.sort()
    
        temp,output = [] , []
        
        def compute(i):
            
            tempsum = sum(temp)
            
            if(tempsum==target): 
                output.append(temp[:])
                return
                
            if(tempsum > target):
                return
             
            if(i<=len(candidates)-1):
                temp.append(candidates[i])
                compute(i)
                temp.pop()
                compute(i+1)
    
        
        
        compute(0)
        
        return output
            
            
        