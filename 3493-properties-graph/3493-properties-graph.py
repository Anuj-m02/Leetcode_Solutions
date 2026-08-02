from collections import defaultdict , deque , Counter
import heapq

from functools import lru_cache


class DSU :
    
    def __init__(self , n) :
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.components = n
    
    def find(self , node) :
        if self.parent[node] != node :
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self , x , y) :

        root_x , root_y = self.find(x) , self.find(y)

        if root_x == root_y :
            return False
        
        if self.size[root_x] <= self.size[root_y] :
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        
        else :
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        
        self.components -= 1
        return True
    

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:

        n = len(properties)

        dsu = DSU(n)

        for i in range(n) :
            for j in range(n) :
                if i != j :
                    s1 , s2 = set(properties[i]) , set(properties[j])
                    res = s1.intersection(s2)
                    if len(res) >= k :
                        dsu.union(i,j)
        
        return dsu.components