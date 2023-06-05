class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):

      queue = []
      indegree = []
      topo = []

      for i in range(V):
            for j in adj[i]:
                  indegree[j]+=1

      for i in range (len(indegree)):
            if indegree[i]==0 :
                  queue.append(i) 
                        
           
      while(len(queue)!=0):
           ele = queue.pop(0)
           topo.append(ele)

           for j in adj(ele):
                indegree[j]-=1
                if(indegree[j]==0):
                     queue.append(j)


