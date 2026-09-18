from collections import defaultdict , deque
from functools import lru_cache

import heapq

class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        
        graph = defaultdict(list)
        indegree = [0]*(n)
        parents = defaultdict(list)
        if not edges:
            return sum((i + 1) * s for i, s in enumerate(sorted(score)))
        #  u->v directed graph
        for u,v in edges :
            graph[u].append(v)
            indegree[v] += 1
            parents[v].append(u)
        
        @lru_cache(maxsize=None)
        def dfs(state):

            # print(state)
            
            if len(state) == n :
                return 0
            
            pos = len(state) + 1
            ans = 0

            for node in range(n) :

                if node in state :
                    continue
                ok = True

                for p in parents[node] :
                    if p not in state :
                        ok = False
                        # print("i am here")
                        break
                if ok :
                    ans = max(ans, score[node] * pos + dfs(state | frozenset([node])))
            
            return ans
        
        return dfs(frozenset())