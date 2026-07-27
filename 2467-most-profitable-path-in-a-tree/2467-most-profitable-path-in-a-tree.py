# from collections import defaultdict , deque
# import heapq
# from functools import lru_cache

# class Solution:
#     def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
#         n = len(edges) + 1

#         graph = defaultdict(list)
#         out_degree = [0]*(n)

#         for u , v in edges :
#             graph[u].append(v)
#             graph[v].append(u)
#             out_degree[u] += 1
        
#         leaf = []
#         for node in range(n) :
#             if out_degree[node] == 0 and node != 0 :
#                 leaf.append(node)
        
#         bob_time = defaultdict(int)

#         # def bob_bfs(node , parent , time) :
#         queue = deque([(bob , -1 , 0)])

#         while queue :
#                 curr_node , curr_parent , curr_time = queue.popleft()
#                 if curr_node == 0 :
#                     bob_time[node] = time
#                     break
#                 bob_time[curr_node] = curr_time
#                 for neighbour in graph[curr_node] :
#                 if neighbour != curr_parent :
#                     queue.append((neighbour , curr_node , curr_time+1))
            
#         # bob_bfs(bob , -1 , 0)

#         maxi = float("-inf")


#         queue = deque([(0 , -1 , 0 , 0)])

#         while queue :

#             curr_node , curr_profit , curr_time , curr_profit = queue.popleft()
#             if curr_node not in bob_time or bob_time[curr_node] > curr_time :
#                 curr_profit += amount[curr_node]
#             elif curr_time == bob_time[curr_node] :
#                 curr_profit += amount[node]//2
#             else :
#                 curr_profit += 0
            
#             for neighbour in graph[curr_node] :
#                 if neighbour in leaf :
#                     maxi = max(maxi , curr_profit)
#                 if neighbour != parent :
#                     queue.append((neighbour , curr_node , curr_time+1 ,curr_profit))
        
#         return maxi

            
from collections import defaultdict, deque
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 1. Find the unique parent of each node relative to root (0) using BFS
        parent_map = {0: -1}
        queue = deque([0])
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor != parent_map[curr]:
                    parent_map[neighbor] = curr
                    queue.append(neighbor)

        # 2. Trace Bob's exact path back from `bob` to `0`
        bob_time = {}
        curr_node = bob
        time = 0
        while curr_node != -1:
            bob_time[curr_node] = time
            curr_node = parent_map[curr_node]
            time += 1

        # 3. BFS for Alice starting at node 0
        max_profit = float("-inf")
        # Store tuple: (curr_node, parent, curr_time, accumulated_profit)
        alice_queue = deque([(0, -1, 0, 0)])

        while alice_queue:
            curr_node, parent, curr_time, curr_profit = alice_queue.popleft()

            # Calculate profit at the current node based on Bob's arrival time
            if curr_node not in bob_time or curr_time < bob_time[curr_node]:
                curr_profit += amount[curr_node]
            elif curr_time == bob_time[curr_node]:
                curr_profit += amount[curr_node] // 2

            # Check if curr_node is a leaf (non-root node with degree 1)
            is_leaf = (curr_node != 0 and len(graph[curr_node]) == 1)
            if is_leaf:
                max_profit = max(max_profit, curr_profit)

            # Traverse neighbors
            for neighbor in graph[curr_node]:
                if neighbor != parent:
                    alice_queue.append((neighbor, curr_node, curr_time + 1, curr_profit))

        return max_profit








