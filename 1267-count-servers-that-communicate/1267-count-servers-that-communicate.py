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
    def countServers(self, grid: list[list[int]]) -> int:

        n , m = len(grid) , len(grid[0])

        dsu = DSU(n*m + 1)
        x_map = defaultdict(list)
        y_map = defaultdict(list)

        for row in range(n):
            for col in range(m) :
                if grid[row][col] == 1 :
                    x_map[row].append(col)
                    y_map[col].append(row)
        
        for row , cols in x_map.items() :
            first_id = row*m + cols[0]
            for c in cols[1:] :
                curr_id = row*m + c
                dsu.union(first_id , curr_id)
        
        for col , rows in y_map.items() :
            first_id = rows[0]*(m) + col
            for r in rows[1:] :
                curr_id = r*m + col
                dsu.union(first_id , curr_id)
        

        cnt = 0
        for row in range(n):
            for col in range(m) :
                if grid[row][col] == 1 :
                    cell_id = row*m + col
                    root = dsu.find(cell_id)
                    if dsu.size[root] > 1 :
                        cnt += 1
        
        return cnt
