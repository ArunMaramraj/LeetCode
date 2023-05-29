class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
        if digits == "":
            return []
        
        n = len(digits)
       
        output  = []
        
        def compute(i,res):
            
            if i>=len(digits) :
                output.append(res)
                return
            
            for letter in dic[digits[i]]:
                temp = res
                res = res + letter
                compute(i+1,res)
                res = temp
                
                
               
        compute(0,"")        
        return output        
                
            