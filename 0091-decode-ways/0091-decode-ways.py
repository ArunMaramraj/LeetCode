class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        #1 - 26
        
        n = len(s)
        
        dic = {}
        
        def compute(index):
            if index>=n:
                return 1
            
            if index in dic:
                return dic[index]
                
            take_one_at_once, take_two_at_once = 0,0
            
            if s[index] == '0':
                return 0
       
            take_one_at_once = compute(index+1)
                
            if index!=n-1 and (1<=int(s[index:index+2])<=26):
                take_two_at_once = compute(index+2)
                
            dic[index] =  take_one_at_once + take_two_at_once
            return dic[index]
        
        
        return compute(0)
            
        
        
        