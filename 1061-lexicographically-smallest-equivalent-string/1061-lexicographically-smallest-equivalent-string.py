from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class DSU :
    def __init__(self , n) :
        self.n = n
        self.parent = list(range(n))
        self.size = [1]*(n)
    
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
        return True


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        

        n = len(s1)

        m = len(baseStr)

        dsu = DSU(26)

        for i in range(n) :
            a , b = ord(s1[i]) - ord("a") , ord(s2[i]) - ord("a")
            dsu.union(a , b)
        

        res = ""
        for i in range(m) :
            curr = baseStr[i]
            end = ord(curr) - ord("a")
            root = dsu.find(end)
            chk = False
            for j in range(0 , end) :
                if dsu.find(j) == root :
                    res += chr(ord("a") + j)
                    chk = True
                    break
            if not chk :
                res += curr

        return res