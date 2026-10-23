from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class DSU :
    def __init__(self , n) :
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.comp = n
    
    def find(self , node) :
        if self.parent[node] != node :
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]

    def union(self , a , b) :
        root_a , root_b = self.find(a) , self.find(b)

        if root_a == root_b :
            return False
        
        self.parent[root_a] = root_b
        self.size[root_b] += self.size[root_a]
        self.comp -= 1

        return True


class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])

        def check(str1 , str2) :
            cnt = 0
            for i in range(m) :
                if str1[i] != str2[i] :
                    cnt += 1
            
            return cnt <= 2


        dsu = DSU(n)

        for i in range(n) :
            for j in range(i+1 , n) :
                if check(strs[i] , strs[j]) :
                    dsu.union(i , j)
        
        return dsu.comp
