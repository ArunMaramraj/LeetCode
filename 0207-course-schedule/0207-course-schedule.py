class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = []
        indegree = [0] * numCourses
        topo = []
        
        adj = [[] for _ in range(numCourses)]
        
        for i in prerequisites:
            adj[i[0]].append(i[1])
            indegree[i[1]] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.pop(0)
            topo.append(course)
            
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(topo) == numCourses
