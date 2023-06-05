class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here


        vis = [False]*V
    
        # Write your code here
        st = []
        
        def dfs(i):
    
            vis[i] = True
            
            if len(adj[i])>0:
                for j in adj[i]:
                    if vis[j]:
                        continue
                    else:    
                        dfs[j]
            st.append(i)
    
    
    
        for i in range (v):
            if not vis[i]:
                dfs(i)
    
        return st.reverse()        