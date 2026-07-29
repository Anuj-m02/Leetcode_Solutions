from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        
        ans = -1
        n = len(online)
        graph = defaultdict(list)

        low = 0 
        high = -1

        def check(mid) :

            # curr_cost , curr_node
            heap = [(0 , 0 )]
            dist = [float("inf")]*(n)
            dist[0] = 0

            while heap :
                curr_cost , curr_node = heapq.heappop(heap)

                if curr_cost > dist[curr_node] :
                    continue


                if curr_node == n-1 and curr_cost <= k :
                    return True

                for neighbour , cost in graph[curr_node] :
                    if online[neighbour] :
                        
                        if cost >= mid :

                            new_cost , new_node = curr_cost + cost , neighbour

                            if new_cost <= k and new_cost < dist[new_node]:
                                heapq.heappush(heap , (new_cost , new_node ))
                                dist[new_node] = new_cost
            
            return False

        for u , v , cost in edges:
            graph[u].append((v,cost))
            high = max(high , cost)
        
        # start from 0th node 
        # (curr_cost , curr_node , min_edge_val)
        heap = [(0 , 0 , float("inf"))]


        while low <= high :
            mid = (low+high)//2

            if check(mid) :
                low = mid+1
                ans = mid
            else :
                high = mid-1
        
        return ans

        

