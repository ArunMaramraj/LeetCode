from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        adj = defaultdict(list)

        for edge in edges:
            u, v = edge
            adj[v].append(u)
            adj[u].append(v)

        output1 = set()
        output2 = []

        def dfs(i, parent, visited):
            visited.add(i)

            for j in adj[i]:
                if j == parent:
                    continue
                if j in visited:
                    output1.add((i, j))
                else:
                    dfs(j, i, visited)

        for key in adj.keys():
            visited = set()
            dfs(key, -1, visited)

        for sets in output1:
            output2.append(list(sets))

        intersection = [x for x in edges if x in output2]

        return intersection[-1] if intersection else []
