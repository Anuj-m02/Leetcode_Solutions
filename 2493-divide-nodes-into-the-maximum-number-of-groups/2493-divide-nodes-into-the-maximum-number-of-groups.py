from collections import deque, defaultdict

class DSU:
    def __init__(self, n: int):
        # 0-indexed parent array
        self.parent = list(range(n))
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry


class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        # 1. Build adjacency list (converted to 0-indexed)
        g = [[] for _ in range(n)]
        dsu = DSU(n)
        
        for a, b in edges:
            u, v = a - 1, b - 1
            g[u].append(v)
            g[v].append(u)
            dsu.union(u, v)

        # 2. Run BFS from every node to check bipartiteness & track maximum depth per component
        max_depth_per_component = defaultdict(int)

        for start_node in range(n):
            queue = deque([start_node])
            dist = [0] * n
            dist[start_node] = 1
            max_depth = 1

            while queue:
                curr = queue.popleft()
                for neighbor in g[curr]:
                    if dist[neighbor] == 0:
                        dist[neighbor] = dist[curr] + 1
                        max_depth = max(max_depth, dist[neighbor])
                        queue.append(neighbor)
                    elif abs(dist[neighbor] - dist[curr]) != 1:
                        # Adjacent nodes in the same layer -> Odd-length cycle found
                        return -1

            # Store the largest BFS depth for this component root
            root = dsu.find(start_node)
            max_depth_per_component[root] = max(max_depth_per_component[root], max_depth)

        # 3. Sum maximum groups across all components
        return sum(max_depth_per_component.values())

from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Check Bipartiteness (Odd-length cycle detection)
        color = [0] * (n + 1)
        components = []
        
        for i in range(1, n + 1):
            if color[i] != 0:
                continue
            
            component = []
            queue = deque([i])
            color[i] = 1
            
            while queue:
                curr = queue.popleft()
                component.append(curr)
                for neighbor in adj[curr]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[curr]
                        queue.append(neighbor)
                    elif color[neighbor] == color[curr]:
                        return -1  # Odd cycle found

            components.append(component)

        # 2. Find max BFS depth for each node
        def getMaxGroupsFrom(start_node: int) -> int:
            visited = [-1] * (n + 1)
            visited[start_node] = 1
            queue = deque([start_node])
            max_depth = 1
            
            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = visited[curr] + 1
                        max_depth = max(max_depth, visited[neighbor])
                        queue.append(neighbor)
            return max_depth

        # 3. Sum maximum groups across all components
        total_groups = 0
        for comp in components:
            max_component_groups = max(getMaxGroupsFrom(node) for node in comp)
            total_groups += max_component_groups

        return total_groups