class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        V = len(graph)
        
        output = set()
        
        vis  = [False]*V
        pathvis = [False]*V
        
        
        def dfs(i):
            
            if(vis[i] and pathvis[i]):
                return False
            
            
            if (vis[i] and not pathvis[i]):
                if i in output:
                    return True
                else:
                    return False
                
                
            vis[i] = True
            pathvis[i] = True
            
            booli = True
            
            for j in graph[i]:
                booli = booli and dfs(j)
                if(booli == False):
                    break
                    
            pathvis[i] = False       
                    
            if booli: 
                output.add(i)
                
            return booli    
        
        
        
        for v in range(V):
            if (not vis[v]):
                dfs(v)
        
        return sorted(list(output))
        
        
        
        
                