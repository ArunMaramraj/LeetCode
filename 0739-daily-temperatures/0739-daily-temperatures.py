class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        output = [None]*len(temperatures)
        
        if len(temperatures)==1: return [0]
        
        pointer = len(temperatures)-2
        
        stack = [pointer+1]
        output[pointer+1]=0

        while(pointer>=0):
            
            while(stack and temperatures[pointer]>=temperatures[stack[-1]]):
                stack.pop()

            if (len(stack)==0):
                output[pointer]=0
                stack.append(pointer)

            else : 
                output[pointer]=stack[-1]-pointer
                stack.append(pointer)

            pointer-=1    
            
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        