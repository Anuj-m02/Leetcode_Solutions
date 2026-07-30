# from collections import defaultdict , deque
# import heapq
# from functools import lru_cache

# class Solution:
#     def countVisitedNodes(self, edges: List[int]) -> List[int]:
#         n = len(edges)
#         graph = defaultdict()
#         indegree = [0]*(n)

#         for node in range(n):
#             graph[node].append(edges[node])
#             indegree[edges[node]] += 1
#         # print(graph)
#         # print(indegree)
#         queue = deque([])
#         for node in range(n) :
#             if indegree[node] == 0 :
#                 queue.append(node)
        
#         ans = [0]*(n)
#         temp = []
#         while queue :
#             # print(queue)
#             curr_node = queue.popleft()
#             temp.append(curr_node)
#             for neighbour in graph[curr_node] :
#                 indegree[neighbour] -= 1
#                 if indegree[neighbour] == 0 :
#                     queue.append(neighbour)
        
#         print(temp)

#         for node in range(n):
#             if indegree[node] > 0 :
#                 curr_node = node
#                 cycle_len = 0 
#                 while True :
#                     curr_node = graph[curr_node]
#                     cycle_len += 1
#                     if curr_node == node :
#                         break
                
#                 curr_node = node
#                 while True :
#                     ans[curr_node] += cycle_len
#                     indegree[curr_node] = 0
#                     curr_node = graph[curr_node]
#                     if curr_node == node :
#                         break
        
#         while temp :
#             node = stack.pop()
#             ans[node] = ans[graph[node]]+1
        
#         return ans


#         # no of node not in cycle is len of temp
#         # in_cycle = n - len(temp)
#         # for node in range(n):
#         #     if node not in temp :
#         #         ans[node] += in_cycle
#         #     else :
#         #         ans[node] += (in_cycle+1) 
        
#         return ans


from collections import defaultdict, deque
import heapq
from functools import lru_cache
from typing import List

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        indegree = [0]*(n)

        # 1. Use the 'edges' array directly instead of building a new 'graph' dict
        for node in range(n):
            indegree[edges[node]] += 1

        queue = deque([])
        for node in range(n) :
            if indegree[node] == 0 :
                queue.append(node)
        
        ans = [0]*(n)
        temp = []
        while queue :
            curr_node = queue.popleft()
            temp.append(curr_node)
            
            # 2. Replaced the for loop since there's only 1 outgoing edge per node
            neighbour = edges[curr_node] 
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0 :
                queue.append(neighbour)

        for node in range(n):
            if indegree[node] > 0 :
                curr_node = node
                cycle_len = 0 
                while True :
                    curr_node = edges[curr_node] # Replaced graph with edges
                    cycle_len += 1
                    if curr_node == node :
                        break
                
                curr_node = node
                while True :
                    ans[curr_node] += cycle_len
                    indegree[curr_node] = 0
                    curr_node = edges[curr_node] # Replaced graph with edges
                    if curr_node == node :
                        break
        
        while temp :
            node = temp.pop() # 3. Changed 'stack' to 'temp'
            ans[node] = ans[edges[node]]+1 # Replaced graph with edges
        
        return ans
