class Solution:
    def minDeletions(self, s: str) -> int:
        
        dic = {}
        
        for i in s:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        
        s = set()
        res =0
        
        for key,val in dic.items():
            while val>0 and val in s:
                val-=1
                res+=1
            s.add(val)    
            
        return res    