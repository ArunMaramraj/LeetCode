class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        index1 = len(s)-1
        index2 = len(t)-1
        
        dic = {}
        
        def compute(index1,index2):
            if index1<0 and index2>=0:
                return 0
            
            if index1<0 and index2<0:
                return 1
            
            if index2<0 and index1>=0:
                return 1
            
            if (index1,index2) in dic:
                return dic[(index1,index2)]
            
            if s[index1] == t[index2]:
                dic[(index1,index2)] = (compute(index1-1,index2-1) + compute(index1-1,index2))
            
            else:
                dic[(index1,index2)] = compute(index1-1,index2)
                
            
            return dic[(index1,index2)]
        
        return compute(index1,index2)    
            