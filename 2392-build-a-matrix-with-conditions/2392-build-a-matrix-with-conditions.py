from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:

        def topo_sort(condition) :
            graph = defaultdict(list)
            indegree = [0]*(k+1)

            # above -> below
            for u,v in condition:
                graph[u].append(v)
                indegree[v] += 1

            queue = deque([i for i in range(1,k+1) if indegree[i] == 0])
            order = []

            while queue :
                curr = queue.popleft()
                order.append(curr)
                for neighbour in graph[curr] :
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0 :
                        queue.append(neighbour)
            
            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        # print(row_order)
        # print(col_order)

        if not row_order or not col_order :
            return []
        
        row_pos = {num : i for i,num in enumerate(row_order)}
        col_pos = {num : i for i,num in enumerate(col_order)}

        # print(row_pos)
        # print(col_pos)

        matrix = [[0]*k for _ in range(k)]
        for num in range(1 , k+1) :
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix