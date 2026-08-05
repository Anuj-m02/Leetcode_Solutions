from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        # n = len(parent)

        # graph = defaultdict(list)
        # for i in range(1,n):
        #     graph[i].append(parent[i])
        #     graph[parent[i]].append(i)
    
        # vis = [0]*(n)
        # maxi = -1
        # queue = deque([(0,0)])

        # while queue :
        #     curr_node , curr_len = queue.popleft()
        #     curr_val = s[curr_node]
        #     maxi = max(maxi , curr_len)
        #     for neighbours in graph[curr_node] :
        #         if s[neighbours] != curr_val :
        #             curr_len += 1
        #             queue.append((neighbours,curr_len))
        #         else :
        #             queue.append((neighbours , 0))


        # return maxi 

        n = len(parent)
        graph = defaultdict(list)

        for i in range(1 , n) :
            u = i
            v = parent[i]
            graph[u].append(v)
            graph[v].append(u)
        
        @lru_cache(maxsize=None)
        def dp(node , par) :

            ans = 0
            for neighbour in graph[node] :
                if neighbour != par :
                    if s[neighbour] != s[node] :
                        ans = max(ans , 1+ dp(neighbour , node))
            
            if ans == 0 :
                ans = 1

            return ans
        
        res = 0
        for i in range(n) :
            res = max(res , dp(i , -1))
        
        return res
