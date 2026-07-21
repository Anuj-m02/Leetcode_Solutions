from collections import defaultdict , deque
import heapq
from functools import lru_cache


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        denied = defaultdict(list)
        # for restriction (u,v -1) -1 denotes restrcited okay
        for u , v in restrictions :
            denied[u].append(v)
            denied[v].append(u)
        
        parent = list(range(n))
        size = [1]*(n)

        def find(node) :
            if parent[node] != node :
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(x , y) :
            root_x , root_y = find(x) , find(y)

            if root_x == root_y :
                return True
            
            if size[root_x] < size[root_y] :
                parent[root_x] = root_y
                size[root_y] += size[root_x]
            else :
                parent[root_y] = root_x
                size[root_x] += size[root_y]
        
        m = len(requests)
        ans = [False]*m

        for indx in range(m) :
            u , v = requests[indx]
            root_u , root_v = find(u) , find(v)

            if root_u == root_v :
                ans[indx] = True
                continue
            else :
                chk = True
                for x,y in restrictions :
                    root_x , root_y = find(x) , find(y)
                    if (root_x == root_u and root_y == root_v) or (root_x == root_v and root_y == root_u) :
                        chk = False
                        break
                if chk :
                    graph[u].append(v)
                    graph[v].append(u)
                    union(u,v)
                    ans[indx] = True
        
        return ans


        

