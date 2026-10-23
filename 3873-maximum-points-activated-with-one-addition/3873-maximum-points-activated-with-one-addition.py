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
    def maxActivated(self, points: list[list[int]]) -> int:
        
        n = len(points)

        # count no of components with their size
        dsu = DSU(n)

        x_map = {}
        y_map = {}

        # if there is a single compon return its size+1
        # if there are more than one comp return max two sizes + 1

        for indx , (x,y) in enumerate(points) :
            if x in x_map :
                dsu.union(indx , x_map[x])
            
            else :
                x_map[x] = indx
            
            if y in y_map :
                dsu.union(indx , y_map[y])
            
            else :
                y_map[y] = indx
        

        comp_sizes = []
        for i in range(n) :
            if dsu.find(i) == i :
                comp_sizes.append(dsu.size[i])


        comp_sizes.sort(reverse=True)

        if len(comp_sizes) == 1 :
            return comp_sizes[0] + 1
        else :
            return comp_sizes[0] + comp_sizes[1] + 1



