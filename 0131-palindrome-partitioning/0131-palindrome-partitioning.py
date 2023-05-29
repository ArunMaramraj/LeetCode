class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        output = []
        
        
        def isPalindrome(s,l,r):
            
            while(l<r):
                if(s[l]!=s[r]): return False
                l+=1
                r-=1
            return True    
        
        
        def compute(i):
            if(i>=len(s)):
                output.append(res[:])
                return
            
            for j in range(i,len(s)):
                if(isPalindrome(s,i,j)):
                    res.append(s[i:j+1])
                    compute(j+1)
                    res.pop()
        
        
        
        compute(0)
        return output
        
        
        
        