class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        
        l = 0
        r = n-1
        
        while(l<r):
            
            if M[l][r] == 1:
                l+=1
            
            else:
                r-=1
        
        
        for i in range(n) :
            if i!=l and (M[i][l]==0 or M[l][i]==1):
                return -1
                
        return l        