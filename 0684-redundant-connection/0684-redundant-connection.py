class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # variables
        n = len(edges)
        parents = [i for i in range(n + 1)]

        def find_group_root(node):
            group_root = node
            while group_root != parents[group_root]:
                group_root = parents[group_root]
            return group_root
        
        for v1, v2 in edges:
            group_root1 = find_group_root(v1)
            group_root2 = find_group_root(v2)
            if group_root1 == group_root2:
                return [v1, v2]
            # union two groups
            parents[group_root2] = group_root1