from collections import defaultdict, deque
import math


class Solution:

  def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
    if not roads:
      return 0

    n = len(roads) + 1
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in roads:
      graph[u].append(v)
      graph[v].append(u)
      indegree[u] += 1
      indegree[v] += 1

    # Only add non-capital leaf nodes (nodes != 0 with indegree == 1)
    queue = deque([node for node in range(n) if indegree[node] == 1 and node != 0])

    rep = [1] * n
    total_fuel = 0

    while queue:
      curr_node = queue.popleft()

      total_fuel += math.ceil(rep[curr_node] / seats)

      for neighbour in graph[curr_node]:
        if indegree[neighbour] > 0:  # Only process active edges
        #   indegree[curr_node] -= 1
          indegree[neighbour] -= 1

          rep[neighbour] += rep[curr_node]

          # Queue neighbor when all its children are processed and it's not node 0
          if indegree[neighbour] == 1 and neighbour != 0:
            queue.append(neighbour)

    return total_fuel
# from collections import defaultdict , deque , Counter


# class Solution:
#     def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        
#         if not roads :
#             return 0
        
#         n = len(roads) + 1
#         graph = defaultdict(list)
#         indegree = [0]*(n)
#         for u,v in roads :
#             graph[u].append(v)
#             graph[v].append(u)
#             indegree[u] += 1
#             indegree[v] += 1
        
#         # get all nodes having indegree 1 
#         # start from those nodes with (curr_node , seat_cap) if sseat cap less than seats include another one

#         queue = deque([])
#         for nodes in range(n) :
#             if indegree[nodes] == 1 :
#                 queue.append((nodes))
        
#         rep = [1]*(n)
#         total_fuel = 0

#         while queue :
#             curr_node = queue.popleft()

#             total_fuel += math.ceil(rep[curr_node]/seats)

#             for neighbour in graph[curr_node] :
#                 indegree[neighbour] -= 1

#                 rep[neighbour] += rep[curr_node]
#                 if indegree[neighbour] == 1 and neighbour != 0 :
#                     queue.append(neighbour)

#         return total_fuel  
#         # cnt = 0
#         # while queue :
#         #     curr_node , curr_seat = queue.popleft()
#         #     cnt += 1
#         #     if curr_node == 0 :
#         #         continue
#         #     for neighbour in graph[curr_node] :
#         #         if curr_seat < seats :
#         #             queue.append((neighbour , curr_seat+1))
#         #         else :
#         #             queue.append((neighbour , seats))
#         #             queue.append((neighbour , 1))
        
#         # return cnt


