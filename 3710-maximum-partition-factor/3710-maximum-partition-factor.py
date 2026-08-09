# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache

# class DSU:

#     def __init__(self, size: int):
#         self.parent = list(range(size))

#     def find(self, i: int) -> int:
#         if self.parent[i] == i:
#             return i
#         self.parent[i] = self.find(self.parent[i])  # Path compression
#         return self.parent[i]

#     def union(self, i: int, j: int):
#         root_i = self.find(i)
#         root_j = self.find(j)
#         if root_i != root_j:
#             self.parent[root_i] = root_j



# class Solution:
#     def maxPartitionFactor(self, points: List[List[int]]) -> int:

#         n = len(points)

#         # we have to divide in 2 grps , so the max(min(distance)) so definitely binary search

#         def check(mid) :
            
#             dsu = DSU(2*n)
#             for i in range(n) :
#                 for j in range(i+1 , n) :
#                     x1 , y1 = points[i]
#                     x2 , y2 = points[j]
#                     dist = abs(x1-x2) + abs(y1-y2)
#                     if dist <= mid :
#                         dsu.union(i, j+n)
#                         dsu.union(i+n , j)

#                         if dsu.find(i) == dsu.find(i+n) :
#                             return False
#             return True 


#         low = 0
#         high = int(1e9)
#         ans = -1
        
#         while low <= high :
#             mid = (low) + (high-low)//2

#             if check(mid) :
#                 ans = mid
#                 low = mid+1
#             else :
#                 high = mid-1
        
#         return ans

from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq
from typing import List


class DSU:

    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j


class Solution:

    def maxPartitionFactor(self, points: List[List[int]]) -> int:

        n = len(points)
        if n <= 2:
            return 0

        # We have to divide in 2 grps , so max(min(distance)) -> binary search
        def check(mid):
            dsu = DSU(2 * n)
            for i in range(n):
                for j in range(i + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < mid:
                        dsu.union(i, j + n)
                        dsu.union(i + n, j)

                        if dsu.find(i) == dsu.find(i + n):
                            return False
            return True

        low = 0
        high = 4 * 10**9  # Fixed: accommodates maximum possible Manhattan distance
        ans = -1

        while low <= high:
            mid = (high+low)//2

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans