# from typing import List

# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         def dfs(node, visited, graph, curr, colour):
#             visited[node] = 1
#             colour[node] = curr
#             for neighbour in graph[node]:
#                 if not visited[neighbour]:
#                     if not dfs(neighbour, visited, graph, 1 - curr, colour):
#                         return False
#                 elif colour[neighbour] == curr:
#                     return False
#             return True

#         n = len(graph)
#         visited = [0] * n
#         colour = [-1] * n
#         for i in range(n):
#             if not visited[i]:
#                 if not dfs(i, visited, graph, 0, colour):
#                     return False
#         return True


from collections import deque
from typing import List


class Solution:

  def isBipartite(self, graph: List[List[int]]) -> bool:
    n = len(graph)
    # -1: uncolored, 0: color A, 1: color B
    color = [-1] * n

    # Loop through all nodes to handle disconnected components
    for i in range(n):
      if color[i] == -1:
        color[i] = 0
        queue = deque([i])

        while queue:
          node = queue.popleft()

          for neighbor in graph[node]:
            if color[neighbor] == -1:
              # Assign opposite color to neighbor
              color[neighbor] = 1 - color[node]
              queue.append(neighbor)
            elif color[neighbor] == color[node]:
              # Neighbor has the same color, conflict found
              return False

    return True