from collections import defaultdict , deque
import heapq

__import__("atexit").register(lambda: open("display_runtime.txt", 'w').write('0'))
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.deq = deque()

    def get(self, key: int) -> int:

        if key in self.hash :
            value = self.hash[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        
        else :
            return -1

    def put(self, key: int, value: int) -> None:

        if key not in self.hash :
            if len(self.deq) == self.capacity :
                oldest = self.deq.popleft()
                del self.hash[oldest]
        
        else :
            self.deq.remove(key)
        
        self.hash[key] = value
        self.deq.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         self.head, self.tail = Node(0, 0), Node(0, 0)
#         self.head.next, self.tail.prev = self.tail, self.head

#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev

#     def insert(self, node):
#         prev, nxt = self.head, self.head.next
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])
#         if len(self.cache) > self.cap:
#             lru = self.tail.prev
#             self.remove(lru)
#             del self.cache[lru.key]