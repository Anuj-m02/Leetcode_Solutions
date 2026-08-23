from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque([])
        self.cache = {} # key - > val
        self.heap = [] 
        self.freq = defaultdict(int) # key -> frequency
        self.time = 0

    def get(self, key: int) -> int:

        if key not in self.cache :
            return -1
        
        self.freq[key] += 1
        self.time += 1
        heapq.heappush(self.heap , (self.freq[key] , self.time , key))
        return self.cache[key]

        

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0 :
            return

        if key in self.cache :
            self.cache[key] = value
            self.get(key)
            return

        if len(self.cache) >= self.capacity :
            while self.heap :
                f , t , k = heapq.heappop(self.heap)

                if k in self.cache and self.freq[k] == f :
                    del self.cache[k]
                    del self.freq[k]
                    break
        
        self.cache[key] = value
        self.freq[key] = 1
        self.time += 1
        heapq.heappush(self.heap , (1 , self.time , key))
        


# # Your LFUCache object will be instantiated and called as such:
# # obj = LFUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

import heapq
from collections import defaultdict, deque

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}          # key -> value
        self.freq = defaultdict(int)  # key -> frequency
        self.time = 0            # Global timer for LRU tie-breaking
        self.heap = []           # Stores (frequency, time, key)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.freq[key] += 1
        self.time += 1
        heapq.heappush(self.heap, (self.freq[key], self.time, key))
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self.get(key)  # Updates frequency and timestamp
            return

        # Evict least frequently used if capacity is reached
        if len(self.cache) >= self.capacity:
            while self.heap:
                f, t, k = heapq.heappop(self.heap)
                # Verify entry is stale (key's latest freq/time match the heap top)
                if k in self.cache and self.freq[k] == f:
                    del self.cache[k]
                    del self.freq[k]
                    break

        self.cache[key] = value
        self.freq[key] = 1
        self.time += 1
        heapq.heappush(self.heap, (1, self.time, key))