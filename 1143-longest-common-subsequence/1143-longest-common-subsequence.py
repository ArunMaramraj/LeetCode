class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dic = {}
        
        def compute(index1,index2):
            
            if index1<0 or index2<0:
                return 0
            
            if (index1,index2) in dic:
                return dic[(index1,index2)]
            
            if text1[index1] == text2[index2]:
                return 1 + compute(index1-1,index2-1)
            
            dic[(index1,index2)] = max(compute(index1-1,index2) , compute(index1,index2-1))
            
            return dic[(index1,index2)]
        
        
        return compute(len(text1)-1 , len(text2)-1)
                     