class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dic = {}
        n = len(questions)
        for i in range(n-1,-1,-1):
            dic[i] = max(questions[i][0]+dic.get(questions[i][1]+i+1,0) , dic.get((i+1),0))
        return dic[0]        
            
            
            