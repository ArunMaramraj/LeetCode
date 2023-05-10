class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        
        
        output=[]
        target = n
        
        def compute(stack, openN , closeN , string):
            
            if openN == closeN == target:
                output.append(string)
                return
                
            if openN < target :
                stack.append('(')
                compute(stack,openN+1,closeN,string+'(')
                stack.pop()
                
            if closeN < target : 
                    if (stack and stack[-1]=='('):
                        stack.pop()
                        compute(stack,openN,closeN+1,string+')')
                        stack.append('(')
                
        compute([],0,0,"")
        
        return output
        
        
        
        
        
        
        