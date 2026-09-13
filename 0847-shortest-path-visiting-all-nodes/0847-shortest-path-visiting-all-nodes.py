from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1 :
            return 0
        # curr_node , visited_set , distance
        queue = deque()
        visited_states = set()
        for i in range(n):
            visited_set = frozenset([i])
            queue.append((i , visited_set , 0))
            visited_states.add((i , visited_set))
        
        while queue :
            node , visited_set , dist = queue.popleft()

            if len(visited_set) == n :
                return dist
            
            for neighbour in graph[node]:
                new_visited = visited_set | frozenset([neighbour])
                state = (neighbour , new_visited)
                if state not in visited_states :
                    visited_states.add(state)
                    queue.append((neighbour , new_visited ,dist+1))
        return -1 