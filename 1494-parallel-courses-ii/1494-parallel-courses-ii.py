# # # from collections import defaultdict , deque , Counter
# # # import heapq
# # # from functools import lru_cache

# # # class Solution:
# # #     def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:

# # #         graph = defaultdict(list)
# # #         indegree = [0]*(n+1)

# # #         if not relations :
# # #             return math.ceil(n/k)

# # #         for u , v in relations :
# # #             graph[u].append(v)
# # #             indegree[v] += 1
        
# # #         queue = deque([])
# # #         cnt = 1

# # #         sem_dict = defaultdict(list)

# # #         for node in range(n) :
# # #             if indegree[node] == 0 :
# # #                 curr_sem = math.ceil(cnt//k)
# # #                 queue.append((node , curr_sem))
# # #                 sem_dict[curr_sem].append(node)
# # #                 cnt += 1
        
# # #         ans = 0

# # #         while queue :
# # #             length = len(queue)
# # #             curr_node , curr_sem = queue.popleft()
# # #             ans = max(ans , curr_sem)

# # #             for neighbour in graph[curr_node] :
# # #                 indegree[neighbour] -= 1
# # #                 if indegree[neighbour] == 0 :
# # #                     new_sem = curr_sem + 1
# # #                     while len(sem_dict[new_sem]) > k :
# # #                         # sem_dict[new_sem].append(neighbour)
# # #                         # queue.append((neighbour , new_sem))
# # #                         new_sem += 1
# # #                     sem_dict[new_sem].append(neighbour)
# # #                     queue.append((neighbour , new_sem))

# # #         return ans                        

        
# # #         # print(queue)
# # #         # while queue :
# # #         #     length = len(queue)
# # #         #     for curr_node , curr_sem in queue :
# # #         #         curr_node , curr_sem = queue.popleft()
# # #         #         ans = max(ans , curr_sem)
                
# # #         #         for neighbour in graph[curr_node] :
# # #         #             indegree[neighbour] -= 1
# # #         #             if indegree[neighbour] == 0 :
# # #         #                 queue.append((neighbour , curr_sem + 1))
        
# # #         # return ans
            

# # import math
# # from collections import defaultdict, deque
# # from typing import List

# # class Solution:
# #     def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
# #         graph = defaultdict(list)
# #         indegree = [0] * (n + 1)

# #         for u, v in relations:
# #             graph[u].append(v)
# #             indegree[v] += 1
        
# #         queue = deque([])
# #         sem_dict = defaultdict(list)
# #         cnt = 1

# #         # 1. Fixed indexing: iterate from 1 to n inclusive
# #         for node in range(1, n + 1):
# #             if indegree[node] == 0:
# #                 # 2. Fixed semester calculation using math.ceil(cnt / k)
# #                 curr_sem = math.ceil(cnt / k)
# #                 queue.append((node, curr_sem))
# #                 sem_dict[curr_sem].append(node)
# #                 cnt += 1
        
# #         ans = 0

# #         while queue:
# #             curr_node, curr_sem = queue.popleft()
# #             ans = max(ans, curr_sem)

# #             for neighbour in graph[curr_node]:
# #                 indegree[neighbour] -= 1
# #                 if indegree[neighbour] == 0:
# #                     new_sem = curr_sem + 1
# #                     # 3. Fixed logic: increment new_sem ONLY IF the semester is ALREADY full (== k)
# #                     while len(sem_dict[new_sem]) >= k:
# #                         new_sem += 1
                    
# #                     sem_dict[new_sem].append(neighbour)
# #                     queue.append((neighbour, new_sem))

# #         return ans


# from functools import lru_cache
# from collections import defaultdict
# from typing import List

# class Solution:
#     def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        
#         # Build prerequisites map
#         prereqs = defaultdict(set)
#         for u, v in relations:
#             prereqs[v].add(u)
            
#         @lru_cache(None)
#         def solve(taken: frozenset) -> int:
#             if len(taken) == n:
#                 return 0
            
#             # Find all available nodes whose prerequisites are fully met
#             available = [
#                 node for node in range(1, n + 1)
#                 if node not in taken and prereqs[node].issubset(taken)
#             ]
            
#             # If available courses fit in one semester, take all of them
#             if len(available) <= k:
#                 return 1 + solve(taken | frozenset(available))
            
#             # Otherwise, branch: try every combination of k courses
#             import itertools
#             min_sems = float('inf')
            
#             for choice in itertools.combinations(available, k):
#                 min_sems = min(min_sems, 1 + solve(taken | frozenset(choice)))
                
#             return min_sems

#         return solve(frozenset())

import math
from collections import defaultdict
from functools import lru_cache
from typing import List
import itertools

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:

        graph = defaultdict(list)
        indegree = [0] * (n + 1)

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        @lru_cache(None)
        def solve(taken: frozenset) -> int:
            if len(taken) == n:
                return 0

            # Find all nodes with current indegree == 0 (prereqs in 'taken')
            available = []
            for node in range(1, n + 1):
                if node not in taken:
                    # Check if all dependencies are already taken
                    if all(parent in taken for parent in range(1, n + 1) if node in graph[parent]):
                        available.append(node)

            # Option 1: If available courses <= k, take all in current sem
            if len(available) <= k:
                return 1 + solve(taken | frozenset(available))

            # Option 2: Choose which k courses to add or defer to a later sem
            min_sem = float('inf')
            for choice in itertools.combinations(available, k):
                min_sem = min(min_sem, 1 + solve(taken | frozenset(choice)))

            return min_sem

        return solve(frozenset())