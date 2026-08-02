# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache

# class DSU :

#     def __init__(self , n) :
#         self.parent = list(range(n+1))
#         self.size = [1]*(n)
#         self.components = n
    
#     def find(self , node) :
#         if self.parent[node] != node :
#             self.parent[node] = self.find(self.parent[node])
        
#         return self.parent[node]
    
#     def union(self , x , y) :
#         root_x , root_y = self.find(x)  , self.find(y)
#         if root_x == root_y :
#             return False
        
#         if self.size[root_x] < self.size[root_y] :
#             self.parent[root_x] = root_y
#             self.size[root_y] += self.size[root_x]
        
#         else :
#             self.parent[root_y] = root_x
#             self.size[root_x] += self.size[root_y]
        
#         self.components -= 1
#         return True



# class Solution:
#     def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
#         dsu = DSU(n)
#         required = []
#         optional = []

#         max_val = 0
#         for u , v , w , must in edges :
#             max_val = max(max_val , w*2)
#             if must == 1 :
#                 required.append((u,v,w))
#             else :
#                 optional.append((u,v,w))
        
#         for u, v , w in required  :
#             if not dsu.union(u,v) :
#                 return -1
        
#         def check(target) :
#             nonlocal k
#             dsu = DSU(n)
#             used = 0

#             for u,v,w in required :
#                 if w < target :
#                     return False
#                 dsu.union(u,v)
            
#             not_used = []
#             for u,v,w in optional :
#                 if w >= target :
#                     dsu.union(u,v)
#                 else :
#                     not_used.append((u,v,w))
            
#             for u,v,w in not_used :
#                 if 2*w >= target and k > 0 :
#                     if dsu.union(u,v) :
#                         k -= 1
            
#             return dsu.components == 1
        

#         low , high = 1 , max_val
#         ans = -1
        
#         while low <= high :
#             mid = (low+high)//2
#             if check(mid) :
#                 ans = mid
#                 low = mid+1
#             else :
#                 high = mid-1
        
#         return ans



from collections import defaultdict, deque, Counter
import heapq
from functools import lru_cache
from typing import List

class DSU:

    def __init__(self, n):
        self.parent = list(range(n))  # Fixed: size n to match indices 0 to n-1
        self.size = [1] * n
        self.components = n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        
        self.components -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        dsu = DSU(n)
        required = []
        optional = []

        max_val = 0
        for u, v, w, must in edges:
            max_val = max(max_val, w * 2)
            if must == 1:
                required.append((u, v, w))
            else:
                optional.append((u, v, w))
        
        for u, v, w in required:
            if not dsu.union(u, v):
                return -1
        
        def check(target):
            dsu = DSU(n)
            upgrades_left = k  # Fixed: Local copy of k so binary search calls don't corrupt k

            for u, v, w in required:
                if w < target:
                    return False
                dsu.union(u, v)
            
            not_used = []
            for u, v, w in optional:
                if w >= target:
                    dsu.union(u, v)
                else:
                    not_used.append((u, v, w))
            
            for u, v, w in not_used:
                if 2 * w >= target and upgrades_left > 0:
                    if dsu.union(u, v):
                        upgrades_left -= 1  # Fixed: decrement local tracker
            
            return dsu.components == 1
        
        low, high = 1, max_val
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans