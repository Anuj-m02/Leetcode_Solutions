# # from collections import defaultdict , deque , Counter
# # import heapq
# # from functools import lru_cache
# # from itertools import combinations

# # class DSU :
    
# #     def __init__(self , n) :
# #         self.parent = list(range(n))
# #         self.size = [1]*(n)
    
# #     def find(self , node) :
# #         if self.parent[node] != node :
# #             self.parent[node] = self.find(self.parent[node])
        
# #         return self.parent[node]
    
# #     def union(self , x , y) :

# #         root_x , root_y = self.find(x) , self.find(y)

# #         if root_x == root_y :
# #             return False
        
# #         self.parent[root_x] = root_y
# #         self.size[root_y] += self.size[root_x]
# #         return True

# # class Solution:
# #     def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:

# #         n = len(nums)
# #         graph = defaultdict(list)
    
# #         def backtrack(index, current_subset):
# #             # Base case: if we have made a decision for all elements
# #             if index == len(my_list):
# #                 result.append(list(current_subset)) # Append a copy
# #                 return
            
# #             # Choice 1: Include the element at the current index
# #             current_subset.append(my_list[index])
# #             backtrack(index + 1, current_subset)
            
# #             # Choice 2: Exclude the element (backtrack)
# #             current_subset.pop()
# #             backtrack(index + 1, current_subset)

# #         # backtrack(0, [])
# #         # return result
# #         dsu = DSU(n)
# #         for u , v in edges :
# #             graph[u].append(v)
# #             graph[v].append(u)
# #             dsu.union(u,v)
        
# #         nodes = list(range(n))
# #         subsets = []
# #         ans = 0
# #         for r in range(n + 1) :
# #             # subsets.append(combinations(nodes , r))
# #             for subset in combinations(nodes , r) :
        
# #         # ans = 0
# #         # for subset in subsets :
# #                 prev_root = -1
# #                 total = 0
# #                 chk = True
# #                 for indx in range(len(subset)) :
# #                     curr_node = subset[indx]
# #                     total += nums[curr_node]
# #                     curr_root = dsu.find(curr_node)
# #                     if prev_root == -1 :
# #                         prev_root = curr_root
# #                     if prev_root != curr_root :
# #                         chk = False
# #                         break
                
# #                 if chk and total%2 :
# #                     ans += 1
            
# #         return ans


            
# from collections import defaultdict, deque, Counter
# import heapq
# from functools import lru_cache
# from itertools import combinations

# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.size = [1] * n
    
#     def find(self, node):
#         if self.parent[node] != node:
#             self.parent[node] = self.find(self.parent[node])
#         return self.parent[node]
    
#     def union(self, x, y):
#         root_x, root_y = self.find(x), self.find(y)
#         if root_x == root_y:
#             return False
        
#         self.parent[root_x] = root_y
#         self.size[root_y] += self.size[root_x]
#         return True

# class Solution:
#     def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
#         n = len(nums)
#         graph = defaultdict(list)
        
#         dsu = DSU(n)
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
#             dsu.union(u, v)
        
#         nodes = list(range(n))
#         ans = 0
        
#         # Iterate through all combination sizes (from size 1 to n)
#         for r in range(1, n + 1):
#             for subset in combinations(nodes, r):
#                 prev_root = -1
#                 total = 0
#                 chk = True
                
#                 # Iterate directly over the elements in the subset tuple
#                 for curr_node in subset:
#                     total += nums[curr_node]
#                     curr_root = dsu.find(curr_node)
                    
#                     if prev_root == -1:
#                         prev_root = curr_root
#                     elif prev_root != curr_root:
#                         chk = False
#                         break
                
#                 if chk and total % 2 == 0:  # Note: Checked for even sum (total % 2 == 0)
#                     ans += 1
        
#         return ans

from collections import defaultdict, deque, Counter
import heapq
from functools import lru_cache
from itertools import combinations


class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:

        n = len(nums)

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0

        nodes = list(range(n))

        for r in range(1, n + 1):

            for subset in combinations(nodes, r):

                # ------------------------------------------------
                # Check sum
                # ------------------------------------------------

                total = 0

                for node in subset:
                    total += nums[node]

                if total % 2 != 0:
                    continue

                # ------------------------------------------------
                # Check connectivity of induced subgraph
                # ------------------------------------------------

                selected = set(subset)

                q = deque([subset[0]])
                visited = {subset[0]}

                while q:

                    node = q.popleft()

                    for nei in graph[node]:

                        if nei in selected and nei not in visited:
                            visited.add(nei)
                            q.append(nei)

                if len(visited) == len(subset):
                    ans += 1

        return ans