from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        n = len(source)
        graph = defaultdict(list)
        for i in range(len(cost)) :
            graph[original[i]].append((changed[i] , cost[i]))
        
        # these need to be changed
        candid = list(set(original))

        # print(candid)

        @lru_cache(None)
        def dijkstra(start) :

            dist = {start : 0}
            heap = [(0,start)]

            while heap :
                curr_cost , curr_node = heapq.heappop(heap)

                if curr_cost > dist[curr_node] :
                    continue
                
                for neighbour , wt in graph[curr_node]:
                    new_cost = curr_cost + wt

                    if neighbour not in dist or new_cost < dist[neighbour] :
                        dist[neighbour] = new_cost
                        heapq.heappush(heap , (new_cost , neighbour))
            
            return dist
        
        # dp(indx) to convert source[indx:] to target[indx:]

        @lru_cache(None)
        def dp(indx) :

            if indx == n :
                return 0
            
            ans = float("inf")

            # option1 chars alrdy equal
            if source[indx] == target[indx] :
                ans = dp(indx+1)
            
            # option2 choose a original string starting at indx 
            for s in candid :
                length = len(s)

                # print(length)
                if indx + length > n :
                    continue
                
                if source[indx : indx+length] != s :
                    continue
                
                t = target[indx : indx+length]

                if s == t :
                    continue
                
                dist = dijkstra(s)
                if t not in dist :
                    continue
                
                curr = dist[t] + dp(indx+length)
                ans = min(ans , curr)
            
            return ans
        
        res = dp(0)

        return -1 if res == float("inf") else res
