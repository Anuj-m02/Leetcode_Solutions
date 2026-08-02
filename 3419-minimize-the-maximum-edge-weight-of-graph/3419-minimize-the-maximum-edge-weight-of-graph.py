from collections import defaultdict, deque , Counter
import heapq
from functools import lru_cache
from typing import List

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:


        graph = defaultdict(list)
        indegree = [0]*(n)
        max_val = float('-inf')
        # building revserse graph so run a bfs and check if all nodes visible from node 0
        for u , v , w in edges :
            max_val = max(max_val , w)
            graph[v].append((u,w))
            indegree[v] += 1
        
        def check(target) :
            # dist , node
            heap = [(0,0)]
            dist = [float('inf')]*(n)
            dist[0] = 0

            while heap :

                curr_weight , curr_node = heapq.heappop(heap)

                if dist[curr_node] < curr_weight :
                    continue
                
                for neighbour , wt in graph[curr_node] :
                    new_wt = curr_weight + wt
                    if dist[neighbour] > new_wt and wt <= target :
                        dist[neighbour] = new_wt
                        indegree[neighbour] -= 1
                        heapq.heappush(heap , (new_wt , neighbour))
            
            if float("inf") in dist :
                return False
            
            return True


        
        low , high = 0 , max_val
        ans = -1
        while low <= high :
            mid = (low+high)//2
            if check(mid) :
                ans = mid
                high = mid-1
            else :
                low = mid+1
        
        return ans