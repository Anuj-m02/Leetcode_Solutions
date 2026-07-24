from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:

        graph = defaultdict(list)
        for u , v , w in edges :
            graph[u].append((v,w))
            graph[v].append((u,w))

        time = [float("inf")]*(n)

        # queue = deque([]) 
        queue = []
        queue.append((0,0))
        time[0] = 0
        while queue :
            curr_time , curr_node = heapq.heappop(queue)

            if curr_time > time[curr_node] :
                continue

            for neighbour , weight in graph[curr_node] :
                if time[neighbour] > time[curr_node] + weight and disappear[neighbour] > time[curr_node] + weight :
                    time[neighbour] = time[curr_node] + weight
                    # queue.append((neighbour,time[neighbour]))
                    heapq.heappush(queue , (time[neighbour] , neighbour))
        
        ans = []
        for i in range(n):
            if time[i] == float("inf") :
                ans.append(-1)
            else :
                ans.append(time[i])
        
        return ans
