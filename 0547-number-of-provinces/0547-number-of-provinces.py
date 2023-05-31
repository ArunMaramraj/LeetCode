class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
       
        vis = [False]*len(isConnected)
        count = 0
        
        def compute(i):          
            vis[i] = True
            for j in range (len(isConnected[i])):
                if(isConnected[i][j] == 1 and vis[j]==False):
                    compute(j)
    
        for i in range (len(isConnected)): 
            if(vis[i]==0):
                count+=1
                compute(i)
         
        return count
                