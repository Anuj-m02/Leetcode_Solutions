# from collections import defaultdict, deque

# class Solution:
#     def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:

#         graph = defaultdict(list)
#         children = defaultdict(list)

#         # for par, ch in edges:
#         #     children[par].append(ch)
#         #     graph[par].append(ch)
#         #     graph[ch].append(par)

#         parent = [-1] * n

#         for par, ch in edges:
#             parent[ch] = par
#             children[par].append(ch)
#             graph[par].append(ch)
#             graph[ch].append(par)

#         queue = deque()

#         for node in range(n):
#             if not children[node]:
#                 queue.append(
#                     (node, graph[node], baseTime[node], baseTime[node], baseTime[node])
#                 )

#         early = []
#         late = []

#         while queue:
#             curr_node, curr_par, earliest, latest, time = queue.popleft()

#             if curr_node == 0:
#                 early.append(earliest)
#                 late.append(latest)
#                 continue

#             next_node = parent[curr_node]

#             new_time = (latest - earliest) + baseTime[next_node] + latest

#             queue.append(
#                 (next_node, graph[next_node], new_time, new_time, new_time)
#             )

#         ownDuration = max(late) - min(early) + baseTime[0]

#         return max(late) + ownDuration - baseTime[0]


from collections import deque
from typing import List

class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        
        # Keep track of parents to move upwards
        parent = [-1] * n
        # Keep track of how many children a node is waiting for
        children_count = [0] * n
        
        for u, v in edges:
            parent[v] = u
            children_count[u] += 1
            
        # Store the finish times of the children for each node
        children_finish_times = [[] for _ in range(n)]
        
        # Step 1: "Take down all leaf nodes first"
        queue = deque()
        for i in range(n):
            if children_count[i] == 0:
                queue.append(i)
                
        # Step 2: "Traversal from leaf to 0th node"
        while queue:
            u = queue.popleft()
            
            # Calculate the finish time for the current node
            if not children_finish_times[u]:
                # It's a leaf node
                finish_time = baseTime[u]
            else:
                # Non-leaf node: process the collected finish times of its children
                earliest = min(children_finish_times[u])
                latest = max(children_finish_times[u])
                ownDuration = (latest - earliest) + baseTime[u]
                finish_time = latest + ownDuration
                
            # If we've calculated the root, we're done
            if u == 0:
                return finish_time
                
            # Pass the finish time up to the parent
            p = parent[u]
            if p != -1:
                children_finish_times[p].append(finish_time)
                children_count[p] -= 1
                
                # Once all children of the parent are processed, add parent to the queue
                if children_count[p] == 0:
                    queue.append(p)
                    
        return -1