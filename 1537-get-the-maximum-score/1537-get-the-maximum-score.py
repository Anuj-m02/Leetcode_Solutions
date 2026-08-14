# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache


# class Solution:
#     def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

#         n , m = len(nums1) , len(nums2)

#         graph = defaultdict(list)

#         for i in range(n-1):
#             graph[nums1[i]].append(nums1[i+1])
        
#         for i in range(m-1) :
#             graph[nums2[i]].append(nums2[i+1])
        
#         # starting point can either be nums1[0] or nums2[0]
#         @lru_cache(maxsize=None)
#         def dfs(node) :
#             # if node in memo :
#             #     return memo[node]
            
#             max_future = 0
#             for neighbour in graph[node] :
#                 max_future = max(max_future , dfs(neighbour))
            
#             # memo[node] = node + max_future
#             return (node + max_future)%(10**9 + 7)
        
#         res = max(dfs(nums1[0]) , dfs(nums2[0]))

#         return res

#         # dist = defaultdict(lambda : float("-inf"))
#         # queue = deque([(start_node)])
#         # dist[start_node] = 0
#         # while queue :
#         #     curr_node = queue.popleft()

#         #     for neighbour in graph[curr_node] :
#         #         dist[neighbour] = dist[start_node] + neighbour
#         #         queue.append(neighbour)
        




#         # p1 , p2 , sum1 , sum2 , ans = 0 , 0 , 0 , 0 , 0

#         # while p1 < n and p2 < m :

#         #     if nums1[p1] == nums2[p2] :
#         #         ans += max(sum1 , sum2) + nums1[p1]
#         #         sum1 , sum2 = 0, 0
#         #         p1 , p2 = p1+1 , p2+1
            
#         #     elif nums1[p1] < nums2[p2] :
#         #         sum1 += nums1[p1]
#         #         p1 += 1
            
#         #     else :
#         #         sum2 += nums2[p2]
#         #         p2 += 1
        
#         # while (p1 < n) :
#         #     sum1 += nums1[p1]
#         #     p1 += 1
        
#         # while (p2 < m) :
#         #     sum2 += nums2[p2]
#         #     p2 += 1
        
#         # return (ans + max(sum1 , sum2)) % (10**9 + 7)


from collections import defaultdict
from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        graph = defaultdict(list)
        
        # 1. Build Directed Graph
        for i in range(len(nums1) - 1):
            graph[nums1[i]].append(nums1[i+1])
            
        for i in range(len(nums2) - 1):
            graph[nums2[i]].append(nums2[i+1])
            
        memo = {}

        # 2. DFS + Memoization to find the Longest Path from any node
        def dfs(node):
            if node in memo:
                return memo[node]
            
            max_future = 0
            for neighbor in graph[node]:
                max_future = max(max_future, dfs(neighbor))
                
            memo[node] = node + max_future
            return memo[node]

        # 3. Maximum score starting from either nums1[0] or nums2[0]
        result = max(dfs(nums1[0]), dfs(nums2[0]))
        
        return result % (10**9 + 7)
