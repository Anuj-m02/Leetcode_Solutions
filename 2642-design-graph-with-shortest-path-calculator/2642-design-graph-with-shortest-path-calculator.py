from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):

        self.n = n
        self.graph = defaultdict(list)
        for u , v , w in edges :
            self.graph[u].append((v,w))
        

    def addEdge(self, edge: List[int]) -> None:

        u , v , w = edge
        self.graph[u].append((v,w))

        

    def shortestPath(self, node1: int, node2: int) -> int:

        dist = [float("inf")]*(self.n)

        # curr_wt , curr_node
        heap = [(0,node1)]
        dist[node1] = 0

        while heap :
            curr_wt , curr_node = heapq.heappop(heap)

            if dist[curr_node] < curr_wt :
                continue
            
            for neighbour , wt in self.graph[curr_node] :
                new_wt = curr_wt + wt
                if dist[neighbour] > new_wt :
                    dist[neighbour] = new_wt
                    heapq.heappush(heap , (new_wt , neighbour))
        
        if dist[node2] == float("inf") :
            return -1
        else :
            return dist[node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)