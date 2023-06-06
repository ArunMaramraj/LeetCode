class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            
        
            
            
            queue = []
            indegree = [0] * numCourses
            topo = []
            V = len(prerequisites)
            
            adj = [[] for _ in range(numCourses)]

            
            for i in prerequisites:
                adj[i[0]].append(i[1])
            

            for i in range(numCourses):     
                for j in adj[i]:
                    indegree[j]+=1

            for i in range (len(indegree)):     
                if indegree[i]==0 :                
                    queue.append(i) 


            while(len(queue)!=0):
                ele = queue.pop(0)
                topo.append(ele)

                for j in adj[ele]:
                    indegree[j]-=1
                    if(indegree[j]==0):
                        queue.append(j)
            
            
            
            if len(topo)<numCourses : return False
            else: return True
        
        
        
        