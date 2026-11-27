from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class DSU :
    def __init__(self , n) :
        self.parent = list(range(n))
        self.size = [1]*(n)
    
    def find(self , node) :
        if self.parent[node] != node :
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self , a, b) :
        root_a , root_b = self.find(a) , self.find(b)

        if root_a == root_b :
            return False
        
        self.size[root_a] += self.size[root_b]
        self.parent[root_b] = root_a
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        # n = len(nums)
        if not nums :
            return 0

        d = {}
        nums = list(set(nums))
        n = len(nums)

        dsu = DSU(n)

        for i in range(n):
            curr = nums[i]

            if curr-1 in d :
                dsu.union(i , d[curr-1])
            
            if curr+1 in d :
                dsu.union(i , d[curr+1])
            
            d[curr] = i
        
        return max(dsu.size)



        # s = set(nums)
        # maxi = 0
        # for i in s :
        #     if i-1 not in s :
        #         length = 1
        #         while i+1 in s :
        #             i += 1
        #             length += 1
        #         maxi = max(length,maxi)
        # return maxi