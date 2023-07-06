class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        
        n,m = len(str1),len(str2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if j==0:
                    dp[i][j] = 0
                elif i==0:
                    dp[i][j] =0 
                else:
                    if str2[i-1] == str1[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
      #n,j=>str1
    #m,i=>str2
    
        i,j = m,n
        temp = ""
        while(i>0 and j>0):
            if str1[j-1] == str2[i-1]:
                temp+=str1[j-1]
                i-=1
                j-=1
            
            elif dp[i-1][j] >= dp[i][j-1]:
                temp+=str2[i-1]
                i-=1
                
            else:
                temp+=str1[j-1]
                j-=1
                
        while(i>0):
            temp+=str2[i-1]
            i-=1
        
        while(j>0):
            temp+=str1[j-1]
            j-=1
                
                
        return temp[::-1]
    