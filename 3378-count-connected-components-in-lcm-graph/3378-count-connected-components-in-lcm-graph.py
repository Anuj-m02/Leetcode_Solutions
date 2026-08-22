# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache


# class DSU :
#     def __init__(self , n) :
#         self.parent = list(range(n))
#         self.size = [1]*(n)
#         self.components = n
    

#     def find(self , node) :
#         if self.parent[node] != node :
#             self.parent[node] = self.find(self.parent[node])
#         return self.parent[node]
    
#     def union(self , a , b) :
#         root_a , root_b = self.find(a) , self.find(b)

#         if root_a == root_b :
#             return False
        
#         self.parent[root_a] = root_b
#         self.size[root_b] += self.size[root_a]
#         self.components -= 1
#         return True
    


# class Solution:
#     def countComponents(self, nums: List[int], threshold: int) -> int:
        
#         n = len(nums)
#         s = set(nums)

#         dsu = DSU(n)

#         visited = [0]*(threshold+1)

#         for i in range(n) :

#             curr_num = nums[i]
#             if curr_num > threshold :
#                 continue
#             for j in range(curr_num , threshold+1 , curr_num) :

#                 if not visited[j] :
#                     dsu.union(i , j)
                
#                 else :
#                     visited[j] = i
        
#         return dsu.components


from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return False
        
        self.parent[root_a] = root_b
        self.size[root_b] += self.size[root_a]
        self.components -= 1
        return True
    

class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        dsu = DSU(n)

        # Replaces 's = set(nums)'. Tracks which index first reached multiple 'j'
        multiple_visited_by = [-1] * (threshold + 1)

        for i in range(n):
            curr_num = nums[i]
            
            # Numbers > threshold cannot share an LCM <= threshold. Skip them.
            if curr_num > threshold:
                continue
                
            # Your exact loop: iterate through multiples up to the threshold
            for j in range(curr_num, threshold + 1, curr_num):
                if multiple_visited_by[j] != -1:
                    # Union the current index 'i' with the index that visited this multiple earlier
                    dsu.union(i, multiple_visited_by[j])
                else:
                    # Mark this multiple as visited by index 'i'
                    multiple_visited_by[j] = i
        
        return dsu.components