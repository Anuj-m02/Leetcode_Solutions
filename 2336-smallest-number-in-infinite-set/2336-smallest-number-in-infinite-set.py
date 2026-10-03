from collections import defaultdict, deque , Counter
import heapq
from functools import lru_cache

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1 , 1001))
        self.s = set(self.heap)
        heapq.heapify(self.heap)
        

    def popSmallest(self) -> int:
        
        num = heapq.heappop(self.heap)
        self.s.remove(num)
        return num



    def addBack(self, num: int) -> None:

        if num in self.s :
            return
        
        else :
            heapq.heappush(self.heap , num)
            self.s.add(num)
            return

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)