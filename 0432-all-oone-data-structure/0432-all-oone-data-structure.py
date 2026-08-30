# from collections import defaultdict , deque , Counter
# import heapq



# class AllOne:

#     def __init__(self):
#         self.count = {}
#         self.heap = []
#         self.deleted = set()
        

#     def inc(self, key: str) -> None:

#         if key not in self.count :
#             self.count[key] = 1
#             # heapq.heappush(heap , (1 , key))
        
#         else :
#             self.count[key] += 1

#         heapq.heappush(self.heap , (self.count[key] , key))


        

#     def dec(self, key: str) -> None:

#         self.count[key] -= 1
#         if self.count[key] == 0 :
#             del self.count[key]
#             deleted.add(key)
        
#         if self.count[key] :
#             heapq.heappush(self.heap , (self.count[key] , key))


#     def getMaxKey(self) -> str:

#         # heapq.heapify(self.heap)
#         print(self.heap)
#         max_key = self.heap[-1]
#         return max_key[1]


#     def getMinKey(self) -> str:

#         return self.heap[0][1]   
        


# # Your AllOne object will be instantiated and called as such:
# # obj = AllOne()
# # obj.inc(key)
# # obj.dec(key)
# # param_3 = obj.getMaxKey()
# # param_4 = obj.getMinKey()


import heapq

class AllOne:

    def __init__(self):
        self.count = {}
        self.min_heap = []  # (count, key)
        self.max_heap = []  # (-count, key)

    def inc(self, key: str) -> None:
        self.count[key] = self.count.get(key, 0) + 1
        cnt = self.count[key]
        heapq.heappush(self.min_heap, (cnt, key))
        heapq.heappush(self.max_heap, (-cnt, key))

    def dec(self, key: str) -> None:
        self.count[key] -= 1
        if self.count[key] == 0:
            del self.count[key]
        else:
            cnt = self.count[key]
            heapq.heappush(self.min_heap, (cnt, key))
            heapq.heappush(self.max_heap, (-cnt, key))

    def getMaxKey(self) -> str:
        # Clean up stale/outdated entries from top of heap
        while self.max_heap:
            neg_cnt, key = self.max_heap[0]
            if key in self.count and self.count[key] == -neg_cnt:
                return key
            heapq.heappop(self.max_heap)
        return ""

    def getMinKey(self) -> str:
        # Clean up stale/outdated entries from top of heap
        while self.min_heap:
            cnt, key = self.min_heap[0]
            if key in self.count and self.count[key] == cnt:
                return key
            heapq.heappop(self.min_heap)
        return ""
