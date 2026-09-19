# from collections import defaultdict , deque , Counter


# # class DSU :
# #     def __init__(self , n) :
# #         self.n = n
# #         self.parent = list(range(n))
# #         self.size = [1]*(n)
    
# #     def find(self , node) :
# #         if self.parent[node] != node :
# #             self.parent[node] = self.find(self.parent[node])
        
# #         return self.parent[node]
    
# #     def union(self , x , y) :
# #         xr , yr = self.find(x) , self.find(y)

# #         if xr == yr :
# #             return False
        
# #         self.parent[xr] = yr
# #         self.size[yr] += self.size[xr]
# #         return True


# class Solution:
#     def magnificentSets(self, n: int, edges: list[list[int]]) -> int:

#         graph = defaultdict(list)
#         for u,v in edges :
#             graph[u].append(v)
#             graph[v].append(u)
        
#         colour = [0]*(n+1)
#         component = []

#         for i in range(1,n+1) :
#             if colour[i] != 0 :
#                 continue
            
#             comp = []
#             queue = deque([i])
#             colour[i] = 1

#             while queue :
#                 curr = queue.popleft()
#                 comp.append(curr)
#                 for neighbour in graph[curr] :
#                     if colour[neighbour] == 0 :
#                         colour[neighbour] = -colour[curr]
#                         queue.append(neighbour)
#                     elif colour[neighbour] == colour[curr] :
#                         return -1 # odd cycle found
            
#             component.append(comp)
        
    
#         def max_groups(start_node) :
#             visited = [-1]*(n+1)
#             visited[start_node] = 1
#             queue = deque([start_node])
#             max_depth = 1

#             while queue :
#                 curr = queue.popleft()
#                 for neighbour in graph[curr] :
#                     if visited[neighbour] == -1 :
#                         visited[neighbour] = visited[curr_node] + 1
#                         max_depth = max(max_depth , visited[neighbour])
#                         queue.append(neighbour)
            
#             return max_depth
        
#         total_grps = 0
#         for comp in component :
#             max_comp_grps = max(max_grps(node) for node in comp)
#             total_grps += max_comp_grps
        
#         return total_grps


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