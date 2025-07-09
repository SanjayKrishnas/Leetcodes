class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]  # Initialize each node as its own parent
        size = [1] * (n + 1)  # Initially each set has size 1
        
        def find(x):
            """Find root with path compression"""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Union by size - attach smaller tree to larger tree"""
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False  # Already in same set, would create a cycle
            
            # Union by size - attach smaller tree to larger tree
            if size[root_x] < size[root_y]:
                parent[root_x] = root_y
                size[root_y] += size[root_x]  # Update the size of root_y
            else:
                parent[root_y] = root_x
                size[root_x] += size[root_y]  # Update the size of root_x
                
            return True  # Union successful
        
        # Process each edge
        for u, v in edges:
            if not union(u, v):
                return [u, v]  # This edge creates a cycle, so it's redundant
                
