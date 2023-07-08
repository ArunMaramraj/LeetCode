# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
        
        
              #recursive:
        
#         i1,i2 = len(word1)-1 , len(word2)-1
#         def compute(i1,i2):
#             if i1<0 and i2<0:
#                 return 0
#             elif i1<0 and i2>=0:
#                 return i2+1
            
#             elif i1>=0 and i2<0:
#                 return i1+1
            
#             if word1[i1] == word2[i2]:
#                 return 0 + compute(i1-1,i2-1)
            
#             else:
#                 replace = 1 + compute(i1-1,i2-1)
#                 insert  = 1 + compute(i1,i2-1)
#                 delete = 1 + compute(i1-1,i2)
                
#                 return min(insert,replace,delete)
            
#         return compute(i1,i2)
    
    
    
    
#                  memo:



#                 i1,i2 = len(word1)-1 , len(word2)-1
            
            
#         def compute(i1,i2):
#             memo = {}
#             if i1<0 and i2<0:
#                 return 0
#             elif i1<0 and i2>=0:
#                 return i2+1
            
#             elif i1>=0 and i2<0:
#                 return i1+1
            
#             if (i1,i2) in memo:
#                 return memo[(i1,i2)]
            
#             if word1[i1] == word2[i2]:
#                 return 0 + compute(i1-1,i2-1)
            
#             else:
#                 replace = 1 + compute(i1-1,i2-1)
#                 insert  = 1 + compute(i1,i2-1)
#                 delete = 1 + compute(i1-1,i2)
                
#                 dic[(i1,i2)] = min(insert,replace,delete)
#                 return dic[(i1,i2)]
            
#         return compute(i1,i2)



#                   tabulation:
        
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m,n = len(word1),len(word2)
        
        dp = [[0]*(n+1) for _ in range(m+1) ]
        
        for i in range(m+1):
            for j in range(n+1):
                if j==0:
                    dp[i][j] = i
                    continue
                if i==0:
                    dp[i][j] = j
                    continue
                
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                    
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    
        return dp[-1][-1]