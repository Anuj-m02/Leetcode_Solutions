from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        
        # i have developed an algo to do this ques , 
        # we will store the starting node i.e 0 {0 , moves_left}
        # heap will be there which will have {cnt i.e number of node in between node a and  b,  a , b , moves_left  , and thereby incrementing ans += }
        # got it , now lets code this 

        graph = defaultdict(list)
        for u,v,cnt in edges :
            graph[u].append((v,cnt))
            graph[v].append((u,cnt))
        
        max_moves_at_node = {}
        visited_subnodes = {}

        heap = [(-maxMoves , 0)]

        while heap :
            neg_moves , node = heapq.heappop(heap)
            moves_left = -neg_moves
            # alrdy visited this node with more moves left
            if node in max_moves_at_node and max_moves_at_node[node] >= moves_left :
                continue

            max_moves_at_node[node] = moves_left

            for neighbour , cnt in graph[node] :
                take = min(cnt , moves_left)
                visited_subnodes[(node,neighbour)] = take

                if moves_left >= cnt+1 :
                    remaining_after_neighbour = moves_left - (cnt+1)
                    if neighbour not in max_moves_at_node or max_moves_at_node[neighbour] < remaining_after_neighbour :
                        heapq.heappush(heap , (-remaining_after_neighbour , neighbour))

        ans = len(max_moves_at_node)

        for u,v,cnt in edges :
            from_u = visited_subnodes.get((u,v),0)
            from_v = visited_subnodes.get((v,u),0)

            ans += min(cnt , from_u+from_v)

        return ans 

