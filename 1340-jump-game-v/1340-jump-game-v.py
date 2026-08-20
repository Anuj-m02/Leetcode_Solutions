from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        n = len(arr)

        graph = defaultdict(list)
        indegree = [0]*(n)

        for i in range(n) :
            # jump right
            for x in range(1 , d+1) :
                j = i + x
                if j >= n or arr[j] >= arr[i] :
                    break
                graph[i].append(j)
                indegree[j] += 1
            
            # jump left
            for x in range(1 , d+1) :
                j = i - x
                if j < 0 or arr[j] >= arr[i] :
                    break
                graph[i].append(j)
                indegree[j] += 1
        
        queue = deque([])
        dist = [1]*(n)

        for i in range(n) :
            if indegree[i] == 0 :
                queue.append(i)
        max_visited = 1

        while queue :
            curr_node = queue.popleft()
            max_visited = max(max_visited , dist[curr_node])

            for neighbour in graph[curr_node] :
                dist[neighbour] = max(dist[neighbour] , dist[curr_node] + 1)
            
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0 :
                    queue.append(neighbour)
        
        return max_visited
        