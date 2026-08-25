# # # class FreqStack:

# # #     def __init__(self):
# # #         self.stack = []
# # #         self.map1 = defaultdict(list)
# # #         # {5 : [0 , 2 , 5] , ,7 :[1 , 3] , 4 :4}
# # #         #(val : [all_indxs])
# # #         self.map2 = {}
# # #         # {5 : (3, 5) , 7 :{2 , 3} , 4:{1 , 4}}
# # #         # (val : (count , recnt_indx))
# # #         self.indx = 

# # #     def push(self, val: int) -> None:
        
# # #         self.stack.append((val , indx))
# # #         self.map1[self.val].append(indx)
# # #         self.map2[self.val]
        

# # #     def pop(self) -> int:
    


# # # # Your FreqStack object will be instantiated and called as such:
# # # # obj = FreqStack()
# # # # obj.push(val)
# # # # param_2 = obj.pop()

# # from collections import defaultdict

# # class FreqStack:

# #     def __init__(self):
# #         self.stack = []  
# #         # (val, index)

# #         self.map1 = defaultdict(list)
# #         # val -> [all occurrence indices]

# #         self.map2 = {}
# #         # val -> [frequency, recent_index]

# #         self.indx = 0

# #     def push(self, val: int) -> None:

# #         # Add to stack
# #         self.stack.append((val, self.indx))

# #         # Store occurrence index
# #         self.map1[val].append(self.indx)

# #         # Update frequency and recent index
# #         if val not in self.map2:
# #             self.map2[val] = [1, self.indx]
# #         else:
# #             self.map2[val][0] += 1
# #             self.map2[val][1] = self.indx

# #         self.indx += 1

# #     def pop(self) -> int:

# #         # Find:
# #         # 1. maximum frequency
# #         # 2. among those, maximum recent index

# #         temp = []

# #         for key , val in map2 :
# #             a , b = val
# #             temp.append((a,b , key))
        
# #         temp.sort(reverse=True)

# #         max_cnt , max_indx , val = temp[0]

# #         map1[val].remove(max_indx)
# #         latest_indx = map1[val][-1]
# #         if max_cnt-1 == 0 :
# #             del map2[val]
# #         map2[val] = [max_cnt-1 , latest_indx]

# #         return max_cnt


# #         # best_val = -1
# #         # best_freq = -1
# #         # best_index = -1

# #         # for val, (freq, recent_index) in self.map2.items():

# #         #     if freq > best_freq:
# #         #         best_freq = freq
# #         #         best_index = recent_index
# #         #         best_val = val

# #         #     elif freq == best_freq and recent_index > best_index:
# #         #         best_index = recent_index
# #         #         best_val = val

# #         # # Remove latest occurrence of best_val
# #         # self.map1[best_val].pop()

# #         # # Update frequency and recent index
# #         # self.map2[best_val][0] -= 1

# #         # if self.map2[best_val][0] == 0:
# #         #     del self.map2[best_val]
# #         #     del self.map1[best_val]
# #         # else:
# #         #     self.map2[best_val][1] = self.map1[best_val][-1]

# #         # return best_val

# from collections import defaultdict

# class FreqStack:

#     def __init__(self):
#         self.stack = []
        
#         # val -> [all occurrence indices]
#         self.map1 = defaultdict(list)
        
#         # val -> [frequency, recent_index]
#         self.map2 = {}
        
#         self.indx = 0

#     def push(self, val: int) -> None:

#         # Store (value, index)
#         self.stack.append((val, self.indx))

#         # Store occurrence index
#         self.map1[val].append(self.indx)

#         # Update frequency and recent index
#         if val not in self.map2:
#             self.map2[val] = [1, self.indx]
#         else:
#             self.map2[val][0] += 1
#             self.map2[val][1] = self.indx

#         self.indx += 1

#     def pop(self) -> int:

#         temp = []

#         # (frequency, recent_index, value)
#         for key, value in self.map2.items():
#             freq, recent_index = value
#             temp.append((freq, recent_index, key))

#         # Highest frequency first.
#         # If frequency is same, highest recent_index first.
#         temp.sort(reverse=True)

#         max_cnt, max_indx, val = temp[0]

#         # Remove latest occurrence
#         self.map1[val].pop()

#         # Decrease frequency
#         max_cnt -= 1

#         if max_cnt == 0:
#             del self.map2[val]
#             del self.map1[val]
#         else:
#             # New latest occurrence
#             latest_indx = self.map1[val][-1]

#             self.map2[val] = [max_cnt, latest_indx]

#         return val

import heapq

class FreqStack:

    def __init__(self):
        self.freq = {}
        self.heap = []
        self.index = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        self.index += 1
        # Store (-cnt, -indx, val) to simulate a max-heap
        heapq.heappush(self.heap, (-self.freq[val], -self.index, val))

    def pop(self) -> int:
        # Extract the highest (-cnt, -indx) priority element
        neg_cnt, neg_indx, val = heapq.heappop(self.heap)
        
        # Decrement frequency in map
        self.freq[val] -= 1
        
        return val