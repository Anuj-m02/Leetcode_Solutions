import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        heap = [-val for val in freq.values()]
        heapq.heapify(heap)

        time = 0
        while heap :
            cycle = []
            for _ in range(n+1) :
                if heap :
                    cnt = heapq.heappop(heap)
                    cycle.append(cnt)
            for cnt in cycle :
                if cnt+1 < 0 :
                    heapq.heappush(heap , cnt+1)
            
            if heap :
                time += n+1
            else :
                time += len(cycle)
        
        return time