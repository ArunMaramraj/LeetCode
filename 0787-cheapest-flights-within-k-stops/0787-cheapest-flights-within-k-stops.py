from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, price in flights:
            graph[a].append((b, price))
        
        node2minNstop = {i: float("inf") for i in range(n)}
        pq = [(0, src, -1)]
        while pq:
            dist_from_src, node, n_stops = heappop(pq)
            if node == dst:
                return dist_from_src
			# skip current iteration if number of stops exceeds maximum
			# or we can reach current node with fewer stops. Suppose we've
			# visited this node before, by the property of Dijkstra we must have found
			# a path with lower cost to this node before. The only reason we might want
			# to visit it again is if we can visit it with fewer stops. If this is not the case, we
			# skip.
            if n_stops >= min(k, node2minNstop[node]):
                continue
            node2minNstop[node] = n_stops
            for neighbor, dist_to_neighbor in graph[node]:
                heappush(pq, (dist_from_src+dist_to_neighbor, neighbor, n_stops+1))
                    
        return -1