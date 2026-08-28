from collections import defaultdict ,deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for u , v in edges :
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        

        dist = [[0]*n for _ in range(n)]

        for start in range(n):
            queue = deque([(start , 0)])

            vis = {start}
            while queue :
                curr , d = queue.popleft()
                dist[start][curr] = d
                for neighbour in graph[curr] :
                    if neighbour not in vis :
                        vis.add(neighbour)
                        queue.append((neighbour , d+1))
        

        def compute_distance(nodes) :
            max_d = 0
            node_list = list(nodes)
            for i in range(len(node_list)) :
                for j in range(i+1 , len(node_list)) :
                    max_d = max(max_d , dist[node_list[i]][node_list[j]])
            
            return max_d
        
        ans = [0]*(n-1)
        visited_subtrees = set()

        @cache
        def dp(subtree) :

            if subtree in visited_subtrees :
                return 

            visited_subtrees.add(subtree) 

            if len(subtree) >= 2 :
                d = compute_distance(subtree)
                ans[d-1] += 1
            
            for node in subtree :
                for neighbour in graph[node] :
                    if neighbour not in subtree :
                        dp(subtree | frozenset([neighbour]))
        
        for i in range(n):
            dp(frozenset([i]))
        
        return ans


