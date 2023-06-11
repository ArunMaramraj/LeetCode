from heapq import heappop, heappush
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # Build the graph
        graph = [[] for _ in range(n)]
        dis = [float('inf')] * n
        
        for flight in flights:
            u, v, w = flight
            graph[u].append((v, w))
        
        pq = deque()
        pq.append((0, src, 0))  # dis, source, no of stops
        
        dis[src] = 0
        
        while pq:
            d, u, st = pq.popleft()
            
            for v, w in graph[u]:
                if d + w < dis[v] and st <= k:
                    dis[v] = d + w
                    pq.append((dis[v], v, st + 1))
        
        if dis[dst] == float('inf'):
            return -1
        
        return dis[dst]