import heapq
from collections import defaultdict, deque
from functools import lru_cache

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:

        if not edges :
            return max(vals)
        
        n = len(vals)

        graph = defaultdict(list)
        degree = [0]*(n)

        start = []

        for u,v in edges :
            graph[u].append((vals[v] , v))
            graph[v].append((vals[u] , u))
            degree[u] += 1
            degree[v] += 1



        # # contestants
        # heap = []
        # for node in range(n):
        #     if degree[node] >= k :
        #         heap.append(node)
        # # curr_cost , curr_node

        # if not heap :
        #     return max(vals)

        for items in graph.values() :
            items.sort(key = lambda x : x[0] , reverse = True)

        ans = float("-inf")

        for curr_node in range(n) :
            temp = vals[curr_node]
            cnt = 0

            for val , neighbour in graph[curr_node] :
                if cnt >= k or val <= 0 :
                    break
                
                temp += val
                cnt += 1
            
            ans = max(ans , temp)
        
        return ans



        # while heap :
        #     print(heap)
        #     temp = 0
        #     curr_node = heapq.heappop(heap)
        #     temp += vals[curr_node]
        #     cnt = 0
        #     for val , neighbour in graph[curr_node] :
        #         print(val , neighbour)
        #         if cnt >= k :
        #             break
        #         cnt += 1
        #         temp += val

        #         print(temp)
            
        #     ans = max(ans , temp)
        
        # return ans


